from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

app = FastAPI()

app.mount("/templates", StaticFiles(directory="templates"), name="templates")

class User(BaseModel):
    username: str
    email: str
    phone: int
    password: str


@app.post("/users/")
async def create_user(user: User):
    db = SessionLocal()
    db_user = User(username=user.username, email=user.email, phone=user.phone, password=user.password)

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="User already exists")
    finally:
        db.close()

if __name__ == '__main__':
    uvicorn.run(app, host='localhost')
