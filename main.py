import streamlit as st
import time
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

st.title("🤖 FAQ Chatbot")
st.caption("I am your friendly AI assistant. Ask me anything!")

# OpenAI model to generate the responses
model = ChatOpenAI(model="gpt-3.5-turbo")

# Generate response
def generate_response(prompt):
    
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that can answer anything."),
        ("human", "{user_query}"),
    ])
    
    human_prompt = prompt_template.invoke({"user_query": prompt})
    response = model.invoke(human_prompt)
    return response.content

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Ask me anything! 👇"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What's up!"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Let me think...."):
            assistant_response = generate_response(prompt)
        
        full_response = ""
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
