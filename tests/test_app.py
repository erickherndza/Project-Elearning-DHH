import unittest
from app import app  # Asegúrate de que puedas importar tu aplicación Flask aquí


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_lesson(self):
        response = self.app.get('/lesson/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_invalid_lesson(self):
        response = self.app.get('/lesson/999', follow_redirects=True)
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
