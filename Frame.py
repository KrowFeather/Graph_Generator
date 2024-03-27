import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QApplication, QGraphicsScene, QTableWidgetItem
from generator_ui import Ui_Form
import Kernel.DirectedGraph as DAG
import Kernel.UndirectedGraph as UDG
import Kernel.trans_to_xlsx as xlsx_writer
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
        self.tableIndex = 0
        self.bind()

    def bind(self):
        self.btn_generate.clicked.connect(lambda: self.generate())
        self.btn_addEdge.clicked.connect(lambda: self.addEdge())
        self.btn_delEdge.clicked.connect(lambda: self.delEdge())
        self.btn_confirm.clicked.connect(lambda: self.confirmGraph())

    def generate(self):
        DAG.Generate_DirectedGraph()
        UDG.Generate_UndirectedGraph()
        # waiting delete
        print(GB.edges_buffer)
        print(DAG.matrix)
        print(UDG.matrix)
        # end
        self.showPic()
        self.showMatrixTable()
        xlsx_writer.xw_to_excel(UDG.matrix, f'./xlsx/xls_{UDG.timestamp}.xlsx')

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

    def addEdge(self):
        e = Utils.random_edges()
        GB.edges_buffer.append(e)
        col1 = QTableWidgetItem(str(e[0]))
        col2 = QTableWidgetItem(str(e[1]))
        col3 = QTableWidgetItem(str(e[2]))
        self.edgelistframe.insertRow(int(self.edgelistframe.rowCount()))
        self.edgelistframe.setItem(self.tableIndex, 0, col1)
        self.edgelistframe.setItem(self.tableIndex, 1, col2)
        self.edgelistframe.setItem(self.tableIndex, 2, col3)
        self.tableIndex += 1

    def delEdge(self):
        if not GB.edges_buffer:
            return
        self.edgelistframe.removeRow(self.tableIndex - 1)
        self.tableIndex -= 1
        GB.edges_buffer.pop()

    def showPic(self):
        img = QPixmap(f"./images/UndirectedGraph/UDG_{UDG.timestamp}")
        scaled_pixmap = img.scaled(500, 380, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.view.setPixmap(scaled_pixmap)

    def showMatrixTable(self):
        self.matrixTable.setRowCount(GB.MAX_NODE_SIZES)
        self.matrixTable.setColumnCount(GB.MAX_NODE_SIZES)
        for pack in GB.edges_buffer:
            self.matrixTable.setItem(pack[0] - 1, pack[1] - 1, QTableWidgetItem(str(pack[2])))


def run():
    app = QApplication([])
    window = Frame()
    window.show()
    sys.exit(app.exec_())
