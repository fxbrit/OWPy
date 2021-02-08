from geopy.geocoders import Nominatim


class Location:
    _lat = 0
    _lon = 0

    def __init__(self, loc):
        locator = Nominatim(user_agent="owp")
        location = locator.geocode(loc)
        lat = float("%.1f" % (location.latitude))
        lon = float("%.1f" % (location.longitude))
        self._lat = lat
        self._lon = lon

    def get_lat(self):
        return self._lat

    def get_lon(self):
        return self._lon
