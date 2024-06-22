from PyQt5.QtWidgets import (
    QApplication,
)
import sys

from zodiaq.gui.windows import MainWindow


def run_gui():
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_gui()
