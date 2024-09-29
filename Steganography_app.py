import sys
import os
from turtle import color
from PyQt5.QtCore import  Qt, QPoint 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QFrame, QLabel, QPushButton, QFileDialog, QPlainTextEdit, QInputDialog
from PIL import Image
from PIL import ImageQt
import cv2
from matplotlib import pyplot as plt
from mainpage import Ui_Dialog as MainPageUi
from encode_page import Ui_Dialog as EncodePageUi
from decode_page import Ui_Dialog as DecodePageUi
from detection import Ui_Dialog as DetectionPageUi
import numpy as np
from stegano import lsb
from dialogclass import CustomDialog
from cryptography.fernet import Fernet
import base64
import hashlib

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.setWindowTitle("Steganography Application")
        self.setGeometry(100, 100, 1200, 700)
        self.setFixedSize(1200, 700)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
       
        # Setup main page
        self.main_page = MainPageUi()
        self.main_widget = QWidget()
        self.main_page.setupUi(self.main_widget)

        # Connect buttons to methods to change pages
        self.main_page.pushButton_3.clicked.connect(self.show_encode_page)
        self.main_page.pushButton_4.clicked.connect(self.show_decode_page)
        self.main_page.closeButton.clicked.connect(self.close_application)
        self.main_page.minimizeButton.clicked.connect(self.minimize_application)
        self.main_page.pushButton_5.clicked.connect(self.show_detection_page)

        
        self.central_widget.addWidget(self.main_widget)

        # Setup encode page
        self.encode_page_ui = EncodePageUi()
        self.encode_page = QWidget()
        self.encode_page_ui.setupUi(self.encode_page)
        self.encode_page_ui.closeButton.clicked.connect(self.close_application)
        self.encode_page_ui.minimizeButton.clicked.connect(self.minimize_application)
        self.encode_page_ui.selectButton.clicked.connect(lambda: self.select_image(self.encode_page_ui.encodeImageLabel))
        self.encode_page_ui.encodeButton.clicked.connect(self.encode_message)
        self.encode_page_ui.encryptButton.clicked.connect(self.encrypt_message)
        self.encode_page_ui.saveButton.clicked.connect(self.save_image)
         
        # Setup decode page
        self.decode_page_ui = DecodePageUi()
        self.decode_page = QWidget()
        self.decode_page_ui.setupUi(self.decode_page)
        self.decode_page_ui.closeButton.clicked.connect(self.close_application)
        self.decode_page_ui.minimizeButton.clicked.connect(self.minimize_application)
        self.decode_page_ui.select_image.clicked.connect(lambda: self.select_image(self.decode_page_ui.decodeImageLabel))
        self.decode_page_ui.decodeButton.clicked.connect(self.decode_message)
        self.decode_page_ui.decryptButton.clicked.connect(self.decrypt_message)

        # Setup detection page
        self.detection_ui = DetectionPageUi()
        self.detection = QWidget()
        self.detection_ui.setupUi(self.detection)
        self.detection_ui.closeButton_2.clicked.connect(self.close_application)
        self.detection_ui.minimizeButton_2.clicked.connect(self.minimize_application)
        #self.detection_ui.selectButton_2.clicked.connect(lambda: self.select_image(self.detection_ui.encodeImageLabel_2))
        self.detection_ui.histogramButton.clicked.connect(self.show_histogram_analysis)
        
      
        # Add all pages to the stacked widget
        self.central_widget.addWidget(self.encode_page)
        self.central_widget.addWidget(self.decode_page)
        self.central_widget.addWidget(self.detection)


        # Optional: Connect buttons in encode page and decode buttons
        self.encode_page_ui.backButton.clicked.connect(self.show_main_page)
        self.decode_page_ui.backButton.clicked.connect(self.show_main_page)
        self.detection_ui.backButton_2.clicked.connect(self.show_main_page)
        self.detection_ui.cleanimageButton.clicked.connect(self.select_clean_image)
        self.detection_ui.StegoimageButton.clicked.connect(self.select_stego_image)

         # Variables to store mouse press state
        self.dragging = False
        self.offset = QPoint()

        # Install event filter on the title frame to handle mouse events
        self.main_page.titleframe.installEventFilter(self)
        self.encode_page_ui.titleframe.installEventFilter(self)
        self.decode_page_ui.titleframe.installEventFilter(self)
        self.detection_ui.titleframe.installEventFilter(self)

         # Initialize variables
        self.filename = None
        self.secret = None
        self.clean_image_path = None
        self.stego_image_path = None




    def show_main_page(self):
        self.central_widget.setCurrentWidget(self.main_widget)



    def show_encode_page(self):
        self.central_widget.setCurrentWidget(self.encode_page)



    def show_decode_page(self):
        self.central_widget.setCurrentWidget(self.decode_page)


    
    
    def show_detection_page(self):
        self.central_widget.setCurrentWidget(self.detection)



    def close_application(self):
        self.close()



    def minimize_application(self):
        self.showMinimized()

    

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton:
                self.dragging = True
                self.offset = event.globalPos() - self.frameGeometry().topLeft()
                return True
        elif event.type() == QtCore.QEvent.MouseMove and self.dragging:
            self.move(event.globalPos() - self.offset)
            return True
        elif event.type() == QtCore.QEvent.MouseButtonRelease:
            if event.button() == Qt.LeftButton:
                self.dragging = False
                return True
        return QMainWindow.eventFilter(self, obj, event)
    

      
    def select_image(self, image_label):
        filename, _ = QFileDialog.getOpenFileName(self, 'Select Image File', os.getcwd(), "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*.*)")
        print(f"Selected file: {filename}")  # Debugging print
        
        if filename:
            self.filename = filename  # Store the filename for encoding/decoding
            img = Image.open(filename)
            img = img.convert("RGBA")
            data = img.tobytes("raw", "RGBA")
            q_image = QtGui.QImage(data, img.width, img.height, QtGui.QImage.Format_RGBA8888)
            pixmap = QtGui.QPixmap.fromImage(q_image)
            image_label.setPixmap(pixmap.scaled(400, 400, Qt.KeepAspectRatio))
            image_label.setFixedSize(400, 400)
        else:
            print("No file selected.")


            
    def save_image(self):
        if self.secret:
            save_path, _ = QFileDialog.getSaveFileName(self, 'Save Image File', '', "PNG Files (*.png);;All Files (*.*)")
            if save_path:
                self.secret.save(save_path)
                text = "Image saved at " + save_path 
                

            else:
                #print("Save operation cancelled.")
                text= "Save operation cancelled."

        else:
            #print("No encoded image to save.")
             text= "No encoded image to save."

        dlg = CustomDialog(text)
        dlg.exec()

        try:
            print("Success!")
        except:
            print("Cancel!")



    def encrypt_message(self):
        message = self.encode_page_ui.messageTextEdit.toPlainText()
        if message:      
            KEY, ok = QInputDialog.getText(self, 'Encryption key', 'ENTER A KEY TO ENCRYPT')
            if ok and  KEY:
                encrypted_message = self.symmetricEncryption(message, KEY)
                self.encode_page_ui.messageTextEdit.setPlainText(encrypted_message)

        else: 
            #print("enter the text to encrypt")
            text= "enter the text to encrypt"
            dlg = CustomDialog(text)
            dlg.exec()
        
        
    def symmetricEncryption(self, message, KEY):
        key = hashlib.sha256(KEY.encode()).digest()
        fernet_key = base64.urlsafe_b64encode(key[:32])
        fernet = Fernet(fernet_key)
        encrypted_message = fernet.encrypt(message.encode()).decode()
        return encrypted_message
            


    def encode_message(self):     
        if self.filename:
            message = self.encode_page_ui.messageTextEdit.toPlainText()
            if message:
                self.secret = lsb.hide(self.filename, message)
                text ="Message encoded."
            else:
                text ="enter text to encode the message"

        else:
            text="No image selected to encode the message."

        dlg = CustomDialog(text)
        dlg.exec()

        try:
            print("Success!")
        except:
            print("Cancel!")



    def decode_message(self):
        if self.filename:
            clear_message = lsb.reveal(self.filename)
            self.decode_page_ui.messageTextEdit.setPlainText(clear_message)
            #print("Message decoded.")
            text = "Message decoded."
        else:
            #print("No image selected to decode the message.")
            text = "No image selected to decode the message."

        dlg = CustomDialog(text)
        dlg.exec()

        try:
            print("Success!")
        except:
            print("Cancel!")



    def decrypt_message(self):
        message = self.decode_page_ui.messageTextEdit.toPlainText()
        if message:      
            KEY, ok = QInputDialog.getText(self, 'GETTING DECRYPTION KEY', 'ENTER THE KEY TO DECRYPT')
            if ok and  KEY:
               decrypted_message = self.symmetricDecryption(message, KEY)
               self.decode_page_ui.messageTextEdit.setPlainText(decrypted_message)

        else: 
            #print("enter the text to encrypt")
            text= "Decode the message first to decrypt it!"
            dlg = CustomDialog(text)
            dlg.exec()



    def symmetricDecryption(self, message, KEY):
        
        key = hashlib.sha256(KEY.encode()).digest()
        fernet_key = base64.urlsafe_b64encode(key[:32])
        fernet = Fernet(fernet_key)
        decrypted_message = fernet.decrypt(message.encode()).decode()
        return decrypted_message
    
    
    def select_clean_image(self):
        
        self.clean_image_path, _ = QFileDialog.getOpenFileName(self, 'Select Clean Image', '', "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*.*)")
        if self.clean_image_path:
            self.display_image(self.clean_image_path, self.detection_ui.cleanImageLabel)
        else:
            print("No clean image selected.")
    
    def select_stego_image(self):
       
        self.stego_image_path, _ = QFileDialog.getOpenFileName(self, 'Select Stego Image', '', "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*.*)")
        if self.stego_image_path:
            self.display_image(self.stego_image_path, self.detection_ui.stegoImageLabel)
        else:
            print("No stego image selected.")


    def display_image(self, image_path, label):
       
        img = Image.open(image_path)
        img = img.convert("RGBA")
        data = img.tobytes("raw", "RGBA")
        q_image = QtGui.QImage(data, img.width, img.height, QtGui.QImage.Format_RGBA8888)
        pixmap = QtGui.QPixmap.fromImage(q_image)
        label.setPixmap(pixmap.scaled(175, 175, Qt.KeepAspectRatio))
        label.setFixedSize(175, 175)

    def show_histogram_analysis(self):
  
        if not self.clean_image_path or not self.stego_image_path:
            print("Invalid image path(s)")
            return

        clean_image = cv2.imread(self.clean_image_path)
        stego_image = cv2.imread(self.stego_image_path)
        
        if clean_image is None or stego_image is None:
            print("Failed to load image(s).")
            return

        # Compute histograms for both images
        clean_histograms = []
        stego_histograms = []
        colors = ('b', 'g', 'r')
        
        plt.figure(figsize=(8, 6))  # Set figure size
        
        for i, color in enumerate(colors):
            clean_hist = cv2.calcHist([clean_image], [i], None, [256], [0, 256])
            stego_hist = cv2.calcHist([stego_image], [i], None, [256], [0, 256])

            clean_histograms.append(clean_hist)
            stego_histograms.append(stego_hist)
            
            # Compute histogram difference
            hist_diff = stego_hist - clean_hist
            
            # Plot the histograms for the current color channel
            plt.subplot(3, 1, i + 1)  # One subplot for each color channel (B, G, R)
            plt.plot(hist_diff, color=color)
            plt.xlim([0, 256])
            plt.title(f'Difference in {color.upper()} channel')
            plt.xlabel('Pixel Intensity')
            plt.ylabel('Difference')
        
        plt.tight_layout()
        plt.show()

        # Save the plot as an image
        difference_image_path = 'histogram_difference.png'
        plt.savefig(difference_image_path)
        plt.close()

        # Display the difference histogram image in the QLabel
        self.display_histogram_on_label(difference_image_path)

    



    def display_histogram_on_label(self, image_path):
        if not os.path.exists(image_path):
            print(f"File does not exist: {image_path}")
            return
        else:
            print(f"File exists: {image_path}")
        
        # Load the saved histogram image and display it in the QLabel
        pixmap = QtGui.QPixmap(image_path)
        self.detection_ui.histogramLabel.setPixmap(pixmap.scaled(600, 700, Qt.KeepAspectRatio))
            



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
