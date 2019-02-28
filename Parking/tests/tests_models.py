import pytest
from django.test import TestCase
pytestmark = pytest.mark.django_db
from Parking.models import Parking
from django.urls import reverse, resolve


class TestParking(TestCase):

    # Test url for BusLuas app
    def test_index(self):
        resp = self.client.get('/Parking/')
        self.assertEqual(resp.status_code, 200)

    # Test view for BusLuas app
    def test_home_url_resolves_home_view(self):
        view = resolve('/Parking/')
        self.assertEquals(view.view_name, 'Parking:index')

    # Testing string type models
    def test_string_representation(self):
         entry = Parking(location="Clondalkin Civic Offices", roadname="Ninth Lock Road", spacetype="Surface", Point="Point",
                         id1=236, noofspaces=2, OBJECTID=68, lat=53.291516862, long=-6.316224651)
         assert isinstance(entry.location, str)
         assert isinstance(entry.roadname, str)
         assert isinstance(entry.spacetype, str)
         assert isinstance(entry.Point, str)
         assert isinstance(entry.id1, int)
         assert isinstance(entry.noofspaces, int)
         assert isinstance(entry.OBJECTID, int)
         assert isinstance(entry.lat, float)
         assert isinstance(entry.long, float)
         # Testing string type models

    def test_int_representation(self):
        entry = Parking(id1=236, noofspaces=2, OBJECTID=68)
        assert isinstance(entry.id1, int)
        assert isinstance(entry.noofspaces, int)
        assert isinstance(entry.OBJECTID, int)

    def test_float_representation(self):
        entry = Parking(lat=53.291516862, long=-6.316224651)
        assert isinstance(entry.lat, float)
        assert isinstance(entry.long, float)
