import conftest

def test_list_books_returns_200(client):
    response = client.get(conftest.get_all_books_url)
    assert response.status_code == 200

# def test_list_books_returns_a_list(client):
#     pass

# def test_list_books_contains_three_items(client):
#     pass

# def test_each_book_has_required_fields(client):
#     pass
