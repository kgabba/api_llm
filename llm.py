# llm.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType
from langgraph.prebuilt import create_react_agent

INSTRUCT = (
    "Ты вежливый агент. Если сообщение содержит мат/оскорбления — не добавляй в базу, "
    "ответь вежливо отказом. Иначе используй инструмент add_bd для добавления."
)

load_dotenv()

def make_agent(db: list):
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url="https://aleron-llm.neuraldeep.tech/",
        temperature=0
    )

    @tool
    def add_bd(name: str, mess: str) -> str:
        """Добавляет сообщение в БД. Аргументы: name (str), mess (str)."""
        db.append({"name": name, "message": mess})
        return f"Спасибо, {name}. Ваше сообщение загружено в базу."

    tools = [add_bd]

    agent = create_react_agent(llm, tools, prompt=INSTRUCT)
    return agent
