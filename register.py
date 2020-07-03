# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 437)
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
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.user_name = QtWidgets.QLineEdit(Dialog)
        self.user_name.setObjectName("user_name")
        self.verticalLayout.addWidget(self.user_name)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.password_2 = QtWidgets.QLineEdit(Dialog)
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_2.setObjectName("password_2")
        self.verticalLayout.addWidget(self.password_2)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.tel = QtWidgets.QLineEdit(Dialog)
        self.tel.setMaxLength(11)
        self.tel.setObjectName("tel")
        self.verticalLayout.addWidget(self.tel)
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setStyleSheet("font: 9pt \"宋体\";\n"
"")
        self.cancel.setObjectName("cancel")
        self.verticalLayout.addWidget(self.cancel)
        self.register_2 = QtWidgets.QPushButton(Dialog)
        self.register_2.setObjectName("register_2")
        self.verticalLayout.addWidget(self.register_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.register_2.clicked.connect(self.register_check)
        self.cancel.clicked.connect(self.window_close)
        self.user_name.returnPressed.connect(self.register_check)
        self.password.returnPressed.connect(self.register_check)
        self.tel.returnPressed.connect(self.register_check)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "用户注册"))
        self.label_2.setText(_translate("Dialog", "用户名"))
        self.user_name.setPlaceholderText(_translate("Dialog", "请输入用户名"))
        self.label_3.setText(_translate("Dialog", "密码"))
        self.password.setPlaceholderText(_translate("Dialog", "请输入登录密码"))
        self.label_4.setText(_translate("Dialog", "密码（请再输入一次）"))
        self.password_2.setPlaceholderText(_translate("Dialog", "请再输入一次"))
        self.label_5.setText(_translate("Dialog", "联系方式"))
        self.tel.setPlaceholderText(_translate("Dialog", "请输入联系方式（长度小于等于11）"))
        self.cancel.setText(_translate("Dialog", "取消"))
        self.register_2.setText(_translate("Dialog", "注册"))

# 实例化注册窗体
    def instantiation(self):
        register_dialog = QDialog()
        child1_ui = Ui_Dialog()
        child1_ui.setupUi(register_dialog)
        return register_dialog, child1_ui


    # connect button
    def button_connect(self, child_register, button):
        # first instantiation ,next the name of button
        btn1 = button
        btn1.clicked.connect(child_register.show)


    def register_check(self):
        user_name = self.user_name.text()
        password = self.password.text()
        password_2 = self.password_2.text()
        tel = self.tel.text()
        if (user_name == "" or password == "" or tel == ""):
            QMessageBox.warning(self, "警告", "用户名,密码及联系方式不可为空!", QMessageBox.Ok)
            return
        elif (password != password_2):
            QMessageBox.warning(self, "警告","两次输入密码不一致!", QMessageBox.Ok)
            return
        # 进行数据库操作
        query = QSqlQuery()  # 新建sql对象
        query.prepare('INSERT INTO 用户表(用户名,用户密码,用户权限,用户联系方式)'
                      'VALUES(:user_name,:password,0,:tel)')  # 输入SQL语句
        query.bindValue(":user_name", user_name)
        query.bindValue(":password", password)
        query.bindValue(":tel", tel)
        # 绑定占位符和相应的功能

        value = query.exec_()
        if (value):
            QMessageBox.information(self, "提示", "注册成功!", QMessageBox.Ok)
            self.close()
        else:
            QMessageBox.information(self, "提示", "注册失败！（已存在相同的用户名）", QMessageBox.Ok)

        return

    def window_close(self):
        self.close()