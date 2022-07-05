import pytest
import app
from controllers import members

@pytest.fixture
def api(monkeypatch):
    test_members = [
        {'id': 1, 'name': 'sam', 'alter-ego': "not sam"},
        {'id': 2, 'name': 'gio', 'alter-ego': "not gio"}
    ]
    monkeypatch.setattr(members, "members", test_members)
    api = app.app.test_client()
    return api
