import pandas as pd
from pathlib import Path
from enum import Enum
from copy import deepcopy


class SensorType(Enum):
    ALL = "All"
    TEMPERATURE = "Temperature"
    HUMIDITY = "Humidity"
    CO2 = "CO2"

    @staticmethod
    def list() -> list[str]:
        return [sensor.value for sensor in SensorType]


class Model:
    df: pd.DataFrame
    processed_df: pd.DataFrame

    def load_csv(self, csv_path: Path) -> None:
        self.df = pd.read_csv(csv_path)
        return

    def get_df(self) -> pd.DataFrame:
        return self.df

    def get_processed_df(self) -> pd.DataFrame:
        return self.processed_df

    @staticmethod
    def celsius_to_kelvin(temperature: float) -> float:
        return temperature + 273.15

    @staticmethod
    def normalize_humidity(value: float) -> float:
        return value / 100

    @staticmethod
    def adjust_co2_bias(value: float, bias: float = 23) -> float:
        return value + bias

    PROCESS_FUNCS = {
        SensorType.TEMPERATURE: celsius_to_kelvin,
        SensorType.HUMIDITY: normalize_humidity,
        SensorType.CO2: adjust_co2_bias,
    }

    @staticmethod
    def filter_df(df: pd.DataFrame, sensor: SensorType) -> pd.DataFrame:
        if sensor is SensorType.ALL:
            return df
        return df.loc[df["Sensor"] == sensor.value]

    def process_df(self, sensor: SensorType) -> None:
        df = deepcopy(self.df)
        sensor_df = self.filter_df(df, sensor)
        unique_sensors = sensor_df["Sensor"].unique()
        for unique_sensor in unique_sensors:
            sensor_df_mask = sensor_df["Sensor"] == unique_sensor
            process_func = self.PROCESS_FUNCS[SensorType(unique_sensor)]
            sensor_df.loc[sensor_df_mask, "Value"] = sensor_df.loc[sensor_df_mask, "Value"].apply(process_func)

        self.processed_df = sensor_df
        return

    def save_processed_df(self, csv_path: Path) -> None:
        self.processed_df.to_csv(csv_path, index=False)
        return
