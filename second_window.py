# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(492, 177)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 471, 121))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label.setObjectName("label")
        self.second_w_FullName = QtWidgets.QLabel(self.groupBox)
        self.second_w_FullName.setGeometry(QtCore.QRect(130, 20, 331, 16))
        self.second_w_FullName.setText("")
        self.second_w_FullName.setObjectName("second_w_FullName")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 101, 16))
        self.label_2.setObjectName("label_2")
        self.second_w_PhoneNumber = QtWidgets.QLabel(self.groupBox)
        self.second_w_PhoneNumber.setGeometry(QtCore.QRect(130, 40, 331, 16))
        self.second_w_PhoneNumber.setText("")
        self.second_w_PhoneNumber.setObjectName("second_w_PhoneNumber")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 101, 16))
        self.label_3.setObjectName("label_3")
        self.second_w_Email = QtWidgets.QLabel(self.groupBox)
        self.second_w_Email.setGeometry(QtCore.QRect(130, 60, 331, 16))
        self.second_w_Email.setText("")
        self.second_w_Email.setObjectName("second_w_Email")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 111, 16))
        self.label_4.setObjectName("label_4")
        self.second_w_sum_ = QtWidgets.QLabel(self.groupBox)
        self.second_w_sum_.setGeometry(QtCore.QRect(130, 80, 331, 16))
        self.second_w_sum_.setText("")
        self.second_w_sum_.setObjectName("second_w_sum_")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 111, 16))
        self.label_5.setObjectName("label_5")
        self.second_w_Comments = QtWidgets.QLabel(self.groupBox)
        self.second_w_Comments.setGeometry(QtCore.QRect(130, 100, 331, 16))
        self.second_w_Comments.setText("")
        self.second_w_Comments.setObjectName("second_w_Comments")
        self.Cansel = QtWidgets.QPushButton(Dialog)
        self.Cansel.setGeometry(QtCore.QRect(10, 140, 161, 31))
        self.Cansel.setObjectName("Cansel")
        self.Confirm = QtWidgets.QPushButton(Dialog)
        self.Confirm.setGeometry(QtCore.QRect(330, 140, 151, 31))
        self.Confirm.setObjectName("Confirm")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "ПЕРЕВІРТЕ ПРАВИЛЬНІСТЬ ВКАЗАНИХ ДАНИХ"))
        self.label.setText(_translate("Dialog", "ФІО :"))
        self.label_2.setText(_translate("Dialog", "Номер телефону :"))
        self.label_3.setText(_translate("Dialog", "Емейл :"))
        self.label_4.setText(_translate("Dialog", "сумма сертифікату :"))
        self.label_5.setText(_translate("Dialog", "Коментар :"))
        self.Cansel.setText(_translate("Dialog", "ВІДМІНИТИ"))
        self.Confirm.setText(_translate("Dialog", "ПІДТВЕРДИТИ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
