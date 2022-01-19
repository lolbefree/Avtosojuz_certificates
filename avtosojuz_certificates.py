import sys
from random import randint
import code128
import requests as requests
from PIL import Image
import os
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator, QIcon
from PyQt5.QtWidgets import QDialog
import not_for_git
import main_gui
import mailsender
import second_window
from win10toast import ToastNotifier
import pyodbc
import getpass
import configparser

import sql_querys


class AnotherWindow(QDialog):
    """
    get parameters from MainProgram
    """

    def __init__(self, fullname, phone_number, email, sum_, comments):
        self.config_name = "avtosojuz_certificates.exe.config"
        config = configparser.ConfigParser()
        self.random_int = int()
        self.FullName = fullname
        self.Phone_number = phone_number
        self.Email = email
        self.Sum_ = sum_
        self.Comments = comments
        if "'" in comments:
            self.Comments = self.Comments.replace("'", "")

        super().__init__()
        self.ui2 = second_window.Ui_Dialog()
        self.ui2.setupUi(self)
        self.setWindowTitle("Сертифікати")
        self.setWindowIcon(QIcon("app.ico"))
        self.setStyleSheet("""
                QDialog {
                background-color: #919090}
                QPushButton{
                background-color: #cdd3d7;
                color: #272627;
                }
                QLineEdit {
                background-color: #cdd3d7;}
                QTextEdit {
                background-color: #cdd3d7;
                }
                """)
        config.read(self.config_name)
        self.server = config.get("DEFAULT", "sql_server")
        self.database = config.get("DEFAULT", "sql_db")
        self.username = config.get("DEFAULT", "sql_user")
        self.password = config.get("DEFAULT", "sql_pw")
        self.driver = '{SQL Server}'  # Driver you need to connect to the database
        self.port = '1433'
        self.name = ""
        self.if_in_base = False
        self.row_count = int()

        self.cnn = pyodbc.connect(
            'DRIVER=' + self.driver + ';PORT=port;SERVER=' + self.server + ';PORT=1443;DATABASE=' + self.database
            + ';UID=' + self.username + ';PWD=' + self.password)
        self.ui2.Confirm.clicked.connect(lambda x: self.start())
        self.ui2.Cansel.clicked.connect(lambda x: self.close())
        self.ui2.second_w_FullName.setText(self.FullName)
        self.ui2.second_w_PhoneNumber.setText(self.Phone_number)
        self.ui2.second_w_Email.setText(self.Email)
        self.ui2.second_w_sum_.setText(self.Sum_)
        self.ui2.second_w_Comments.setText(self.Comments)
        self.cursor = self.cnn.cursor()

    def insert_into_base(self, id_cert):

        self.cursor.execute((sql_querys.add_cert_to_base(id_cert, self.FullName, self.Phone_number, self.Sum_,
                                                         getpass.getuser(), self.Comments, self.Email)))
        self.cnn.commit()

    def start(self):
        self.random_int = randint(1000000000, 9999999999)
        sql_res = list(self.cursor.execute(sql_querys.if_exit_id(self.random_int)))
        if sql_res[0][0] == 'none':
            self.insert_into_base(self.random_int)
            cd = code128.image('{}'.format(self.random_int))
            cd.save("{}\\{}.png".format(os.getcwd(), self.random_int))
            img1 = Image.open(f'{os.getcwd()}\\cert.jpg')  # main image
            new_barcode = Image.open("{}\\{}.png".format(os.getcwd(), self.random_int))

            img1.paste(new_barcode, (50, 950))  # paste barcode to main image
            img1.save(f"{os.getcwd()}\\img_with_barcode.png")

            mailsender.sender(self.Email, self.FullName, "img_with_barcode.png")
            self.my_notifier(f"Сертифікат на ім'я {self.FullName} відправлено! ")
            text = f"Сертифікат відпралено на: {self.Email}, також можете користуватись ботом(отримання, залишок, історія) {'https://t.me/AvtosojuzBot'} "

            self.sent_sms(self.Phone_number, text)
            os.remove(f"{os.getcwd()}\\img_with_barcode.png")
            os.remove(f"{os.getcwd()}\\{self.random_int}.png")
            sys.exit()
        else:
            self.start()

    def sent_sms(self, to, text):
        # r = requests.post(
        #     f"https://api.turbosms.ua/message/send.json?recipients[0]\
        #     =38{to}&sms[sender]=AVTOSOJUZ&sms[text]={text}&token={not_for_git.token}")
        query = f"""
        DECLARE @Script nvarchar(max) =
        N'
        insert into avtosojuz (message,number,sign)
        values (''{text}'', ''38{to}'', ''AVTOSOJUZ'');'
         EXECUTE (@script) AT turbosms;
"""
        self.cursor.execute(query)
        self.cnn.commit()

    def my_notifier(self, x):
        toaster = ToastNotifier()
        toaster.show_toast(f"{x}", f"{x}",
                           threaded=True, icon_path="app.ico", duration=5)


