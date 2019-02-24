from django.test import TestCase
from BusLuas.models import BusLuas
import datetime
class TestIrishRail(TestCase):
  # Test response of App BusLuas
  def test_index(self):
        resp = self.client.get('/BusLuas/')
        self.assertEqual(resp.status_code, 200)
  #Testing string type models
  def test_string_representation(self):
        irishrail = BusLuas(TrainCode="E920")
        self.assertEqual(str(irishrail), irishrail.TrainCode)
  def test_string_representation(self):
        stationfullname = BusLuas(StationFullName="Dalkey")
        self.assertEqual(str(stationfullname), stationfullname.StationFullName)
  def test_string_representation(self):
        code = BusLuas(StationCode="DLKEY")
        print(code)
        self.assertEqual(str(code), code.StationCode)   
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