# main.py
from fastapi import FastAPI
from model import mod
from llm import make_agent

api = FastAPI()

db = []                 # простая "БД" в памяти
agent = make_agent(db)  # агент видит ту же ссылку на db

@api.get("/")
async def check():
    return "server on"

@api.get("/db_list")
async def dblist(head: int = 3):
    return db[:head]

@api.post("/w_mess")
async def wmess(data: mod):
    prompt = f"Добавь в базу (если допустимо): name='{data.name}', mess='{data.message}'."
    res = agent.invoke({"messages": [("user", prompt)]})
    return {"result": res["messages"][-1].content}
