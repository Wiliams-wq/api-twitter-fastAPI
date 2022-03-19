# modulos propios
from models.user import User
from models.tweet import Tweet

# python
from typing import List

# fastAPI
from fastapi import FastAPI
from fastapi import status

app = FastAPI()

# path operations

# users


@app.post(
    "/signup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="register a new user",
    tags=["users"]
)
def signup(user: User):
    pass


@app.post(
    "/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="login a user",
    tags=["users"]
)
def login():
    pass
# usamos list por que de todos los que obtengamos los guarde en una lista y luego retorne un json


@app.get(
    "/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="show all users",
    tags=["users"]
)
def showAllUsers(user: User):
    pass


@app.get(
    "/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="show a user",
    tags=["users"]
)
def showAUser():
    pass


@app.put(
    "/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="update a user",
    tags=["users"]
)
def updateAUser(user: User):
    pass


@app.delete(
    "/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="delete a user",
    tags=["users"]
)
def deleteAUser(user: User):
    pass


# tweets

@app.get(
    "/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="show all tweets",
    tags=["tweets"]
)
def Home():
    return {"message": "Hello World from twitter app"}

@app.post(
    "/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="post a new tweet",
    tags=["tweets"]
)
def PostATweet():
    return {"message": "Hello World from twitter app"}

@app.get(
    "/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="show a tweet",
    tags=["tweets"]
)
def showATweet():
    return {"message": "Hello World from twitter app"}


@app.delete(
    "/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="delete a tweet",
    tags=["tweets"]
)
def deleteATweet():
    return {"message": "Hello World from twitter app"}

@app.put(
    "/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="update a tweet",
    tags=["tweets"]
)
def updateATweet():
    return {"message": "Hello World from twitter app"}
