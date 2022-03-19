#modulos propios
from userBase import UserBase

#pydantic
from pydantic import Field

#clase que se usa solo cuanod se quiere loguear por eso solo tiene el password
class userLogin(UserBase):
    password: str = Field(...,min_length=8, max_length=128, alias="password")
