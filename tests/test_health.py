import conftest

# --- ROOT --- #
def test_root_return_200(client):
    response = client.get(conftest.root_url)
    assert response.status_code == 200

def test_root_returns_json_content_type(client):
    response = client.get(conftest.root_url)
    assert "application/json" in response.headers["content-type"]

def test_root_body_has_message_key(client):
    response = client.get(conftest.root_url)
    assert "message" in response.json()

def test_openapi_schema_is_available(client):
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert "openapi" in response.json()

# --- HEALTH --- #
def test_health_return_200(client):
    response = client.get(conftest.health_url)
    assert response.status_code == 200

def test_health_returns_json_content_type(client):
    response = client.get(conftest.health_url)
    assert "application/json" in response.headers["content-type"]

def test_health_body_has_message_key(client):
    response = client.get(conftest.health_url)
    assert "healthcheck" in response.json()
    assert response.json()["healthcheck"] == "successed"

