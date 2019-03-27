
# pytestmark = pytest.mark.django_db
from django.test import TestCase
from django.urls import reverse, resolve
from datetime import datetime
import django.utils.timezone

class APIHandlingTestCase(TestCase):
    # def test_index1(self):
    #     resp = self.client.get('/APIHandling/')
    #     print(resp)
    #     self.assertEqual(resp.status_code, 200)

    # Test view for BusLuas app
    def test_home_url_resolves_home_view(self):
        view = resolve('/APIHandling/')
        self.assertEquals(view.view_name, 'APIHandling:index')
