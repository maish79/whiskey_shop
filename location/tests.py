from django.test import TestCase

# Create your tests here.
class TestLocationViews(TestCase):
    """
    A class for testing location views
    """
    def test_get_location_page(self):
        """
        This test checks if the location page is displayed
        """
        response = self.client.get('/locations/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'locations.html')

    def test_get_add_location_page(self):
        """
        This test checks if the add location page is displayed
        """
        response = self.client.get('/locations/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_location.html')