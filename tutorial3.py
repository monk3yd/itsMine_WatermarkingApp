# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(180, 170, 441, 221))
        self.button.setObjectName("button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button.setText(_translate("MainWindow", "Show Popup"))

    def show_popup(self):
        msg = QMessageBox()
        # MessageBox Title
        msg.setWindowTitle("Tutorial on PyQt6")

        # MessageBox Text
        msg.setText("This is the main text!")

        # MessageBox Icons
        # msg.setIcon(QMessageBox.Icon.Critical)
        # msg.setIcon(QMessageBox.Icon.Warning)
        msg.setIcon(QMessageBox.Icon.Information)
        # msg.setIcon(QMessageBox.Icon.Question)

        # MessageBox Buttons
        msg.setStandardButtons(QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Save|QMessageBox.StandardButton.Reset)
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        # QMessageBox.Ok  An “OK” button defined with the AcceptRole.
        # QMessageBox.Open  An “Open” button defined with the AcceptRole.
        # QMessageBox.Save  A “Save” button defined with the AcceptRole.
        # QMessageBox.Cancel  A “Cancel” button defined with the RejectRole.
        # QMessageBox.Close  A “Close” button defined with the RejectRole.
        # QMessageBox.Discard  A “Discard” or “Don’t Save” button, depending on the platform, defined with the DestructiveRole.
        # QMessageBox.Apply  An “Apply” button defined with the ApplyRole.
        # QMessageBox.Reset  A “Reset” button defined with the ResetRole.
        # QMessageBox.RestoreDefaults  A “Restore Defaults” button defined with the ResetRole.
        # QMessageBox.Help  A “Help” button defined with the HelpRole.
        # QMessageBox.SaveAll  A “Save All” button defined with the AcceptRole.
        # QMessageBox.Yes  A “Yes” button defined with the YesRole.
        # QMessageBox.YesToAll  A “Yes to All” button defined with the YesRole.
        # QMessageBox.No  A “No” button defined with the NoRole.
        # QMessageBox.NoToAll  A “No to All” button defined with the NoRole.
        # QMessageBox.Abort  An “Abort” button defined with the RejectRole.
        # QMessageBox.Retry  A “Retry” button defined with the AcceptRole.
        # QMessageBox.Ignore  An “Ignore” button defined with the AcceptRole.
        # QMessageBox.NoButton

        # MessageBox Informative Text
        msg.setInformativeText("Informative Text, Yeah!")

        # MessageBox Detail Text
        msg.setDetailedText("details")

        # Link Buttons in MessageBox
        msg.buttonClicked.connect(self.popup_button)

        # Show Popup
        x = msg.exec()

    # Button Func, i represents the widget
    def popup_button(self, i):
        print(i.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
