import sys
from tkinter import Image
from tkinter.filedialog import FileDialog

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from dialogclass import CustomDialog
def select_image(self, image_label):
        filename, _ = FileDialog.getOpenFileName(self, 'Select Image File', os.getcwd(), "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*.*)")
        if filename:
            self.filename = filename  # Store the filename for encoding/decoding
            img = Image.open(filename)
            img = img.convert("RGBA")
            data = img.tobytes("raw", "RGBA")
            q_image = QtGui.QImage(data, img.width, img.height, QtGui.QImage.Format_RGBA8888)
            pixmap = QtGui.QPixmap.fromImage(q_image)
            image_label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))
            image_label.setFixedSize(400, 400)
            