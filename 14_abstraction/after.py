from typing import Any
from os import environ
import requests
from typing import Protocol

API_KEY = str(environ.get("OPENWEATHER_API_KEY"))


class CityNotFoundError(Exception):
    pass


class HttpClient(Protocol):
    def get_response(self, url:  str) -> dict[str, Any]:
        ...


class RequestClient(HttpClient):
    def get_response(self, url:  str) -> dict[str, Any]:
        return requests.get(url, timeout=5).json()


class WeatherService:
    def __init__(self, api_key: str, response_client: HttpClient) -> None:
        self.api_key = api_key
        self.full_weather_forecast: dict[str, Any] = {}
        self.response_client: HttpClient = response_client

    def retrieve_forecast(self, city: str) -> None:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        response = self.response_client.get_response(url)
        if "main" not in response:
            raise CityNotFoundError(
                f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n"
            )
        self.full_weather_forecast = response

    @property
    def temperature(self) -> float:
        return self.full_weather_forecast["main"]["temp"] - 273.15

    @property
    def humidity(self) -> float:
        return self.full_weather_forecast["main"]["humidity"]

    @property
    def wind_speed(self) -> float:
        return self.full_weather_forecast["wind"]["speed"]

    @property
    def wind_direction(self) -> float:
        return self.full_weather_forecast["wind"]["deg"]


def main() -> None:
    city = "London"
    response_client = RequestClient()
    client = WeatherService(api_key=API_KEY, response_client=response_client)
    client.retrieve_forecast(city=city)

    print(f"The current temperature in {city} is {client.temperature:.1f} °C.")
    print(f"The current humidity in {city} is {client.humidity}%.")
    print(
        f"The current wind speed in {city} is {client.wind_speed} m/s from direction {client.wind_direction} degrees."
    )


if __name__ == "__main__":
    main()
