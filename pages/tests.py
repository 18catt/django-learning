from django.test import TestCase, SimpleTestCase
#Testcase-incase of database
#simpletestcase- without using database


# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_sbout_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

