import argparse
from weather import (
    get_complete_forecast,
    http_get,
    get_temperature,
    get_humidity,
    get_wind_speed,
    get_wind_direction,
)
from enum import Enum


class Condition(Enum):
    ALL = "all"
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    WIND = "wind"


OPTION_TO_CONDITION = {
    "all": Condition.ALL,
    "a": Condition.ALL,
    "temperature": Condition.TEMPERATURE,
    "t": Condition.TEMPERATURE,
    "humidity": Condition.HUMIDITY,
    "h": Condition.HUMIDITY,
    "wind": Condition.WIND,
    "w": Condition.WIND,
}

CONDITION_TO_FUNCTION = {
    Condition.TEMPERATURE: get_temperature,
    Condition.HUMIDITY: get_humidity,
    Condition.WIND: get_wind_speed,
}


def parse_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        description="Get the current weather information for a city"
    )
    parser.add_argument(
        "city", help="Name of the city to get the weather information for"
    )
    parser.add_argument(
        "-c",
        "--conditions",
        dest="conditions",
        metavar="CONDITION",
        nargs="+",
        default=["temperature"],
        choices=OPTION_TO_CONDITION.keys(),
        help=f"Weather conditions to display. Choose between {OPTION_TO_CONDITION.keys()}.",
    )

    parser.add_argument(
        "--api-key",
        default="123456789",
        help="API key for the OpenWeatherMap API",
    )

    args = parser.parse_args()

    if not args.api_key:
        # That will not happen because of the API default value.
        raise ValueError("Please provide an API key with the --api-key option.")

    return args


def main() -> None:
    args = parse_args()

    if not args.conditions:
        #  This will never happen because temperature is set as the default condition.
        raise ValueError(
            "Please specify at least one weather condition to display with the --conditions option."
        )
    # Fetch the data from the OpenMapWeather API
    weather_forecast = get_complete_forecast(
        http_get_fn=http_get, api_key=args.api_key, city=args.city
    )

    conditions = set([OPTION_TO_CONDITION[option] for option in args.conditions])

    if Condition.ALL in conditions or Condition.TEMPERATURE in conditions:
        temperature = get_temperature(weather_forecast)
        print(
            f"The current temperature in {args.city} is {temperature:.1f} °C."
        )
    if Condition.ALL in conditions or Condition.HUMIDITY in conditions:
        print(
            f"The current humidity in {args.city} is {get_humidity(weather_forecast)}%."
        )
    if Condition.ALL in conditions or Condition.WIND in conditions:
        print(
            f"The current wind speed in {args.city} is {get_wind_speed(weather_forecast)} m/s "
            f"from direction {get_wind_direction(weather_forecast)} degrees."
        )


if __name__ == "__main__":
    main()