class MainProgram(main_gui.Ui_MainWindow):
    def __init__(self):
        self.config_name = "avtosojuz_certificates.exe.config"
        if not os.path.isfile(self.config_name):
            self.createConfig()

        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()
        window.setWindowIcon(QIcon("app.ico"))

        window.show()
        self.setupUi(window)
        window.setWindowTitle("Сертифікати")
        window.setStyleSheet("""
        QMainWindow {
        background-color: #919090}
        QPushButton{
        background-color: #cdd3d7;
        color: #272627;
        }
        QLineEdit {
        background-color: #cdd3d7;}
        QTextEdit {
        background-color: #cdd3d7;
        }
        """)
        self.FullName.setToolTip("ПІБ")
        self.FullName.setPlaceholderText("ПІБ")

        self.PhoneNumber.setToolTip("Телефон клієнта")
        self.PhoneNumber.setPlaceholderText("Телефон клієнта в форматі 050ххххххх")
        self.Email.setToolTip("Електронна пошта клієнта")
        self.Email.setPlaceholderText("Електронна пошта клієнта")
        self.sum_.setToolTip("Вкажіть сумму сертифіката")
        self.sum_.setPlaceholderText("Вкажіть сумму сертифіката")
        self.Comments.setToolTip("Коментарі")
        self.Comments.setPlaceholderText("Коментарі")
        self.PhoneNumber.setValidator(QIntValidator(0, 2147483647))
        self.sum_.setValidator(QIntValidator(0, 2147483647))
        self.Cansel.clicked.connect(lambda x: sys.exit())
        self.Confirm.clicked.connect(lambda x: self.apply())

        sys.exit(app.exec_())

    def createConfig(self):
        """
        Create a config file
        """
        config = configparser.ConfigParser()
        config.add_section("Settings")
        config.set("DEFAULT", "certificate_template_861x1212", "cert.jpg")
        config.set("DEFAULT", "sql_server", not_for_git.db_server)
        config.set("DEFAULT", "sql_db", not_for_git.db_name)
        config.set("DEFAULT", "sql_user", not_for_git.db_user)
        config.set("DEFAULT", "sql_pw", not_for_git.db_pw)
        with open(self.config_name, "w") as config_file:
            config.write(config_file)

        os.system('attrib +H *.config /S')

    def apply(self):
        if not self.FullName.text():
            self.Resalt.setText("Заповніть поле ФІО")
            self.Resalt.setStyleSheet("color: red")
        elif not self.PhoneNumber.text():
            self.Resalt.setText("Заповніть поле телефон")
            self.Resalt.setStyleSheet("color: red")
        elif not self.Email.text():
            self.Resalt.setText("Заповніть поле емейл")
            self.Resalt.setStyleSheet("color: red")
        elif "." not in self.Email.text() or "@" not in self.Email.text():
            self.Resalt.setText("Не вірно вказаний емейл")
            self.Resalt.setStyleSheet("color: red")
        elif not self.Comments.toPlainText():
            self.Resalt.setText("Заповніть поле коментарі")
            self.Resalt.setStyleSheet("color: red")
        elif not self.sum_.text():
            self.Resalt.setText("Заповніть поле сумми сертифікату")
            self.Resalt.setStyleSheet("color: red")

        else:
            w = AnotherWindow(self.FullName.text(), self.PhoneNumber.text(), self.Email.text(), self.sum_.text(),
                              self.Comments.toPlainText())
            w.exec_()


if __name__ == '__main__':
    main = MainProgram()
