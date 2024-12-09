import asyncio

import uvicorn
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from src.db.scripts.db_methods import set
from src.db.config.db_env import create_base
from src.db.pydantic.valid import User_model
from src.scripts.hash import hash_converter

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/users/")
async def get_data(data: User_model):
    try:
        await create_base()
        password = await hash_converter(password=bytes(data.password, encoding="utf-8"))
        asyncio.as_completed(fs=await set(nickname=data.name, password=password,
                                          country=data.country, phone_number=data.phone_number,
                                          email=data.email))
        return data
    except Exception as e:
        print(e)

app.mount("/users", app)
app.mount("/", StaticFiles(directory="templates", html=True))


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.2', port=8300)