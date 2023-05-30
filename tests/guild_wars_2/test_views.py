"""
tests for views
"""
def test_index_ok(client):
    """
    checking if the initial index view works properly
    """
    # Make a GET request to / and store the response object
    # using the Django test client.
    response = client.get('/')
    # Assert that the status_code is 200 (OK)
    assert response.status_code == 200
