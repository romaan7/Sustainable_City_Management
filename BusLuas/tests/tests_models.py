import pytest
from django.test import TestCase
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from BusLuas.models import BusLuas
from datetime import datetime
import django.utils.timezone 
#from BusLuas.views import BusLuasView
from django.urls import reverse, resolve

class TestIrishRail(TestCase):
   
  #Initialize Model
  def test_init(self):
        obj = mixer.blend('BusLuas.BusLuas')
        self.assertEqual(obj.pk,1)
       
  # Test url for BusLuas app
  def test_index(self):
        resp = self.client.get('/BusLuas/')
        self.assertEqual(resp.status_code, 200)
 
  #Test view for BusLuas app
  def test_home_url_resolves_home_view(self):
        view = resolve('/BusLuas/')
        self.assertEquals(view.view_name, 'BusLuas:index')


  #Testing string type models
  def test_string_representation(self):
        entry = BusLuas(TrainCode="A130", StationFullName="Dalkey", StationCode="BALNA", Origin="Ballina",Destination="Cork",Status="En Route",Lastlocation="Departed Raheny",Duein="4" )
        assert isinstance(entry.TrainCode, str)
        assert isinstance(entry.StationFullName,str)
        assert isinstance(entry.StationCode, str)
        assert isinstance(entry.Origin,str)
        assert isinstance(entry.Destination, str)
        assert isinstance(entry.Status,str)
        assert isinstance(entry.Lastlocation,str)
        assert isinstance(entry.Duein,str)
  
  #Testing datetime type models
  def test_datetime_representation(self):
        entry = BusLuas(Traindate = datetime.now(), Origintime = django.utils.timezone.now(), Destinationtime = django.utils.timezone.now(), Exparrival = django.utils.timezone.now() , Expdepart = django.utils.timezone.now())
        assert isinstance(entry.Traindate, datetime)
        assert isinstance(entry.Origintime, datetime)
        assert isinstance(entry.Destinationtime, datetime)
        assert isinstance(entry.Exparrival, datetime)
        assert isinstance(entry.Expdepart, datetime)
      
 