import sys

from PySide6.QtWidgets import QWidget, QApplication


class Frame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graph Generator")
        self.setFixedSize(800, 600)


def run():
    app = QApplication([])
    window = Frame()
    window.show()
    sys.exit(app.exec_())
