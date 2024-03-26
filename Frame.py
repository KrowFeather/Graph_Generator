import sys
from PySide6.QtWidgets import QWidget, QApplication
from generator_ui import Ui_Form
from Kernel.DirectedGraph import *
from Kernel.UndirectedGraph import *
from Kernel.trans_to_xlsw import *
from Kernel.GraphBuffer import *


class Frame(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Graph Generator")
        self.bind()
        self.node_num.setPlaceholderText('0')
        self.edge_num.setPlaceholderText('0')

    def bind(self):
        self.btn_generate.clicked.connect(lambda: self.generate())
        self.btn_addEdge.clicked.connect(lambda: self.addEdge())
        self.btn_delEdge.clicked.connect(lambda: self.delEdge())

    def generate(self):
        if self.node_num.text() is None:
            MAX_NODE_SIZES = 0
        else:
            MAX_EDGE_SIZES = int(self.edge_num.text())
        if self.edge_num.text() is None:
            MAX_EDGE_SIZES = 0
        else:
            MAX_NODE_SIZES = int(self.node_num.text())
        print(MAX_NODE_SIZES)
        print(MAX_EDGE_SIZES)
        pass

    def addEdge(self):
        edges.append()
        pass

    def delEdge(self):
        pass


def run():
    app = QApplication([])
    window = Frame()
    window.show()
    sys.exit(app.exec_())
