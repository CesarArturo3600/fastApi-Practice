from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    name = str
    description = Optional[str] = None
    price = Optional[str] = Field(..., gt=0)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    name = Optional[str] = None
    description = Optional[str] = None
    price = Optional[str] = Field(None, gt=0)


class ProductResponse(ProductBase):
    id = int
    created_at = datetime
    updated_at = Optional[datetime] = None

    class Config:
        orm_mode = True
