import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from src.db.scripts.db_methods import set
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

create_base()

@app.post("/users")
async def get_data(data: User):
    try:
        data.password = await hash_converter(password=bytes(data.password, encoding="utf-8"))
        set(email=data.email, nickname=data.username, password=data.password, country=data.country,
            phone_number=data.phone)
        return FileResponse("templates/users.html")
    except Exception as e:
        print(e)



app.mount("/users", app)
app.mount("/", StaticFiles(directory="templates", html=True))

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.2', port=8000, log_level="info")
