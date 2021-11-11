from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os

import bulkrename_GUI

class BulkRenameQT(QDialog, bulkrename_GUI.Ui_bulkrename):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        # assign actions to all buttons
        self.start.clicked.connect(self.start_button)

    def start_button(self, closeEvent):
        file_destination = self.URL.toPlainText()
        rename_text = self.Append.toPlainText()

        i = 0

        a = 0

        if file_destination == "":
            file_destination = os.getcwd()

        path = file_destination + "/"

        for filename in os.listdir(path):
            extension = os.path.splitext(filename)[1]
            print(filename)
            if filename.endswith('.py'):
                i += 1
            elif os.path.isdir(filename):
                i += 1
            else:  
                my_dest = rename_text + str(a) + extension
                my_source = path + filename
                my_dest = path + my_dest
                os.rename(my_source, my_dest)
                a += 1
                i += 1


        quit_msg = QMessageBox.question(self, "Complete", "Rename is complete, close app?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if quit_msg == QMessageBox.Yes:
            exit()

app = QApplication(sys.argv)
bulkrenameQT = BulkRenameQT()
bulkrenameQT.show()
app.exec_()
