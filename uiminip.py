# Form implementation generated from reading ui file 'uiminip.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(431, 371)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.yes_btn = QtWidgets.QPushButton(parent=Form)
        self.yes_btn.setGeometry(QtCore.QRect(10, 80, 201, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yes_btn.sizePolicy().hasHeightForWidth())
        self.yes_btn.setSizePolicy(sizePolicy)
        self.yes_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.yes_btn.setMaximumSize(QtCore.QSize(16777215, 16634634))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.yes_btn.setFont(font)
        self.yes_btn.setObjectName("yes_btn")
        self.no_btn = QtWidgets.QPushButton(parent=Form)
        self.no_btn.setGeometry(QtCore.QRect(220, 80, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.no_btn.setFont(font)
        self.no_btn.setObjectName("no_btn")
        self.reset_btn = QtWidgets.QPushButton(parent=Form)
        self.reset_btn.setGeometry(QtCore.QRect(170, 220, 71, 31))
        self.reset_btn.setObjectName("reset_btn")
        self.no_lbl = QtWidgets.QLabel(parent=Form)
        self.no_lbl.setGeometry(QtCore.QRect(220, 140, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.no_lbl.setFont(font)
        self.no_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.no_lbl.setObjectName("no_lbl")
        self.yes_lbl = QtWidgets.QLabel(parent=Form)
        self.yes_lbl.setGeometry(QtCore.QRect(10, 140, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.yes_lbl.setFont(font)
        self.yes_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.yes_lbl.setObjectName("yes_lbl")
        self.safe_btn = QtWidgets.QPushButton(parent=Form)
        self.safe_btn.setGeometry(QtCore.QRect(90, 220, 71, 31))
        self.safe_btn.setObjectName("safe_btn")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 411, 21))
        self.label.setObjectName("label")
        self.q_line = QtWidgets.QLineEdit(parent=Form)
        self.q_line.setGeometry(QtCore.QRect(10, 20, 371, 21))
        self.q_line.setObjectName("q_line")
        self.q_lbl = QtWidgets.QLabel(parent=Form)
        self.q_lbl.setGeometry(QtCore.QRect(10, 50, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.q_lbl.setFont(font)
        self.q_lbl.setText("")
        self.q_lbl.setObjectName("q_lbl")
        self.yes_spin = QtWidgets.QSpinBox(parent=Form)
        self.yes_spin.setGeometry(QtCore.QRect(70, 190, 81, 21))
        self.yes_spin.setObjectName("yes_spin")
        self.no_spin = QtWidgets.QSpinBox(parent=Form)
        self.no_spin.setGeometry(QtCore.QRect(280, 190, 81, 21))
        self.no_spin.setObjectName("no_spin")
        self.apply_btn = QtWidgets.QPushButton(parent=Form)
        self.apply_btn.setGeometry(QtCore.QRect(170, 190, 91, 23))
        self.apply_btn.setObjectName("apply_btn")
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 260, 411, 101))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.ok_btn = QtWidgets.QPushButton(parent=Form)
        self.ok_btn.setGeometry(QtCore.QRect(390, 12, 31, 31))
        self.ok_btn.setObjectName("ok_btn")
        self.add_btn = QtWidgets.QPushButton(parent=Form)
        self.add_btn.setGeometry(QtCore.QRect(10, 220, 71, 31))
        self.add_btn.setObjectName("add_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.yes_btn.setText(_translate("Form", "За"))
        self.no_btn.setText(_translate("Form", "Против"))
        self.reset_btn.setText(_translate("Form", "Сброс"))
        self.no_lbl.setText(_translate("Form", "0"))
        self.yes_lbl.setText(_translate("Form", "0"))
        self.safe_btn.setText(_translate("Form", "Сохранить"))
        self.label.setText(_translate("Form", "Поле для ввода вопроса:"))
        self.apply_btn.setText(_translate("Form", "Применить"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Вопрос"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "За"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Против"))
        self.ok_btn.setText(_translate("Form", "Ок"))
        self.add_btn.setText(_translate("Form", "Добавить"))
