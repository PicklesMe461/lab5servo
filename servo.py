# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'servo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(646, 262)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(70, 80, 112, 23))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setGeometry(QtCore.QRect(120, 80, 112, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setEnabled(True)
        self.radioButton_3.setGeometry(QtCore.QRect(180, 80, 112, 23))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setEnabled(True)
        self.radioButton_4.setGeometry(QtCore.QRect(240, 80, 112, 23))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Form)
        self.radioButton_5.setEnabled(True)
        self.radioButton_5.setGeometry(QtCore.QRect(300, 80, 112, 23))
        self.radioButton_5.setObjectName("radioButton_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 70, 181, 41))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.setGeometry(QtCore.QRect(80, 160, 481, 20))
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.horizontalSlider.setMouseTracking(False)
        self.horizontalSlider.setTabletTracking(False)
        self.horizontalSlider.setAutoFillBackground(False)
        self.horizontalSlider.setMaximum(180)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setProperty("Angle", 0)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton.setText(_translate("Form", "0"))
        self.radioButton_2.setText(_translate("Form", "45"))
        self.radioButton_3.setText(_translate("Form", "90"))
        self.radioButton_4.setText(_translate("Form", "135"))
        self.radioButton_5.setText(_translate("Form", "180"))
        self.pushButton.setText(_translate("Form", "Release Motor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
