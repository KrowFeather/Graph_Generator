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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 750)
        Form.setMinimumSize(QSize(800, 750))
        Form.setMaximumSize(QSize(14214, 135135))
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.view = QLabel(self.widget)
        self.view.setObjectName(u"view")
        self.view.setMinimumSize(QSize(500, 300))

        self.verticalLayout_2.addWidget(self.view)

        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.edgelistframe = QTableWidget(self.widget)
        self.edgelistframe.setObjectName(u"edgelistframe")
        self.edgelistframe.setMinimumSize(QSize(264, 0))
        self.edgelistframe.setMaximumSize(QSize(16777215, 16777215))
        self.edgelistframe.setBaseSize(QSize(264, 0))

        self.horizontalLayout_2.addWidget(self.edgelistframe)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.widget)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(200, 2))
        self.groupBox.setMaximumSize(QSize(200, 16777215))
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


        self.horizontalLayout_5.addWidget(self.groupBox)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_addEdge = QPushButton(Form)
        self.btn_addEdge.setObjectName(u"btn_addEdge")
        self.btn_addEdge.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.btn_addEdge)

        self.btn_delEdge = QPushButton(Form)
        self.btn_delEdge.setObjectName(u"btn_delEdge")
        self.btn_delEdge.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.btn_delEdge)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.btn_generate = QPushButton(Form)
        self.btn_generate.setObjectName(u"btn_generate")
        self.btn_generate.setMinimumSize(QSize(100, 0))
        self.btn_generate.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.btn_generate)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.node_num = QLineEdit(self.widget_2)
        self.node_num.setObjectName(u"node_num")

        self.verticalLayout_4.addWidget(self.node_num)

        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.edge_num = QLineEdit(self.widget_2)
        self.edge_num.setObjectName(u"edge_num")

        self.verticalLayout_4.addWidget(self.edge_num)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_confirm = QPushButton(self.widget_2)
        self.btn_confirm.setObjectName(u"btn_confirm")

        self.horizontalLayout_6.addWidget(self.btn_confirm)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_4.addWidget(self.widget_2)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.view.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Select Graph Type", None))
        self.btn_UDG.setText(QCoreApplication.translate("Form", u"Undirected Graph", None))
        self.btn_DAG.setText(QCoreApplication.translate("Form", u"Directed Graph", None))
        self.btn_addEdge.setText(QCoreApplication.translate("Form", u"Add Edge", None))
        self.btn_delEdge.setText(QCoreApplication.translate("Form", u"Delet Edge", None))
        self.btn_generate.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Node number", None))
        self.label.setText(QCoreApplication.translate("Form", u"Edge number", None))
        self.btn_confirm.setText(QCoreApplication.translate("Form", u"Confirm", None))
    # retranslateUi

