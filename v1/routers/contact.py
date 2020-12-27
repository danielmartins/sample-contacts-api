from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException, Depends

from v1.deps import get_contacts_service
from v1.schemas.item import Contact, ContactCreate, ContactUpdate
from v1.services.item import ContactService

router = APIRouter()


@router.post("/contacts", response_model=Contact)
def create_contact(item_create: ContactCreate, contacts_service: ContactService = Depends(get_contacts_service)):
    """
    create an contact
    """
    return contacts_service.create_item(item_create)


@router.get("/contacts/{id}", response_model=Contact)
def get_contact(id: str, contacts_service: ContactService = Depends(get_contacts_service)):
    """
    get any specific contact
    """
    item = contacts_service.get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return item


@router.get("/contacts", response_model=List[Contact])
def list_contacts(contacts_service: ContactService = Depends(get_contacts_service)):
    """
    get many contacts
    """
    items = contacts_service.list_items()
    if not items:
        raise HTTPException(status_code=404, detail="Contacts not found.")
    return items


@router.put("/contacts/{id}", response_model=Contact)
def update_contact(id: UUID, item_update: ContactUpdate,
                   contacts_service: ContactService = Depends(get_contacts_service)):
    """
    update an contact
    """
    item = contacts_service.get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return contacts_service.update_item(id, item_update)


@router.delete("/contacts/{id}", response_model=Contact)
def delete_contact(id: UUID, contacts_service: ContactService = Depends(get_contacts_service)):
    """
    delete an item
    """
    item = contacts_service.get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return contacts_service.delete_item(id)
