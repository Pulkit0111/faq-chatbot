from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

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