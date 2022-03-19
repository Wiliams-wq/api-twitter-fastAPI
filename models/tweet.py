#modulos propios
from models.user import User
#python
from typing import Optional
from uuid import UUID
from datetime import date, datetime

#pydantic
from pydantic import BaseModel, Field

#clase que es modelo de los tweets realizados por los usuarios
class Tweet(BaseModel):
    tweet_id: UUID = Field(..., alias="id")
    content: str = Field(..., min_length=2, max_length=140)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    #el tweet tiene un usuario que es la clase user
    by:User = Field(..., alias="user")