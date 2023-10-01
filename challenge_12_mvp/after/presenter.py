from __future__ import annotations
from model import SensorType
from typing import Protocol
import pandas as pd
from pathlib import Path
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb


class ModelProtocol(Protocol):

    def load_csv(self, csv_path: Path) -> None:
        ...

    def get_df(self) -> pd.DataFrame:
        ...

    def get_processed_df(self) -> pd.DataFrame:
        ...

    def process_df(self, sensor: SensorType) -> None:
        ...

    def save_processed_df(self, csv_path: Path) -> None:
        ...


class ViewProtocol(Protocol):
    def start_ui(self, presenter: Presenter) -> None:
        ...

    def mainloop(self) -> None:
        ...
    text_widget: tk.Text
    selected_option: tk.StringVar


class Presenter:
    model: ModelProtocol
    view: ViewProtocol
    sensor_types: list[str] = SensorType.list()

    def __init__(self, model: ModelProtocol, view: ViewProtocol) -> None:
        self.view = view
        self.model = model

    def load_csv(self) -> None:
        file_path = fd.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        self.model.load_csv(Path(file_path))
        mb.showinfo("Import", "Data successfully loaded!")

    def show_raw_data(self) -> None:
        self.view.text_widget.delete(1.0, tk.END)
        try:
            self.view.text_widget.insert(tk.END, str(self.model.get_df()))
        except NameError:
            mb.showinfo("Error", "No data to show!")

    def process_data(self) -> None:

        sensor = SensorType(self.view.selected_option.get())
        self.model.process_df(sensor)
        self.view.text_widget.delete(1.0, tk.END)
        self.view.text_widget.insert(tk.END, str(self.model.get_processed_df()))

    def export_data(self) -> None:
        file_path = fd.asksaveasfile(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
        )
        if file_path is not None:
            self.model.save_processed_df(Path(str(file_path)))
            mb.showinfo("Export", "Data exported successfully!")

    def run(self) -> None:
        self.view.start_ui(self)
        self.view.mainloop()
