from fastapi import FastAPI
from model import mod

api = FastAPI()

db = []

@api.get('/')
async def check():
    return 'server on'

@api.get('/db_list')
async def dblist(head=3):
    return db[:head]

@api.post('/w_mess', response_model=mod)
async def wmess(data: mod):
    db.append({'name': data.name, 'message': data.message})
    return data