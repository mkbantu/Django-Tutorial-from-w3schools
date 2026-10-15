from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_homepage_renders_bootstrap_and_destination_links(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'bootstrap@5.3.8')
        self.assertContains(response, '<h1 class="display-4 fw-bold mb-3">See more of the world.</h1>')
        self.assertContains(response, f'href="{reverse("africa_tours")}"')
        self.assertContains(response, f'href="{reverse("asia_tours")}"')
