from typing import List

from v1.daos.item import ItemDAO
from v1.schemas.item import Contact, ContactCreate, ContactUpdate

item_dao = ItemDAO()


class ItemService:
    def create_item(self, item_create: ContactCreate) -> Contact:
        return item_dao.create(item_create)

    def get_item(self, id: str) -> Contact:
        return item_dao.get(id)

    def list_items(self) -> List[Contact]:
        return item_dao.list()

    def update_item(self, id: str, item_update: ContactUpdate) -> Contact:
        return item_dao.update(id, item_update)

    def delete_item(self, id: str) -> None:
        return item_dao.delete(id)
