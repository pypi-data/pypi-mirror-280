import importlib

import pytest

from docs_src.tutorial.readyapi.app_testing.tutorial001 import main as app_mod
from docs_src.tutorial.readyapi.app_testing.tutorial001 import test_main_001 as test_mod


@pytest.fixture(name="prepare", autouse=True)
def prepare_fixture(clear_sqldev):
    # Trigger side effects of registering table models in SQLDev
    # This has to be called after clear_sqldev
    importlib.reload(app_mod)
    importlib.reload(test_mod)


def test_tutorial():
    test_mod.test_create_hero()
