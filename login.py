# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(1000, 1000)
        Dialog.setMinimumSize(QtCore.QSize(1000, 1000))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(800, 200))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.user_name = QtWidgets.QLineEdit(Dialog)
        self.user_name.setObjectName("user_name")
        self.verticalLayout.addWidget(self.user_name)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.designer = QtWidgets.QRadioButton(Dialog)
        self.designer.setObjectName("designer")
        self.verticalLayout.addWidget(self.designer)
        self.administrator = QtWidgets.QRadioButton(Dialog)
        self.administrator.setObjectName("administrator")
        self.verticalLayout.addWidget(self.administrator)
        self.user = QtWidgets.QRadioButton(Dialog)
        self.user.setObjectName("user")
        self.verticalLayout.addWidget(self.user)
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setObjectName("cancel")
        self.verticalLayout.addWidget(self.cancel)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "机票订购系统登录"))
        self.label_2.setText(_translate("Dialog", "用户名"))
        self.label_3.setText(_translate("Dialog", "密码"))
        self.designer.setText(_translate("Dialog", "设计人员"))
        self.administrator.setText(_translate("Dialog", "机场管理员"))
        self.user.setText(_translate("Dialog", "用户"))
        self.login.setText(_translate("Dialog", "登录"))
        self.cancel.setText(_translate("Dialog", "取消"))

    def instantiation(self):
        login_dialog = QDialog()
        child_ui = Ui_Dialog()
        child_ui.setupUi(login_dialog)
        return login_dialog,child_ui

    def button_connect(self, child_login, button):
        # first instantiation ,next the name of button
        btn1 = button
        btn1.clicked.connect(child_login.show)