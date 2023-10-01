from os import environ
import requests


class CityNotFoundError(Exception):
    pass


class WeatherService:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get_forecast(self, city: str) -> None:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        response = requests.get(url, timeout=5).json()
        if "main" not in response:
            raise CityNotFoundError(
                f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n"
            )

        self.full_weather_forecast = response

    @property
    def temperature(self) -> float:
        temp = self.full_weather_forecast["main"]["temp"] - 273.15
        return temp


def main():
    city = "New Delhi"
    OPENWEATHER_API_KEY = str(environ.get("OPENWEATHER_API_KEY"))
    weather_service = WeatherService(api_key=OPENWEATHER_API_KEY)
    weather_service.get_forecast(city)
    # weather_service.print_temp(city)
    temp = weather_service.temperature
    print(f"The current temperature in {city} is {temp:.1f} °C.")


if __name__ == "__main__":
    main()
