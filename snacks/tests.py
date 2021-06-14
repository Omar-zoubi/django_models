from django.test import TestCase
from django.urls import reverse

class snackstest(TestCase):
    def test_home(self):
        url = reverse('list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_templete(self):
        url = reverse('list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'list.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_templete_tow(self):
        url = reverse('details')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'details.html')
        self.assertTemplateUsed(response, 'base.html')