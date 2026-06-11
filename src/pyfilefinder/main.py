import logging
import sys
from datetime import datetime

from pyfilefinder.logging_config import config_logging

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

from pyfilefinder.views.file_tree import FileTree


def main() -> int:
    config_logging()
    log = logging.getLogger(__name__)
    log.info(
        f"pyfilefinder started at {datetime.now().strftime("%I:%M:%S %p on %B %d, %Y")}"
    )

    app = QApplication(sys.argv)
    app.setApplicationName("PyFileFinder")
    app.setApplicationVersion("0.1.0")

    main_window = QMainWindow()

    central_widget_layout = QVBoxLayout()
    central_widget_layout.addWidget(FileTree())

    central_widget = QWidget()
    central_widget.setLayout(central_widget_layout)

    main_window.setCentralWidget(central_widget)

    main_window.show()

    exit_code = app.exec()

    return exit_code


if __name__ == "__main__":
    main()
