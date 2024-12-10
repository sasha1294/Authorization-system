from celery.bin.result import result
from pydantic_extra_types.phone_numbers import PhoneNumber

from fastapi import HTTPException, status
from src.db.shemas.forms import Users
from sqlalchemy import update, select
from src.db.config.db_env import session

async def create_user(data: Users):
    try:
        user = Users(name=data.name,
                password=data.password,
                country=data.country,
                phone_number=data.phone_number,
                email=data.email)
        session.add(user)
        await session.commit()
        return "Success"

    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail=str(e))


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


