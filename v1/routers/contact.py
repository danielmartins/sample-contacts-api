from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException

from v1.schemas.item import Contact, ContactCreate, ContactUpdate
from v1.services.item import ContactService

router = APIRouter()
contacts_service = ContactService()


@router.post("/contacts", response_model=Contact, tags=["contacts"])
def create(item_create: ContactCreate):
    """
    create an contact
    """
    return contacts_service.create_item(item_create)


@router.get("/contacts/{id}", response_model=Contact, tags=["contacts"])
def get_contact(id: str):
    """
    get any specific contact
    """
    item = contacts_service.get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return item


@router.get("/contacts", response_model=List[Contact], tags=["contacts"])
def list_contacts():
    """
    get many contacts
    """
    items = contacts_service.list_items()
    if not items:
        raise HTTPException(status_code=404, detail="Contacts not found.")
    return items


@router.put("/contacts/{id}", response_model=Contact, tags=["contacts"])
def update_contact(id: UUID, item_update: ContactUpdate):
    """
    update an contact
    """
    item = contacts_service.get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return contacts_service.update_item(id, item_update)


@router.delete("/contacts/{id}", response_model=Contact, tags=["contacts"])
def delete_contact(id: UUID):
    """
    delete an item
    """
    item = contacts_service.get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return contacts_service.delete_item(id)
