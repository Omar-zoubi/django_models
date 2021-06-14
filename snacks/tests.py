from django.test import TestCase
from django.urls import reverse
from .views import snacksListView, snackDetailView

# Create your tests here.

class snackTests(TestCase):
    def test_home(self):
        url = reverse('list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        url = reverse('list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_details_code(self):
        url = reverse('details', args="1")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_details_template(self):
        url = reverse('details', args="1")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)