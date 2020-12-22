from typing import Union, Optional
from uuid import uuid4

from pydantic import BaseModel, Field, EmailStr, UUID4


class ContactBase(BaseModel):
    name: str
    gender: str
    phone: str
    email: EmailStr


class ContactCreate(ContactBase):
    id: Union[str, UUID4] = Field(default_factory=uuid4, alias='id')


class ContactUpdate(ContactBase):
    pass


class Contact(ContactBase):
    id: Union[str, UUID4]

    class Config:
        orm_mode = True

    @classmethod
    def from_firestore(cls, instance):
        data = instance.get().to_dict()
        data.update({"id": instance.id})
        return cls(**data)
