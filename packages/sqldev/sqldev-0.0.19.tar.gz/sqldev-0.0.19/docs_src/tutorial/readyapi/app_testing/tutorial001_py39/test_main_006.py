import pytest
from readyapi.testclient import TestClient
from sqldev import Session, SQLDev, create_engine
from sqldev.pool import StaticPool

from .main import app, get_session


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLDev.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")  # (1)!
def client_fixture(session: Session):  # (2)!
    def get_session_override():  # (3)!
        return session

    app.dependency_overrides[get_session] = get_session_override  # (4)!

    client = TestClient(app)  # (5)!
    yield client  # (6)!
    app.dependency_overrides.clear()  # (7)!


def test_create_hero(client: TestClient):  # (8)!
    response = client.post(
        "/heroes/", json={"name": "Deadpond", "secret_name": "Dive Wilson"}
    )
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Deadpond"
    assert data["secret_name"] == "Dive Wilson"
    assert data["age"] is None
    assert data["id"] is not None
