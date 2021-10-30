def test_get_all_planets_with_no_records(client):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []


"""
def test_get_one_book(client, two_saved_planets):
    response = client.get("/books/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {"id": 1, "title": "Ocean Book", "description": "watr 4evr"}
"""
