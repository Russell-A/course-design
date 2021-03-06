import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import PyQt5.QtGui
# 在这里加上所有的文件
from search import *
import search


class MyWindow(QMainWindow, search.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

conn = pyodbc.connect('DRIVER={SQL SERVER NATIVE CLIENT 10.0};SERVER=127.0.0.1;DATABASE=master;UID=sa;PWD=123456',autocommit= True)
cursor = conn.cursor()
sql = '''select * from sys.databases where name = 'air'
'''
cursor.execute(sql)
effectrow1 = cursor.fetchall()
conn.close()
#可以判断是否存在air数据库
if len(effectrow1) == 1:
    conn = pyodbc.connect('DRIVER={SQL SERVER NATIVE CLIENT 10.0};SERVER=127.0.0.1;DATABASE=air;UID=sa;PWD=123456')
    cursor = conn.cursor()
    sql = '''select 1
       from sys.sysreferences r join sys.sysobjects o on (o.id = r.constid and o.type = 'F')
       where r.fkeyid = object_id('航班') and o.name = 'FK_航班_FK_飞机编号_飞机登记'
    '''
    cursor.execute(sql)
    effectrow2 = cursor.fetchall()
    conn.close()
    if len(effectrow2) == 0:
        print('WRONG AIR, RESETUP!')
        import dbsetup
    else:
        print('ALREADY SETUP AIR')
else:
    print('NO AIR, SETUP AIR!')
    import dbsetup

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #链接数据库
    db = QSqlDatabase.addDatabase("QODBC")
    db.setDatabaseName("Driver={Sql Server};Server=127.0.0.1;Database=air")
    ok = db.open()
    # print(ok)

    #Query = QSqlQuery("select * from 机场")
    #while Query.next():
    #    print(Query.value(0),Query.value(1),)

    # #注册与登录窗口
    # # 实例化主窗口
    # main = QMainWindow()
    # main_ui = search.Ui_MainWindow()
    # main_ui.setupUi(main)
    # # 实例化注册子窗口
    # child_register, child_register_ui = register.Ui_Dialog.instantiation(register)
    # #实例化登录子窗口
    # child_login, child_login_ui = login.Ui_Dialog.instantiation(login)
    # # 按钮绑定事件
    # child_register_ui.button_connect(child_register, main_ui.register_2)
    # child_login_ui.button_connect(child_login, main_ui.login)
    # # 实例化二级子窗口
    # # 注册成功
    # register_win_dialog, register_win_dialog_ui = register_win.Ui_Dialog.instantiation(register_win)
    # # 注册失败
    # register_fail_dialog, register_fail_dialog_ui = register_win.Ui_Dialog.instantiation(register_fail)
    # # 判断注册是否成功
    # """
    # 判断是否存在重复命名
    # """
    # a = 0
    # # 注册成功
    # if a:
    #     register_win_dialog_ui.button_connect(register_win_dialog, child_register_ui.register_2)
    # # 注册失败
    # else:
    #     register_fail_dialog_ui.button_connect(register_fail_dialog, child_register_ui.register_2)
    #
    #
    # main.show()

    # 实例化窗口和子窗口
    # login_window = Login_Window()
    # register_window = Register_Window()
    myWin = MyWindow()

    # 按钮的绑定
    # myWin.login.clicked.connect(login_window.show)
    # myWin.register_2.clicked.connect(register_window.show)

    myWin.show()
    sys.exit(app.exec_())