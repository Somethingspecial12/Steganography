import sys

from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QLabel,QVBoxLayout

class CustomDialog(QDialog):
   
   
    def __init__(self, message):
        super().__init__()

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        messag = QLabel(message)
        self.layout.addWidget(messag)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

