import os

import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests():
    os.environ["DEBUG"] = "False"
