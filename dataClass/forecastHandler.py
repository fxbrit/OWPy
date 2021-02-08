from .forecastData import ForecastData


class ForecastHandler:

    _weathers = []

    def __init__(self, location, wm, unit):
        f = wm.forecast_at_coords(location.get_lat(), location.get_lon(), "3h").forecast
        for forecast in f.weathers:
            self._weathers.append(ForecastData(forecast, unit))

    def get_full_data(self, meas):
        for w in self._weathers:
            meas.append(w)
        return meas
