from tests.units.client import client


class TestAddClothe:
    def test_add_clothe_successfully(self):
        response = client.post('/api/clothes/')

        assert response.status_code == 201
        assert response.json() == {"message": "Look at THIS! You are awesome!"}
