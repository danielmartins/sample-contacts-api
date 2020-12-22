from typing import List
from uuid import UUID

from database import db
from v1.schemas.item import Contact, ContactCreate, ContactUpdate


class ItemDAO:
    collection_name = "contacts"

    def create(self, contact_create: ContactCreate) -> Contact:
        data = contact_create.dict(by_alias=True)
        print(data)
        data["id"] = str(data.pop("id"))
        doc_ref = db.collection(
            self.collection_name).document(str(contact_create.id))
        doc_ref.set(data)
        return self.get(contact_create.id)

    def get(self, id: UUID) -> Contact:
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc = doc_ref.get()
        if doc.exists:
            return Contact.from_firestore(doc_ref)

    def list(self) -> List[Contact]:
        items_ref = db.collection(self.collection_name)
        return [Contact.from_firestore(doc)
                for doc in items_ref.list_documents() if doc.get().to_dict()]

    def update(self, id: UUID, item_update: ContactUpdate) -> Contact:
        data = item_update.dict()
        doc_ref = db.collection(self.collection_name).document(str(id))
        doc_ref.update(data)
        return self.get(id)

    def delete(self, id: UUID) -> None:
        db.collection(self.collection_name).document(str(id)).delete()
