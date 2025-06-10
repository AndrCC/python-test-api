import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import app


@pytest.fixture
def client(monkeypatch, tmp_path):
    blacklist = tmp_path / "blacklist.txt"
    blacklist.write_text("")
    monkeypatch.setenv("BLACKLIST_FILE", str(blacklist))
    application = app.create_app()
    application.config["TESTING"] = True
    with application.test_client() as client:
        yield client


def test_free_cpf(client):
    resp = client.get("/12345678900")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "FREE"}


def test_invalid_characters(client):
    resp = client.get("/123-456-78x-00")
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_invalid_length(client):
    resp = client.get("/12345678")
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_blocked_cpf(monkeypatch, tmp_path):
    blacklist = tmp_path / "blacklist.txt"
    blacklist.write_text("11111111111\n")
    monkeypatch.setenv("BLACKLIST_FILE", str(blacklist))
    application = app.create_app()
    application.config["TESTING"] = True
    with application.test_client() as client:
        resp = client.get("/11111111111")
        assert resp.status_code == 200
        assert resp.get_json() == {"status": "BLOCK"}
