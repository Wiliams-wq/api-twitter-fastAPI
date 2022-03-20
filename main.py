# modulos propios
from models.user import User
from models.tweet import Tweet
from models.userRegister import UserRegister

# python
from typing import List
import json


# fastAPI
from fastapi import FastAPI
from fastapi import status, Body

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
# recibe el usuario de tipo UserRegister del body obligatoriamente
def Signup(user: UserRegister = Body(...)):
    '''
    SignUp
     this path operation  register a user in the app
    parameters:
        -Request Body paremet
    Returns a json with de basic user information
        -user_id: UUID
        -email: EmailStr
        -first_name: str
        -last_name: str
        -birth_date: Optional[date]
    '''
# abrimos el arhivo json y con r+ lo dejamos para que se pueda leer y escribir, usamos utf-8 y el nombre con
# el que vamos a trabajar sera file
    with open("users.json", "r+", encoding="utf-8") as file:
        # en results guardamos lo que se haya leido del archivo pasandolo a diccionario de python
        results = json.loads(file.read())
# a la variable user_dict gurdamos el objeto user que se recibe en el body pasandolo a dicionario de python
        user_dict = user.dict()
# converimos el uuid a string para poder guardarlo en el diccionario
        user_dict["user_id"] = str(user_dict["user_id"])
# converitmos la fecha a string para poder guardarla en el diccionario
        user_dict["birth_date"] = str(user_dict["birth_date"])
# agregamos a results el diccionario user_dict
        results.append(user_dict)
# no ubicamos en el lugar cero del arhivo file
        file.seek(0)
# escribimos en el archivo file el diccionario results pasandolo a json con dumps
        file.write(json.dumps(results))
# retornamos el usuario
        return user


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
def showAllUsers():

    # se lee el archivo users.json y se guarda en results para retornarlo, hay errores por lo que se debe
    # manejar
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results


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
def updateAUser():
    pass


@app.delete(
    "/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="delete a user",
    tags=["users"]
)
def deleteAUser():
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
    """
            This path operation shows all users in the app
            Parameters:
                -
            Returns a json list with all users in the app, with the following keys:
                - tweet_id: UUID
                - content: str
                - created_at: datetime
                - updated_at: datetime
                - by: User
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results
    


@app.post(
    "/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="post a new tweet",
    tags=["tweets"]
)
def PostATweet(tweet: Tweet = Body(...)):
    """
This path operation post a new tweet in the app

Parameters: 
    -REquest Body
        -tweet: Tweet

Returns a json with the basic information of the tweet
    - tweet_id: UUID
    - constent: str
    - created_at: datetime
    - updated_at: datetime(optional)
    -by: User


"""

    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        # se castea todos los datos que no sean json
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["updated_at"] = str(tweet_dict["updated_at"])
        # como el usuario tiene datos del usuario, entonces se castea los datos del usuario
        # como su uuid y el año de nacimiento.
        # esto esta en el json by y luego user_id
        tweet_dict["by"]["user_id"] = str(tweet_dict["by"]["user_id"])
        tweet_dict["by"]["birth_date"] = str(tweet_dict["by"]["birth_date"])

        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet


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
