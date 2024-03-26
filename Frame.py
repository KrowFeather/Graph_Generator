import sys
from PySide6.QtWidgets import QWidget, QApplication
from generator_ui import Ui_Form
from Kernel.DirectedGraph import *
from Kernel.UndirectedGraph import *
from Kernel.trans_to_xlsw import *
import Kernel.GraphBuffer as GraphBuffer


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
        self.btn_confirm.clicked.connect(lambda: self.confirmGraph())

    def generate(self):

        pass

    def confirmGraph(self):
        if self.node_num.text() is '':
            GraphBuffer.MAX_NODE_SIZES = 0
        else:
            GraphBuffer.MAX_NODE_SIZES = int(self.edge_num.text())
        if self.edge_num.text() is '':
            GraphBuffer.MAX_EDGE_SIZES = 0
        else:
            GraphBuffer.MAX_EDGE_SIZES = int(self.node_num.text())
        GraphBuffer.edges_buffer = []
        print(GraphBuffer.MAX_EDGE_SIZES)
        print(GraphBuffer.MAX_NODE_SIZES)

    def addEdge(self):
        e = GraphBuffer.random_edges()
        GraphBuffer.edges_buffer.append(e)
        pass

    def delEdge(self):
        pass


def run():
    app = QApplication([])
    window = Frame()
    window.show()
    sys.exit(app.exec_())
