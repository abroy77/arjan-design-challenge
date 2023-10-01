from typing import Any, Callable, Dict
import requests
from os import environ
from functools import partial

API_KEY = str(environ.get("OPENWEATHER_API_KEY"))
ForecastObject = Dict[str, Any]


class CityNotFoundError(Exception):
    pass


def get_api_call(url: str) -> ForecastObject:
    response = requests.get(url, timeout=5)
    return response.json()


def get_forecast(
        get_function: Callable[[str], ForecastObject],
        city: str,
        api_key: str) -> ForecastObject:
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    return get_function(url)


get_forecast_city = partial(get_forecast, get_function=get_api_call, api_key=API_KEY)


def get_temperature(forecast: ForecastObject) -> float:
    temperature = forecast['main']['temp']
    return temperature - 273.15  # convert from Kelvin to Celsius


def get_humidity(forecast: ForecastObject) -> int:
    return forecast['main']['humidity']


def get_wind_speed(forecast: ForecastObject) -> float:
    return forecast['wind']['speed']


def get_wind_direction(forecast: ForecastObject) -> int:
    return forecast['wind']['deg']


def main() -> None:
    city = "Utrecht"

    forecast = get_forecast_city(city=city)
    temperature = get_temperature(forecast)
    humidity = get_humidity(forecast)
    wind_speed = get_wind_speed(forecast)
    wind_direction = get_wind_direction(forecast)

    print(f"The current temperature in {city} is {temperature:.1f} °C.")
    print(f"The current humidity in {city} is {humidity}%.")
    print(
        f"The current wind speed in {city} is {wind_speed} m/s from direction {wind_direction} degrees."
    )


if __name__ == "__main__":
    main()
