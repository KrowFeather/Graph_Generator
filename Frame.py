import sys

from PySide6.QtWidgets import QWidget, QApplication
from generator_ui import Ui_Form


class Frame(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(Ui_Form)
        self.setWindowTitle("Graph Generator")
        self.setFixedSize(600, 400)


def run():
    app = QApplication([])
    window = Frame()
    window.show()
    sys.exit(app.exec_())
