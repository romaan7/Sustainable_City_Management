# test_models.py
import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db
from CityEvents.models import CityEvents

class TestCityEvents:

    #Initializing
    def test_init(self):
        print('test')
        obj = mixer.blend('CityEvents.CityEvents')
        assert obj.pk == 1, 'Should save an instance'

    #Positive
    def test_data_extraction_postive(self):
        entry = CityEvents(nametext="Love Your Home, Dublin 2019")
        print(entry)
        assert entry.nametext=="Love Your Home, Dublin 2019",'There is issue in the data extraction!!'
        # self.assertEqual(str(entry), entry.nametext)


    # def test_homepage(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)

    
    # def test_get_excerpt(self):
    #     obj = mixer.blend('CityEvents.CityEvents', body='Hello World!')
    #     result = obj.get_excerpt(5)
    #     expected = 'Hello'
    #     assert result == expected, (
    #     'Should return the given number of characters') 