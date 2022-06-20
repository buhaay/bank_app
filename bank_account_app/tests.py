from django.test import TestCase
from django.urls import reverse


class RegisterTest(TestCase):
    def setUp(self):
        self.home_page = reverse('home_page')
        return super().setUp()

    def test_can_view_home_page(self):
        response = self.client.get(self.home_page)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page.html')
