# from django.test import TestCase
# from Parking.models import Parking
# import datetime
# class TestParking(TestCase):
#   # Test response of App BusLuas
#   def test_index(self):
#         resp = self.client.get('/Parking/')
#         self.assertEqual(resp.status_code, 200)
#   #Testing string type models
#   def test_string_representation(self):
#        park_data = Parking(id1=145)
#        print(park_data)
#        self.assertEqual(int(park_data), park_data.id1)
  #def test_string_representation(self):
   #     parkingLocation = Parking(roadname="Ninth Lock Road")
    #    self.assertEqual(str(roadname), parkingLocation.roadname)
  #def test_string_representation(self):
   #     parkingSpacetype = Parking(spacetype="Surface")
    #    print(parkingSpacetype)
     #   self.assertEqual(str(parkingSpacetype), parkingSpacetype.spacetype)
  #def test_string_representation(self):
  #      irishrail = BusLuas(Origin="E920")
  #      print(irishrail)
  #      self.assertEqual(str(irishrail), irishrail.Origin)
  #def test_string_representation(self):
  #      irishrail = BusLuas(Destination="E920")
  #      print(irishrail)
  #      self.assertEqual(str(irishrail), irishrail.Destination)
  #def test_string_representation(self):
  #      irishrail = BusLuas(Status="E920")
  #      print(irishrail)
  #      self.assertEqual(str(irishrail), irishrail.Status)
import pytest
from django.test import TestCase
#from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from Parking.models import Parking
from datetime import datetime
import django.utils.timezone
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
