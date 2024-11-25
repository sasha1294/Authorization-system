from db_env import session
from forms import Users
from sqlalchemy import update, select

#all data states: nickname, country, phone_number, password


def _set(email:str, nickname:str, password:str, country:str, phone_number:int):
    try:
        user = Users(nickname=nickname,
                password=password,
                country=country,
                phone_number=phone_number,
                email=email)

        session.add(user)
        session.commit()
        session.close()
        return "Successfully added"
    except Exception as e:
        return f"Error action: {e}"


def update_password(email: str, new_password: str):
    try:
        update_obj = update(Users).where(Users.email == email).values({"password": new_password})
        session.execute(update_obj)
        session.commit()
        session.close()
        return "Update is successful"

    except:
        return "Error action"


def update_nickname(email: str, password: str, new_nickname: str):
    try:
        update_obj = (update(Users).where(Users.email == email and Users.password == password)
                      .values({"nickname": new_nickname}))
        session.execute(update_obj)
        session.commit()
        session.close()
        return "Update is successful"

    except:
        return "Error action"


def update_email(nickname: str, password: str, new_email: str):
    try:
        update_obj = (update(Users).where(Users.email == nickname and Users.password == password)
                      .values({"nickname": new_email}))
        session.execute(update_obj)
        session.commit()
        session.close()
        return "Update is successful"
    except:
        return 'Error action'


def authorisation_by_email(email: str, password: str):
    try:
        id = select(Users.id).where(Users.email==email and Users.password==password)
        return f"User {id} is successful authorised"

    except:
        return "Failed action"


def authorisation_by_nickname(nickname: str, password: str):
    try:
        id = select(Users.id).where(Users.nickname == nickname and Users.password == password)
        return f"User {id} is successful authorised"

    except:
        return "Failed action"


