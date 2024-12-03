from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
def read_admin():
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
def read_user(
    user_id: Annotated[
        int,
        Path(
            title="Enter User ID",
            description="User ID must be an integer between 1 and 100",
            ge=1,
            le=100,
        ),
    ]
):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
def read_user_info(
    username: Annotated[
        str,
        Path(
            title="Enter username",
            description="Username must be a string between 5 and 20 characters",
            min_length=5,
            max_length=20,
        ),
    ],
    age: Annotated[
        int,
        Path(
            title="Enter age",
            description="Age must be an integer between 18 and 120",
            ge=18,
            le=120,
        ),
    ],
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
