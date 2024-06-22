import importlib

import pytest
from readyapi.testclient import TestClient
from sqldev import Session

from docs_src.tutorial.readyapi.app_testing.tutorial001 import main as app_mod
from docs_src.tutorial.readyapi.app_testing.tutorial001 import test_main_006 as test_mod
from docs_src.tutorial.readyapi.app_testing.tutorial001.test_main_006 import (
    client_fixture,
    session_fixture,
)

assert session_fixture, "This keeps the session fixture used below"
assert client_fixture, "This keeps the client fixture used below"


@pytest.fixture(name="prepare")
def prepare_fixture(clear_sqldev):
    # Trigger side effects of registering table models in SQLDev
    # This has to be called after clear_sqldev, but before the session_fixture
    # That's why the extra custom fixture here
    importlib.reload(app_mod)


def test_tutorial(prepare, session: Session, client: TestClient):
    test_mod.test_create_hero(client)
