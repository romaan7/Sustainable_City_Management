import pytest
pytestmark = pytest.mark.django_db
from django.test import TestCase
from django.urls import reverse, resolve


# class TestUrls(TestCase):
#
#   #    #Test Urls.py
#   # def test_parking_url(self):
#   #      path = reverse('parking_data')
#   #      assert resolve(path).view_name == 'parking_data'
#
#   def test_home_url_resolves_home_view(self):
#       view = resolve('/Parking/')
#       self.assertEquals(view.view_name, 'Parking:index')