from django.test import TestCase, SimpleTestCase  # when we don't work with models SimpleTestCase could be used instead of TestCase
from django.urls import reverse, resolve  # it checks that if given url and view both match

from .views import HomePageView


class HomePageTest(SimpleTestCase):

    def setUp(self) -> None:
        self.response = self.client.get(reverse('pages:home'))

    def test_home_status_code(self):
        # response = self.client.get('/')
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'home.html')

    def test_home_url_name(self):
        # response = self.client.get(reverse('pages:home'))
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_contains_correct_html(self):
        # response = self.client.get('/')
        self.assertContains(self.response, 'HomePage')

    def test_homepage_does_not_contains_incorrect_html(self):
        # response = self.client.get('/')
        self.assertNotContains(self.response, 'this text is not in Home page!')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
