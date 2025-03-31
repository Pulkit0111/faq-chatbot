from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_firestore import FirestoreChatMessageHistory
from google.cloud import firestore
from dotenv import load_dotenv

load_dotenv()

# Firestore Configuration
PROJECT_ID = "langchain-e21d8"
SESSION_ID = "user_session_new"
COLLECTION_NAME = "qna_bot_history"

client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)

print("Chat History Initialized")
print("Current chat history: ", chat_history.messages)

model = ChatOpenAI(model = "gpt-3.5-turbo")

def generate_response(user_query):
    
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that can answer FAQs."),
        ("human", "{user_query}"),
    ])
    
    prompt = prompt_template.invoke({"user_query": user_query})
    response = model.invoke(prompt)
    return response.content

while True:
    user_query = input("You: ")
    if user_query.lower() == "exit":
        print("Exiting...")
        break
    chat_history.add_user_message(user_query) # Add user message to chat history
    response = generate_response(user_query) # Generate response from model
    chat_history.add_ai_message(response) # Add AI message to chat history
    print("Bot: ", response)

