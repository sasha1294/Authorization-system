from fastapi import Depends
from src.configurations.config import router_set, router_init, router_select, router_update, app
from src.db.pydantic.valid import User
from src.db.scripts.db_methods import (create_user, update_email, update_password, update_nickname,
                                       Select_by_email, Select_by_nickname, authorisation_by_email,
                                       authorisation_by_nickname)
import uvicorn
import asyncio
from src.db.config.db_env import create_base
from src.scripts.hash import hash_converter
import httpx


@router_set.post(path="/set")
async def set_user(data: User):
    try:
        await create_base()
        password = await hash_converter(password=bytes(data.password, encoding="utf-8"))
        asyncio.as_completed(fs=await create_user(nickname=data.name, password=password,
                                                  country=data.country, phone_number=data.phone_number,
                                                  email=data.email))

        code = httpx.post(url="https://127.0.0.2:8300/users/").status_code
        if code == 200:
            httpx.post("https://127.0.0.2:8300/users/", data={"message": "OK",
                                             "name": data.nickname,
                                             "email": data.email,
                                             "country": data.country,
                                             "phone": data.phone_number}, verify=True)


    except Exception as e:
        print(e)
        code = httpx.post(url="https://127.0.0.2:8300/users/").status_code
        if code == 200:
            httpx.post("https://127.0.0.2:8300/users/", data={"message": "valid error"})

        else:
            print('server not connect')



app.include_router(router_set)

if __name__ == "__main__":
    uvicorn.run(host="localhost", port=8000, app=app)