import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from dialogclass import CustomDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        message = "none"     
        dlg = CustomDialog(message)
        dlg.exec()
        try:
            print("Success!")
        except:
            print("Cancel!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()