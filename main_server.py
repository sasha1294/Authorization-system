import asyncio

import phonenumbers
import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from src.db.scripts.db_methods import create_user
from src.db.config.db_env import create_base
from src.db.pydantic.valid import User
from src.scripts.hash import hash_converter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/users")
async def get_data(data: User):
    try:
        await create_base()
        data.password = await hash_converter(password=bytes(data.password, encoding="utf-8"))
        trenton = await create_user(data)
        res = asyncio.run(trenton)
        return ORJSONResponse(status_code=200, content=str(res))
    except Exception as e:
        print(e)


app.mount("/users", app)
app.mount("/", StaticFiles(directory="templates", html=True))

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="info")
