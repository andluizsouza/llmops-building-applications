import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI


def setup_credentials():
    
    load_dotenv(".env")
    GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
    genai.configure(api_key=GOOGLE_API_KEY)


def get_completion(prompt, model="gemini-1.5-flash"):

    llm = ChatGoogleGenerativeAI(
        model=model, temperature=0.0, max_output_tokens=1024
    )
    response = llm.invoke(prompt)

    return response.content