import os
import openai
from dotenv import load_dotenv

load_dotenv(".env")

openai.api_key = os.environ.get("OPENAI_API_KEY")

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

print(llm.invoke("龙年出生的女宝宝，希望名字的寓意美好，请你取个好听的名字，我姓吴").content)
