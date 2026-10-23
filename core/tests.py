from django.test import TestCase


class HomeViewTests(TestCase):
    def test_home_displays_username_and_context(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome back, Victor!')
        self.assertContains(response, '3 courses in progress')
        self.assertContains(response, 'Django ORM')
