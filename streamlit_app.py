# In preparation for Automated Question Maker.

import streamlit as st
from openai import OpenAI

# Show title and description.
st.title("💬 Chatbot...💬")
st.write( "This is a simple chatbot . ")

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
#openai_api_key = st.text_input("OpenAI API Key", type="password")

# Global variable
query = "Create a Question with Answer."

def new_query(query):
    return query
# End of Function

def store_n_display(prompt):
        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate a response using the OpenAI API.
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )

#end of Function

        # Stream the response to the chat using `st.write_stream`, then store it in 
        # session state.
        with st.chat_message("assistant"):
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})




openai_api_key = st.secrets["openai"]["secret_key"]
client = OpenAI(api_key=openai_api_key)
if not client:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:


    # Create a session state variable to store the chat messages. This ensures that the
    # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
    

    if st.button("Submit"):
        # Call the `new_query` function with the global `query` variable
        prompt = new_query(query)
        st.write(prompt)
        store_n_display(prompt)
    
    elif prompt := st.chat_input("What is up?"):
        st.write(prompt)
        store_n_display(prompt)

