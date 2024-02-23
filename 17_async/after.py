from dataclasses import dataclass
from typing import Any
import requests
import json
from os.path import abspath, dirname, join
import asyncio


@dataclass
class UrlTemplateClient:
    template: str

    async def get(self, data: dict[str, Any]) -> Any:
        url = self.template.format(**data)
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an exception if the request failed
        return response.json()


class CityNotFoundError(Exception):
    pass


async def get_capital(country: str) -> str:
    client = UrlTemplateClient(template="https://restcountries.com/v3/name/{country}")
    response = await client.get({"country": country})

    # The API can return multiple matches, so we just return the capital of the first match
    return str(response[0]["capital"][0])


async def get_forecast(city: str, api_key: str) -> dict[str, Any]:
    client = UrlTemplateClient(
        template=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    )
    response = await client.get({"city": city})
    if "main" not in response:
        raise CityNotFoundError(
            f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n"
        )
    return response


async def get_temperature(full_weather_forecast: dict[str, Any]) -> float:
    temperature = full_weather_forecast["main"]["temp"]
    return temperature - 273.15  # convert from Kelvin to Celsius


def load_config(config_path: str) -> str:

    with open(config_path) as f:
        config = json.load(f)
    return str(config["api_key"])


async def get_capital_and_forecast(country: str, api_key: str) -> None:
    capital = await get_capital(country)
    print(f"The capital of {country} is {capital}")
    forecast = await get_forecast(capital, api_key)
    temperature = await get_temperature(forecast)
    print(f"The current temperature in {capital} is {temperature:.1f} °C.")
    return


async def main() -> None:
    countries = ["United States of America", "Australia", "Japan", "France", "Brazil"]
    config_path = join(dirname(abspath(__file__)), ".env")
    api_key = load_config(config_path)

    await asyncio.gather(*[get_capital_and_forecast(country, api_key) for country in countries])


if __name__ == "__main__":
    asyncio.run(main())
