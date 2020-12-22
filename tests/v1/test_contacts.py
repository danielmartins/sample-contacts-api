from uuid import uuid4

from starlette.testclient import TestClient

from tests.v1.factories import ContactFactory


def test_no_contacts(client: TestClient):
    request = client.get("/v1/contacts")
    assert request.status_code == 404

    request = client.get(f"/v1/contacts/{str(uuid4())}")
    assert request.status_code == 404

    request = client.put(
        f"/v1/contacts/{str(uuid4())}", json=ContactFactory.mock_item)
    assert request.status_code == 404

    request = client.delete(f"/v1/contacts/{str(uuid4())}")
    assert request.status_code == 404


def test_create_contact(client: TestClient):
    request = client.post("/v1/contacts", json=ContactFactory.mock_item)
    assert request.status_code == 200
    data = request.json()
    assert data.get("name") == "A contacts name"
    assert data.get("gender")
    assert data.get("phone")
    assert data.get("email")


def test_get_item(client: TestClient):
    request = client.post("/v1/contacts", json=ContactFactory.mock_item)
    assert request.status_code == 200
    data = request.json()
    assert data.get("name") == "A contacts name"

    item_id = data.get("id")
    request = client.get(f"/v1/contacts/{item_id}")
    assert request.status_code == 200
    data = request.json()
    assert data.get("name") == "A contacts name"


def test_list_contacts(client: TestClient):
    request = client.get("/v1/contacts")
    assert request.status_code == 200
    assert len(request.json()) == 2


def test_update_item(client: TestClient):
    request = client.post("/v1/contacts", json=ContactFactory.mock_item)
    assert request.status_code == 200
    data = request.json()
    assert data.get("name") == "A contacts name"

    item_id = data.get("id")
    request = client.put(f"/v1/contacts/{item_id}",
                         json=ContactFactory.updated_mock_item)
    assert request.status_code == 200
    data = request.json()
    assert data.get("name") == "A contacts name updated"


def test_delete_item(client: TestClient):
    request = client.post("/v1/contacts", json=ContactFactory.mock_item)
    assert request.status_code == 200
    data = request.json()
    item_id = data.get("id")

    request = client.delete(f"/v1/contacts/{item_id}")
    assert request.status_code == 200

    request = client.get("/v1/contacts")
    assert request.status_code == 200
    assert item_id not in [item.get("id") for item in request.json()]
