# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generator_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 600)
        Form.setMinimumSize(QSize(700, 600))
        Form.setMaximumSize(QSize(700, 600))
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 470, 251, 131))
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_UDG = QRadioButton(self.groupBox)
        self.btn_UDG.setObjectName(u"btn_UDG")

        self.verticalLayout.addWidget(self.btn_UDG)

        self.btn_DAG = QRadioButton(self.groupBox)
        self.btn_DAG.setObjectName(u"btn_DAG")

        self.verticalLayout.addWidget(self.btn_DAG)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 701, 471))
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graphicsView = QGraphicsView(self.widget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout_2.addWidget(self.graphicsView)

        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.edgelistframe = QTableWidget(self.widget)
        self.edgelistframe.setObjectName(u"edgelistframe")
        self.edgelistframe.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_2.addWidget(self.edgelistframe)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(290, 480, 401, 121))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_addEdge = QPushButton(self.layoutWidget)
        self.btn_addEdge.setObjectName(u"btn_addEdge")

        self.verticalLayout_3.addWidget(self.btn_addEdge)

        self.btn_delEdge = QPushButton(self.layoutWidget)
        self.btn_delEdge.setObjectName(u"btn_delEdge")

        self.verticalLayout_3.addWidget(self.btn_delEdge)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.btn_generate = QPushButton(self.layoutWidget)
        self.btn_generate.setObjectName(u"btn_generate")

        self.horizontalLayout_4.addWidget(self.btn_generate)

        self.widget_2 = QWidget(self.layoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget1 = QWidget(self.widget_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 10, 134, 92))
        self.verticalLayout_4 = QVBoxLayout(self.widget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.node_num = QLineEdit(self.widget1)
        self.node_num.setObjectName(u"node_num")

        self.verticalLayout_4.addWidget(self.node_num)

        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.edge_num = QLineEdit(self.widget1)
        self.edge_num.setObjectName(u"edge_num")

        self.verticalLayout_4.addWidget(self.edge_num)


        self.horizontalLayout_4.addWidget(self.widget_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Select Graph Type", None))
        self.btn_UDG.setText(QCoreApplication.translate("Form", u"Undirected Graph", None))
        self.btn_DAG.setText(QCoreApplication.translate("Form", u"Directed Graph", None))
        self.btn_addEdge.setText(QCoreApplication.translate("Form", u"Add Edge", None))
        self.btn_delEdge.setText(QCoreApplication.translate("Form", u"Delet Edge", None))
        self.btn_generate.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Node number", None))
        self.label.setText(QCoreApplication.translate("Form", u"Edge number", None))
    # retranslateUi

