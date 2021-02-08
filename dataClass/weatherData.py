class WeatherData:

    _temp = 0
    _hum = 0
    _pres = 0
    _status = ""

    def __init__(self, location, wm, unit):
        weather = wm.weather_at_coords(location.get_lat(), location.get_lon()).weather
        self._temp = weather.temperature(
            unit
        )  # dict cointaining temp, matxtemp, mintemp
        self._hum = weather.humidity
        self._pres = weather.pressure
        self._status = weather.status

    def get_temp(self):
        return self._temp

    def get_hum(self):
        return self._hum

    def get_pres(self):
        return self._pres

    def get_status(self):
        return self._status

