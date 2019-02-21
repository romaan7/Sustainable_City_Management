from django.urls import reverse, resolve


class TestUrls:

    def test_cityevent_url(self):
        path=reverse('CityEventData')
        assert resolve(path).view_name=='CityEventData'
 