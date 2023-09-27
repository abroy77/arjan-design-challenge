import pandas as pd
from pathlib import Path


def load_csv(csv_path: Path) -> pd.DataFrame:
    return pd.read_csv(csv_path)  # type: ignore


def celsius_to_kelvin(temperature: float) -> float:
    return temperature + 273.15


def normalize_humidity(humidity: float) -> float:
    return humidity / 100


def adjust_co2_bias(co2: float) -> float:
    return co2 + 23


def filter_sensor(df: pd.DataFrame, sensor: str) -> pd.DataFrame:
    if sensor == "All":
        return df
    else:
        return df.loc[df["Sensor"] == sensor]


PROCESS_FUNCS = {
    'Temperature': celsius_to_kelvin,
    'Humidity': normalize_humidity,
    'CO2': adjust_co2_bias,
}


def process_data(df: pd.DataFrame) -> pd.DataFrame:
    sensors_in_data = df["Sensor"].unique()  # type: ignore

    for sensor in sensors_in_data:
        sensor_row_masks = df["Sensor"] == sensor
        process_func = PROCESS_FUNCS[sensor]
        df.loc[sensor_row_masks, "Value"] = df.loc[sensor_row_masks, "Value"].apply(process_func)  # type: ignore
    return df


def main():
    option = input("pick an option from:\n"
                   "All, Temperature, Humidity,CO2\n")  # choose between "All", "Temperature", "Humidity", "CO2"
    assert option in (
        "All",
        "Temperature",
        "Humidity",
        "CO2",
    ), f'Option not valid, should be ("All", "Temperature", "Humidity", "CO2") {option} given!'

    data = load_csv("sensor_data.csv")  # type: ignore
    data = filter_sensor(data, option)
    processed_data = process_data(data)
    print(processed_data)


if __name__ == "__main__":
    main()
