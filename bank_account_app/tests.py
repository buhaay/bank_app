from django.test import TestCase
from django.urls import reverse


class RegisterTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.home_page = reverse('home_page')
        self.login_url = reverse('home_page')
        self.user = {
            'username': 'username',
            'email': 'qw@qw.qw',
            'password1': 'SuperSecretPassword666',
            'password2': 'SuperSecretPassword666'
        }
        return super().setUp()

    def test_user_can_register(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertRedirects(response, reverse('login'))

