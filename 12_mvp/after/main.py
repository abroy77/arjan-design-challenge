from presenter import Presenter
from model import Model
from view import View


def main() -> None:
    model = Model()
    view = View()
    presenter = Presenter(model, view)
    presenter.view.start_ui(presenter)


if __name__ == "__main__":
    main()
