import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QApplication, QGraphicsScene, QTableWidgetItem
from generator_ui import Ui_Form
import Kernel.DirectedGraph as DAG
import Kernel.UndirectedGraph as UDG
from Kernel.trans_to_xlsw import *
import Kernel.GraphBuffer as GB
import Kernel.GraphUtils as Utils


class Frame(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Graph Generator")
        self.node_num.setPlaceholderText('0')
        self.edge_num.setPlaceholderText('0')
        self.edgelistframe.setColumnCount(3)
        self.edgelistframe.setColumnWidth(0, 88)
        self.edgelistframe.setColumnWidth(1, 87)
        self.edgelistframe.setColumnWidth(2, 87)
        self.tableIndex = 1
        self.bind()

    def bind(self):
        self.btn_generate.clicked.connect(lambda: self.generate())
        self.btn_addEdge.clicked.connect(lambda: self.addEdge())
        self.btn_delEdge.clicked.connect(lambda: self.delEdge())
        self.btn_confirm.clicked.connect(lambda: self.confirmGraph())

    def generate(self):
        print(GB.edges_buffer)
        DAG.Generate_DirectedGraph()
        UDG.Generate_UndirectedGraph()
        print(DAG.matrix)
        print(UDG.matrix)
        self.showPic()
        pass

    def confirmGraph(self):
        if self.node_num.text() == '':
            GB.MAX_NODE_SIZES = 0
        else:
            GB.MAX_NODE_SIZES = int(self.node_num.text())
        if self.edge_num.text() == '':
            GB.MAX_EDGE_SIZES = 0
        else:
            GB.MAX_EDGE_SIZES = int(self.edge_num.text())
        GB.edges_buffer = []
        print(f'nodes {GB.MAX_NODE_SIZES}')
        print(f'edges {GB.MAX_EDGE_SIZES}')

    def addEdge(self):
        e = Utils.random_edges()
        GB.edges_buffer.append(e)
        col1 = QTableWidgetItem(text=e[0])
        col2 = QTableWidgetItem(text=e[1])
        col3 = QTableWidgetItem(text=e[2])
        print(col1.text(),col2.text(),col3.text())
        self.edgelistframe.insertRow(int(self.edgelistframe.rowCount()))
        self.edgelistframe.setItem(self.tableIndex, 0, col1)
        self.edgelistframe.setItem(self.tableIndex, 1, col2)
        self.edgelistframe.setItem(self.tableIndex, 2, col3)
        self.edgelistframe.viewport().update()
        self.tableIndex += 1

    def delEdge(self):
        GB.edges_buffer.pop()

    def showPic(self):
        img = QPixmap(f"./images/UndirectedGraph/UDG_{UDG.timestamp}")
        scaled_pixmap = img.scaled(500, 380, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.view.setPixmap(scaled_pixmap)


def run():
    app = QApplication([])
    window = Frame()
    window.show()
    sys.exit(app.exec_())
