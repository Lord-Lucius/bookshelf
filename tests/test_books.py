import conftest

def test_list_books_returns_200(client):
    response = client.get(conftest.get_all_books_url)
    assert response.status_code == 200

def test_list_books_returns_a_list(client):
    response = client.get(conftest.get_all_books_url)
    assert type(response.json()) is list

def test_list_books_contains_three_items(client):
    response = client.get(conftest.get_all_books_url)
    assert len(response.json()) == 3

def test_each_book_has_required_fields(client):
    response = client.get(conftest.get_all_books_url)
    for item in response.json():
        assert "id" in item
        assert "title" in item
        assert "author" in item
        assert "year" in item
        assert "pages" in item
