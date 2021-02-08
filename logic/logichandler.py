from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pyowm

from dataClass.forecastHandler import ForecastHandler
from dataClass.locationData import Location
from dataClass.weatherData import WeatherData


def executor(key, loc, unit):
    owm = pyowm.OWM(key)  # owm object
    config_dict = owm.configuration  # configuration needed to create other objects
    location = Location(
        loc
    )  # location object that returns latitude and longitude correctly formatted
    wm = pyowm.weatherapi25.weather_manager.WeatherManager(
        key, config_dict
    )  # object needed to get current weather in certain location

    cw = get_current_weather(wm, location, unit)
    meas = get_forecast(
        wm, location, unit, cw
    )  # appends forecast data to the current weather data

    temps = []
    hums = []
    curr = datetime.now().strftime("%m/%d,%H")
    times = [curr]
    c = 0
    print(
        f"\n\n----------------------------------------  WEATHER FORECAST ({loc})  ----------------------------------------\n"
    )
    for c, w in enumerate(meas):
        if c > 12:  # max 36 hours forecast
            break
        temps.append(w.get_temp()["temp"])
        hums.append(w.get_hum())
        temporary = ""
        if c == 0:
            temporary = curr
        if c != 0:
            temporary = (datetime.now() + timedelta(hours=3) * c).strftime(
                "%m/%d,%H"
            )  # 3 hour increment for each forecast, which is what OWM offers
            times.append(temporary)
        print(temporary + ":00 - " + w.get_status() + "\n")

    plot_creator(times, temps, hums, unit)


def plot_creator(times, temps, hums, unit):
    print("Check the plots for more in detail info.")
    plt.subplot(2, 1, 1)
    plt.plot(times, temps)
    plt.title("Temperature and humidity % in the next 36 hours")
    if unit == "celsius":
        plt.ylabel("Temperature " + "[°C]")
        plt.ylim([-5, 40])
    elif unit == "fahrenheit":
        plt.ylabel("Temperature " + "[°F]")
        plt.ylim([25, 104])
    plt.xlabel("Time")

    plt.subplot(2, 1, 2)
    plt.plot(times, hums)
    plt.ylabel("Humidity %")
    plt.xlabel("Time")
    plt.ylim([0, 100])

    plt.show()


def get_current_weather(wm, location, unit):
    meas = [
        WeatherData(location, wm, unit)
    ]  # array of measurements with the contenct of the construcotr for WeatherData
    return meas


def get_forecast(wm, location, unit, cw):
    handler = ForecastHandler(location, wm, unit)
    meas = handler.get_full_data(cw)
    return meas
