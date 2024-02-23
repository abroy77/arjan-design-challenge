import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from typing import Protocol


class PresenterProtocol(Protocol):

    def load_csv(self) -> None:
        ...

    def show_raw_data(self) -> None:
        ...

    def process_data(self) -> None:
        ...

    def export_data(self) -> None:
        ...

    sensor_types: list[str]


class View(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Data Processing GUI")

    def start_ui(self, presenter: PresenterProtocol) -> None:

        load_button = tk.Button(self, text="Load CSV", command=presenter.load_csv)

        show_raw_data_button = tk.Button(
            self, text="Show raw data", command=presenter.show_raw_data)

        process_data_button = tk.Button(
            self, text="Process data", command=presenter.process_data)

        export_data_button = tk.Button(
            self, text="Export data", command=presenter.export_data)

        self.selected_option = tk.StringVar(self)
        self.selected_option.set(presenter.sensor_types[0])

        option_menu = tk.OptionMenu(self, self.selected_option, *presenter.sensor_types)

        self.text_widget = tk.Text(self)

        # arrange
        self.text_widget.grid(row=0, column=0, columnspan=2)
        load_button.grid(row=1, column=0)
        show_raw_data_button.grid(row=1, column=1)
        option_menu.grid(row=2, column=0)
        process_data_button.grid(row=2, column=1)
        export_data_button.grid(row=3, column=0)

        self.mainloop()
