from .weatherData import WeatherData


class ForecastData(WeatherData):
    def __init__(self, weather, unit):
        self._temp = weather.temperature(
            unit
        )  # dict cointaining temp, matxtemp, mintemp
        self._hum = weather.humidity
        self._pres = weather.pressure
        self._status = weather.status
