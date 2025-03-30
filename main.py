from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

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
    response = generate_response(user_query)
    print("Bot: ", response)

