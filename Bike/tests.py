
from django.test import TestCase
from Bike.models import Bike

class BikeTestCase(TestCase):
    def setUp(self):
        Bike.objects.create(name="lion", sound="roar")
        Bike.objects.create(name="cat", sound="meow")

    def test_Bike(self):
        contract_name = Bike.objects.get(contract_name="Dublin")
        self.assertEqual(contract_name.name(), 'The lion says "roar"')
