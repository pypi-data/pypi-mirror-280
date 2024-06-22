import pytest  # (1)!
from readyapi.testclient import TestClient
from sqldev import Session, SQLDev, create_engine
from sqldev.pool import StaticPool

from .main import app, get_session


@pytest.fixture(name="session")  # (2)!
def session_fixture():  # (3)!
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLDev.metadata.create_all(engine)
    with Session(engine) as session:
        yield session  # (4)!


def test_create_hero(session: Session):  # (5)!
    def get_session_override():
        return session  # (6)!

    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)

    response = client.post(
        "/heroes/", json={"name": "Deadpond", "secret_name": "Dive Wilson"}
    )
    app.dependency_overrides.clear()
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Deadpond"
    assert data["secret_name"] == "Dive Wilson"
    assert data["age"] is None
    assert data["id"] is not None
