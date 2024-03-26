import sys
from PySide6.QtWidgets import QWidget, QApplication
from generator_ui import Ui_Form


class Frame(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Graph Generator")

    def bind(self):
        self.pushButton.clicked.connect(lambda: self.generate())

    def generate(self):
        pass


def run():
    app = QApplication([])
    window = Frame()
    window.show()
    sys.exit(app.exec_())
