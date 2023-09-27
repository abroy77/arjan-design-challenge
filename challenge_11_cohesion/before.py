import pandas as pd


def main() -> None:
    option = "All"  # choose between "All", "Temperature", "Humidity", "CO2"

    data = pd.read_csv("sensor_data.csv")  # type: ignore
    assert option in (
        "All",
        "Temperature",
        "Humidity",
        "CO2",
    ), f'Option not valid, should be ("All", "Temperature", "Humidity", "CO2") {option} given!'

    if option in ("Temperature", "Humidity", "CO2"):  # type: ignore
        data = data.loc[data["Sensor"] == option]

    processed_data = []
    for _, row in data.iterrows():  # type: ignore
        sensor = row["Sensor"]  # type: ignore
        if sensor == "Temperature":
            row["Value"] += 273.15  # type: ignore ,Convert to Kelvin t
            processed_data.append(row)  # type: ignore
        elif sensor == "Humidity":
            row["Value"] /= 100  # type: ignore ,Convert to scale 0-1
            processed_data.append(row)  # type: ignore
        elif sensor == "CO2":
            row["Value"] += 23  # type: ignore ,Compensating for sensor bias
            processed_data.append(row)  # type: ignore

    processed_data_single: pd.DataFrame = pd.DataFrame(data=processed_data)
    print(processed_data_single)


if __name__ == "__main__":
    main()
