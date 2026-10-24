import app.app as application

def test_home_returns_success():
    client = application.app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["message"] == "Python app is running"

def test_unknown_route_returns_404():
    client = application.app.test_client()

    response = client.get("/route-that-does-not-exist")

    assert response.status_code == 404
