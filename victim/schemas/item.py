"""schema artwork"""
#pylint: disable=all
from uuid import UUID
from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ItemBase(BaseModel):
    name: Optional[str] = None
    image: Optional[str] = None
    creation_date: Optional[datetime] = None
    modification_date: Optional[datetime] = None
    creator_id:int
    is_active: Optional[bool]
    team_id:Optional[UUID]=None
    company_id:Optional[UUID]=None
    


class ItemCreate(ItemBase):
    name: str
    image: str
    

class ItemUpdate(ItemBase):
    name: str
    image: str
    is_active: Optional[bool] = None


class ItemInDBBase(ItemBase):
    id: int
    name: str
    image: str
    creation_date: datetime
    modification_date: datetime
    is_active: bool

    class Config:
        orm_mode = True


class Item(ItemInDBBase):
    pass


class ItemInDB(ItemInDBBase):
    pass
