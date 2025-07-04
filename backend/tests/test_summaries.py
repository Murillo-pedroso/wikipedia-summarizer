import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/")
    assert r.status_code == 200
    assert "message" in r.json()

def test_create_and_list(tmp_path, monkeypatch):
    # monkeypatch do OpenAI + requests para não chamar a API de verdade
    monkeypatch.setenv("OPENAI_API_KEY", "test")
    def fake_scrape(url): return "foo bar baz"
    monkeypatch.setattr("app.services.scrape_text", fake_scrape)
    def fake_summarize(text): return "resumido"
    monkeypatch.setattr("app.services.summarize_text", fake_summarize)

    # cria summary
    r1 = client.post("/summaries/", json={"url":"http://example.com"})
    assert r1.status_code == 200
    data1 = r1.json()
    assert data1["summary"] == "resumido"

    # lista summaries
    r2 = client.get("/summaries/")
    assert r2.status_code == 200
    assert len(r2.json()) >= 1
