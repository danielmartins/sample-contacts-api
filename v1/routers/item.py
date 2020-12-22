from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException

from v1.schemas.item import Contact, ContactCreate, ContactUpdate
from v1.services.item import ItemService

router = APIRouter()
item_service = ItemService()


@router.post("/contacts", response_model=Contact, tags=["contacts"])
def create_item(item_create: ContactCreate):
    """
    create an item
    """
    return item_service.create_item(item_create)


@router.get("/contacts/{id}", response_model=Contact, tags=["contacts"])
def get_item(id: str):
    """
    get any specific item
    """
    item = item_service.get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return item


@router.get("/contacts", response_model=List[Contact], tags=["contacts"])
def list_items():
    """
    get many items
    """
    items = item_service.list_items()
    if not items:
        raise HTTPException(status_code=404, detail="Contacts not found.")
    return items


@router.put("/contacts/{id}", response_model=Contact, tags=["contacts"])
def update_item(id: UUID, item_update: ContactUpdate):
    """
    update an item
    """
    print(id)
    item = item_service.get_item(id)
    print(item)
    if not item:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return item_service.update_item(id, item_update)


@router.delete("/contacts/{id}", response_model=Contact, tags=["contacts"])
def delete_item(id: UUID):
    """
    delete an item
    """
    print(id)
    item = item_service.get_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Contact not found.")
    return item_service.delete_item(id)
