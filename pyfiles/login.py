# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    power = 0 #权限
    username = '' #用户名
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(410, 398)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icon/flight.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("\n"
                             "/**********主界面样式**********/\n"
                             "QWidget#Dialog {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: rgb(232, 241, 252);\n"
                             "}\n"
                             "\n"
                             "QWidget#messageWidget {\n"
                             "        background: rgba(173, 202, 232, 50%);\n"
                             "}\n"
                             "\n"
                             "QWidget#loadingWidget {\n"
                             "        border: none;\n"
                             "        border-radius: 5px;\n"
                             "        background: rgb(187, 212, 238);\n"
                             "}\n"
                             "\n"
                             "StyledWidget {\n"
                             "        qproperty-normalColor: rgb(65, 65, 65);\n"
                             "        qproperty-disableColor: rgb(180, 180, 180);\n"
                             "        qproperty-highlightColor: rgb(0, 160, 230);\n"
                             "        qproperty-errorColor: red;\n"
                             "}\n"
                             "\n"
                             "QProgressIndicator {\n"
                             "        qproperty-color: rgb(2, 65, 132);\n"
                             "}\n"
                             "\n"
                             "/**********表头**********/\n"
                             "QHeaderView{\n"
                             "        border: none;\n"
                             "        border-bottom: 3px solid rgb(0, 78, 161);\n"
                             "        background: transparent;\n"
                             "        min-height: 30px;\n"
                             "}\n"
                             "QHeaderView::section:horizontal {\n"
                             "        border: none;\n"
                             "        color: rgb(2, 65, 132);\n"
                             "        background: transparent;\n"
                             "        padding-left: 5px;\n"
                             "}\n"
                             "QHeaderView::section:horizontal:hover {\n"
                             "        color: white;\n"
                             "        background: rgb(0, 78, 161);\n"
                             "}\n"
                             "QHeaderView::section:horizontal:pressed {\n"
                             "        color: white;\n"
                             "        background: rgb(6, 94, 187);\n"
                             "}\n"
                             "QHeaderView::up-arrow {\n"
                             "        width: 13px;\n"
                             "        height: 11px;\n"
                             "        padding-right: 5px;\n"
                             "        image: url(:/White/topArrow);\n"
                             "        subcontrol-position: center right;\n"
                             "}\n"
                             "QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
                             "        image: url(:/White/topArrowHover);\n"
                             "}\n"
                             "QHeaderView::down-arrow {\n"
                             "        width: 13px;\n"
                             "        height: 11px;\n"
                             "        padding-right: 5px;\n"
                             "        image: url(:/White/bottomArrow);\n"
                             "        subcontrol-position: center right;\n"
                             "}\n"
                             "QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
                             "        image: url(:/White/bottomArrowHover);\n"
                             "}\n"
                             "\n"
                             "/**********表格**********/\n"
                             "QTableView {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: rgb(224, 238, 255);\n"
                             "        gridline-color: rgb(111, 156, 207);\n"
                             "}\n"
                             "QTableView::item {\n"
                             "        padding-left: 5px;\n"
                             "        padding-right: 5px;\n"
                             "        border: none;\n"
                             "        background: white;\n"
                             "        border-right: 1px solid rgb(111, 156, 207);\n"
                             "        border-bottom: 1px solid rgb(111, 156, 207);\n"
                             "}\n"
                             "QTableView::item:selected {\n"
                             "        background: rgba(255, 255, 255, 100);\n"
                             "}\n"
                             "QTableView::item:selected:!active {\n"
                             "        color: rgb(65, 65, 65);\n"
                             "}\n"
                             "QTableView::indicator {\n"
                             "        width: 20px;\n"
                             "        height: 20px;\n"
                             "}\n"
                             "\n"
                             "/**********状态栏**********/\n"
                             "QStatusBar {\n"
                             "        background: rgb(187, 212, 238);\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        border-left: none;\n"
                             "        border-right: none;\n"
                             "        border-bottom: none;\n"
                             "}\n"
                             "QStatusBar::item {\n"
                             "    border: none;\n"
                             "    border-right: 1px solid rgb(111, 156, 207);\n"
                             "}\n"
                             "\n"
                             "/**********分组框**********/\n"
                             "QGroupBox {\n"
                             "        font-size: 15px;\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        border-radius: 4px;\n"
                             "        margin-top: 10px;\n"
                             "}\n"
                             "QGroupBox::title {\n"
                             "        color: rgb(56, 99, 154);\n"
                             "        top: -12px;\n"
                             "        left: 10px;\n"
                             "}\n"
                             "\n"
                             "\n"
                             "\n"
                             "/**********单选框**********/\n"
                             "QRadioButton{\n"
                             "        spacing: 5px;\n"
                             "}\n"
                             "QRadioButton:enabled:checked{\n"
                             "        color: rgb(2, 65, 132);\n"
                             "}\n"
                             "QRadioButton:enabled:!checked{\n"
                             "        color: rgb(70, 71, 73);\n"
                             "}\n"
                             "QRadioButton:enabled:hover{\n"
                             "        color: rgb(0, 78, 161);\n"
                             "}\n"
                             "QRadioButton:!enabled{\n"
                             "        color: rgb(80, 80, 80);\n"
                             "}\n"
                             "QRadioButton::indicator {\n"
                             "        width: 20px;\n"
                             "        height: 20px;\n"
                             "}\n"
                             "/**********输入框**********/\n"
                             "QLineEdit {\n"
                             "        border-radius: 4px;\n"
                             "        height: 25px;\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: white;\n"
                             "}\n"
                             "QLineEdit:enabled {\n"
                             "        color: rgb(84, 84, 84);\n"
                             "}\n"
                             "QLineEdit:enabled:hover, QLineEdit:enabled:focus {\n"
                             "        color: rgb(51, 51, 51);\n"
                             "}\n"
                             "QLineEdit:!enabled {\n"
                             "        color: rgb(80, 80, 80);\n"
                             "}\n"
                             "\n"
                             "/**********文本编辑框**********/\n"
                             "QTextEdit {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        color: rgb(70, 71, 73);\n"
                             "        background: rgb(187, 212, 238);\n"
                             "}\n"
                             "\n"
                             "/**********滚动区域**********/\n"
                             "QScrollArea {\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: rgb(187, 212, 238);\n"
                             "}\n"
                             "\n"
                             "/**********滚动区域**********/\n"
                             "QWidget#transparentWidget {\n"
                             "        background: transparent;\n"
                             "}\n"
                             "\n"
                             "\n"
                             "/**********标签**********/\n"
                             "QLabel#grayLabel {\n"
                             "        color: rgb(70, 71, 73);\n"
                             "}\n"
                             "\n"
                             "QLabel#highlightLabel {\n"
                             "        color: rgb(2, 65, 132);\n"
                             "}\n"
                             "\n"
                             "QLabel#redLabel {\n"
                             "        color: red;\n"
                             "}\n"
                             "\n"
                             "QLabel#grayYaHeiLabel {\n"
                             "        color: rgb(175, 175, 175);\n"
                             "        font-size: 16px;\n"
                             "}\n"
                             "\n"
                             "QLabel#blueLabel {\n"
                             "        color: rgb(0, 160, 230);\n"
                             "}\n"
                             "\n"
                             "QLabel#listLabel {\n"
                             "        color: rgb(51, 51, 51);\n"
                             "}\n"
                             "\n"
                             "QLabel#lineBlueLabel {\n"
                             "        background: rgb(0, 78, 161);\n"
                             "}\n"
                             "\n"
                             "QLabel#graySeperateLabel {\n"
                             "        background: rgb(200, 220, 230);\n"
                             "}\n"
                             "\n"
                             "QLabel#seperateLabel {\n"
                             "        background: rgb(112, 153, 194);\n"
                             "}\n"
                             "\n"
                             "QLabel#radiusBlueLabel {\n"
                             "        border-radius: 15px;\n"
                             "        color: black;\n"
                             "        background: rgb(0, 78, 161);\n"
                             "}\n"
                             "\n"
                             "/**********按钮**********/\n"
                             "QPushButton{\n"
                             "        border-radius: 4px;\n"
                             "        border: none;\n"
                             "        width: 75px;\n"
                             "        height: 25px;\n"
                             "}\n"
                             "QPushButton:enabled {\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton:!enabled {\n"
                             "        background: rgb(180, 180, 180);\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton:enabled:hover{\n"
                             "        background: rgb(100, 160, 220);\n"
                             "}\n"
                             "QPushButton:enabled:pressed{\n"
                             "        background: rgb(0, 78, 161);\n"
                             "}\n"
                             "\n"
                             "QPushButton#blueButton {\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton#blueButton:enabled {\n"
                             "        background: rgb(0, 78, 161);\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton:!enabled {\n"
                             "        background: rgb(180, 180, 180);\n"
                             "        color: white;\n"
                             "}\n"
                             "QPushButton#blueButton:enabled:hover {\n"
                             "        background: rgb(2, 65, 132);\n"
                             "}\n"
                             "QPushButton#blueButton:enabled:pressed {\n"
                             "        background: rgb(6, 94, 187);\n"
                             "}\n"
                             "\n"
                             "QPushButton#selectButton {\n"
                             "        border: none;\n"
                             "        border-radius: none;\n"
                             "        border-left: 1px solid rgb(111, 156, 207);\n"
                             "        background: transparent;\n"
                             "        image: url(:/White/scan);\n"
                             "        color: rgb(51, 51, 51);\n"
                             "}\n"
                             "QPushButton#selectButton:enabled:hover{\n"
                             "        background: rgb(187, 212, 238);\n"
                             "}\n"
                             "QPushButton#selectButton:enabled:pressed{\n"
                             "        background: rgb(120, 170, 220);\n"
                             "}\n"
                             "\n"
                             "QPushButton#linkButton {\n"
                             "        background: transparent;\n"
                             "        color: rgb(0, 160, 230);\n"
                             "        text-align:left;\n"
                             "}\n"
                             "QPushButton#linkButton:hover {\n"
                             "        color: rgb(20, 185, 255);\n"
                             "        text-decoration: underline;\n"
                             "}\n"
                             "QPushButton#linkButton:pressed {\n"
                             "        color: rgb(0, 160, 230);\n"
                             "}\n"
                             "\n"
                             "QPushButton#transparentButton {\n"
                             "        background: transparent;\n"
                             "}\n"
                             "\n"
                             "/*****************标题栏按钮*******************/\n"
                             "QPushButton#minimizeButton {\n"
                             "        border-radius: none;\n"
                             "        border-bottom-left-radius: 4px;\n"
                             "        border-bottom-right-radius: 4px;\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        image: url(:/White/minimizeHover);\n"
                             "}\n"
                             "QPushButton#minimizeButton:hover {\n"
                             "        image: url(:/White/minimize);\n"
                             "}\n"
                             "QPushButton#minimizeButton:pressed {\n"
                             "        image: url(:/White/minimizePressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#maximizeButton[maximizeProperty=\"maximize\"] {\n"
                             "        border-radius: none;\n"
                             "        border-bottom-left-radius: 4px;\n"
                             "        border-bottom-right-radius: 4px;\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        image: url(:/White/maximizeHover);\n"
                             "}\n"
                             "QPushButton#maximizeButton[maximizeProperty=\"maximize\"]:hover {\n"
                             "        image: url(:/White/maximize);\n"
                             "}\n"
                             "QPushButton#maximizeButton[maximizeProperty=\"maximize\"]:pressed {\n"
                             "        image: url(:/White/maximizePressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#maximizeButton[maximizeProperty=\"restore\"] {\n"
                             "        border-radius: none;\n"
                             "        border-bottom-left-radius: 4px;\n"
                             "        border-bottom-right-radius: 4px;\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        image: url(:/White/restoreHover);\n"
                             "}\n"
                             "QPushButton#maximizeButton[maximizeProperty=\"restore\"]:hover {\n"
                             "        image: url(:/White/restore);\n"
                             "}\n"
                             "QPushButton#maximizeButton[maximizeProperty=\"restore\"]:pressed {\n"
                             "        image: url(:/White/restorePressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#closeButton {\n"
                             "        border-radius: none;\n"
                             "        border-bottom-left-radius: 4px;\n"
                             "        border-bottom-right-radius: 4px;\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        image: url(:/White/closeHover);\n"
                             "}\n"
                             "QPushButton#closeButton:hover {\n"
                             "        image: url(:/White/close);\n"
                             "}\n"
                             "QPushButton#closeButton:pressed {\n"
                             "        image: url(:/White/closePressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#skinButton {\n"
                             "        border-radius: none;\n"
                             "        border-bottom-left-radius: 4px;\n"
                             "        border-bottom-right-radius: 4px;\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        image: url(:/White/skinHover);\n"
                             "}\n"
                             "QPushButton#skinButton:hover {\n"
                             "        image: url(:/White/skin);\n"
                             "}\n"
                             "QPushButton#skinButton:pressed {\n"
                             "        image: url(:/White/skinPressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#feedbackButton {\n"
                             "        border-radius: none;\n"
                             "        border-bottom-left-radius: 4px;\n"
                             "        border-bottom-right-radius: 4px;\n"
                             "        background: rgb(120, 170, 220);\n"
                             "        image: url(:/White/feedbackHover);\n"
                             "}\n"
                             "QPushButton#feedbackButton:hover {\n"
                             "        image: url(:/White/feedback);\n"
                             "}\n"
                             "QPushButton#feedbackButton:pressed {\n"
                             "        image: url(:/White/feedbackPressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#closeTipButton {\n"
                             "        border-radius: none;\n"
                             "        border-image: url(:/White/close);\n"
                             "        background: transparent;\n"
                             "}\n"
                             "QPushButton#closeTipButton:hover {\n"
                             "        border-image: url(:/White/closeHover);\n"
                             "}\n"
                             "QPushButton#closeTipButton:pressed {\n"
                             "        border-image: url(:/White/closePressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#changeSkinButton{\n"
                             "        border-radius: 4px;\n"
                             "        border: 2px solid rgb(111, 156, 207);\n"
                             "        background: rgb(204, 227, 252);\n"
                             "}\n"
                             "QPushButton#changeSkinButton:hover{\n"
                             "        border-color: rgb(60, 150, 200);\n"
                             "}\n"
                             "QPushButton#changeSkinButton:pressed, QPushButton#changeSkinButton:checked{\n"
                             "        border-color: rgb(0, 160, 230);\n"
                             "}\n"
                             "\n"
                             "QPushButton#transferButton {\n"
                             "        padding-left: 5px;\n"
                             "        padding-right: 5px;\n"
                             "        color: white;\n"
                             "        background: rgb(0, 78, 161);\n"
                             "}\n"
                             "QPushButton#transferButton:hover {\n"
                             "        background: rgb(2, 65, 132);\n"
                             "}\n"
                             "QPushButton#transferButton:pressed {\n"
                             "        background: rgb(6, 94, 187);\n"
                             "}\n"
                             "QPushButton#transferButton[iconProperty=\"left\"] {\n"
                             "        qproperty-icon: url(:/White/left);\n"
                             "}\n"
                             "QPushButton#transferButton[iconProperty=\"right\"] {\n"
                             "        qproperty-icon: url(:/White/right);\n"
                             "}\n"
                             "\n"
                             "QPushButton#openButton {\n"
                             "        border-radius: none;\n"
                             "        image: url(:/White/open);\n"
                             "        background: transparent;\n"
                             "}\n"
                             "QPushButton#openButton:hover {\n"
                             "        image: url(:/White/openHover);\n"
                             "}\n"
                             "QPushButton#openButton:pressed {\n"
                             "        image: url(:/White/openPressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#deleteButton {\n"
                             "        border-radius: none;\n"
                             "        image: url(:/White/delete);\n"
                             "        background: transparent;\n"
                             "}\n"
                             "QPushButton#deleteButton:hover {\n"
                             "        image: url(:/White/deleteHover);\n"
                             "}\n"
                             "QPushButton#deleteButton:pressed {\n"
                             "        image: url(:/White/deletePressed);\n"
                             "}\n"
                             "\n"
                             "QPushButton#menuButton {\n"
                             "        text-align: left center;\n"
                             "        padding-left: 3px;\n"
                             "        color: rgb(84, 84, 84);\n"
                             "        border: 1px solid rgb(111, 156, 207);\n"
                             "        background: white;\n"
                             "}\n"
                             "QPushButton#menuButton::menu-indicator{\n"
                             "        subcontrol-position: right center;\n"
                             "        subcontrol-origin: padding;\n"
                             "        image: url(:/White/arrowBottom);\n"
                             "        padding-right: 3px;\n"
                             "}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.user_name = QtWidgets.QLineEdit(Dialog)
        self.user_name.setObjectName("user_name")
        self.verticalLayout.addWidget(self.user_name)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.cancel = QtWidgets.QPushButton(Dialog)
        self.cancel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cancel.setObjectName("cancel")
        self.verticalLayout.addWidget(self.cancel)
        self.login = QtWidgets.QPushButton(Dialog)
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.login.clicked.connect(self.login_check)
        self.cancel.clicked.connect(self.window_close)
        self.user_name.returnPressed.connect(self.login_check)
        self.password.returnPressed.connect(self.login_check)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "用户\\管理员登录"))
        self.label_2.setText(_translate("Dialog", "用户名"))
        self.user_name.setPlaceholderText(_translate("Dialog", "请输入用户名"))
        self.label_3.setText(_translate("Dialog", "密码"))
        self.password.setPlaceholderText(_translate("Dialog", "请输入密码"))
        self.cancel.setText(_translate("Dialog", "取消"))
        self.login.setText(_translate("Dialog", "登录"))

    def login_check(self):
        user_name = self.user_name.text()
        password = self.password.text()
        if (user_name == "" or password == ""):
            print(QMessageBox.warning(self, "警告", "用户名和密码不可为空!", QMessageBox.Ok))
            return
        # 进行数据库操作
        query = QSqlQuery()  # 新建sql对象
        query.prepare('SELECT * FROM 用户表 '
                      'WHERE 用户名  = :user_name')  # 输入SQL语句
        query.bindValue(":user_name", user_name)  # 绑定占位符和相应的功能
        query.exec_()

        if (not query.next()):
            QMessageBox.information(self, "提示", "该账号不存在!", QMessageBox.Ok)
        else:
            if (user_name == query.value(0) and password == query.value(1)):

                if (query.value(2) == 1):
                    # 跳转到后续管理员窗口
                    QMessageBox.information(self, "提示", "管理员登录成功!", QMessageBox.Ok)
                    self.power = 2
                    self.username = user_name
                    self.close()
                # 跳转到后续用户窗口
                else:
                    QMessageBox.information(self, "提示", "登录成功!", QMessageBox.Ok)
                    self.power = 1
                    self.username = user_name
                    self.close()
            else:
                QMessageBox.information(self, "提示", "密码错误!", QMessageBox.Ok)
        return

    def window_close(self):
        self.close()
    # 添加后续窗口