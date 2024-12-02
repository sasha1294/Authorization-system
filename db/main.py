from tempfile import template
from urllib.request import Request

from fastapi import FastAPI, HTTPException, Body
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from db.db_env import create_base, session
import uvicorn
from db.db_methods import _set
import httpx
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='pythonProject2/templates')

class User(BaseModel):
    username: str
    email: str
    phone: int
    password: str
    country: str


@app.post("/")
async def start(user: User):
    return templates.TemplateResponse(name='index.html', context={'request': user})


@app.post("/users/")
async def create_user(data = Body()):
    print('flack 4')
    user = User(username=data['username'], email=data['email'], phone=data['phone'], password=data['password'],
                country=data['country'])
    print('flack 1')
    try:
        _set(nickname=user.username, email=user.email, phone_number=user.phone,
             password=user.password, country=user.country)
        print('flack 2')
        httpx.post(url='/users/output', data={'username': user.username, 'password': user.password,
                         'email': user.email, 'country': user.country, 'phone': user.phone, 'message': 'ok'})
    except Exception as e:
        session.rollback()
        session.close()
        raise HTTPException(status_code=400, detail="User already exists")

if __name__ == '__main__':
    create_base()
    uvicorn.run(app, host='localhost')