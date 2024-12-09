from src.db.shemas.forms import Users
from sqlalchemy import update, select
from src.db.config.db_env import session
import asyncio

#all data states: nickname, country, phone_number, password

async def set(email:str, nickname:str, password:str, country:str, phone_number:int):
    try:
        user = Users(nickname=nickname,
                password=password,
                country=country,
                phone_number=phone_number,
                email=email)
        session.add(user)
        await session.commit()

    except Exception as e:
        print(e)


async def update_password(email: str, new_password: str):
    try:
        update_obj = update(Users).where(Users.email == email).values({"password": new_password})
        await session.execute(update_obj)
        await session.commit()
        await session.close()
        return {"action": "Successfully added",
                "code": 200}

    except Exception as e:
        return {"action": f"Error action: {e}",
                "code": 405}


async def update_nickname(email: str, password: str, new_nickname: str):
    try:
        update_obj = (update(Users).where(Users.email == email and Users.password == password)
                      .values({"nickname": new_nickname}))
        await session.execute(update_obj)
        await session.commit()
        await session.close()
        return {"action": "Successfully added",
                "code": 200}

    except Exception as e:
        return {"action": f"Error action: {e}",
                "code": 405}


async def update_email(nickname: str, password: str, new_email: str):
    try:
        update_obj = (update(Users).where(Users.email == nickname and Users.password == password)
                      .values({"nickname": new_email}))
        await session.execute(update_obj)
        await session.commit()
        await session.close()
        return {"action": "Successfully added",
                "code": 200}

    except Exception as e:
        return {"action": f"Error action: {e}",
                "code": 405}


async def authorisation_by_email(email: str, password: str):
    try:
        id = select(Users.id).where(Users.email==email and Users.password==password)
        return {"action": "Successfully",
                "code": 200,
                "data": id}

    except Exception as e:
        return {"action": f"Error action: {e}",
                "code": 405}


async def authorisation_by_nickname(nickname: str, password: str):
    try:
        id = select(Users.id).where(Users.nickname == nickname and Users.password == password)
        return {"action": "Successfully",
                "code": 200,
                "data": id}

    except Exception as e:
        return {"action": f"Error action: {e}",
                "code": 405}


async def Select_by_email(email: str, password: str):
    try:
        data = select(Users).where(Users.email == email and Users.password == password)
        return {"action": "Successfully",
                "code": 200,
                "data": data}

    except Exception as e:
        return {"action": f"Error action: {e}",
                "code": 405}


async def Select_by_nickname(nickname: str, password: str):
    try:
        data = select(Users).where(Users.nickname == nickname and Users.password == password)
        return {"action": "Successfully",
                "code": 200,
                "data": data}

    except Exception as e:
        return {"action": f"Error action: {e}",
                "code": 405}


