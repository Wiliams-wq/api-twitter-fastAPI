#modulos propios
from models.userBase import UserBase

#python
from typing import Optional
from datetime import date

#pydantic
from pydantic import Field

#clase que se le muestra al cliente, nombre apellido y fecha de nacimiento, asi como
#el email y el id por ser heredados
class User(UserBase):
    first_name: str = Field(...,min_length=2, max_length=50)
    last_name: str = Field(...,min_length=2, max_length=50)
    birth_date: Optional[date] = Field(None)