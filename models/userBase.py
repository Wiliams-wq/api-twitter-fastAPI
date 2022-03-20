#python
from uuid import UUID

#pydantic
from pydantic import BaseModel, EmailStr, Field

#clase padre que hereda a los hijos el id y el email
class UserBase(BaseModel):
    user_id: UUID = Field(..., alias="id")
    email: EmailStr = Field(..., alias="email")
