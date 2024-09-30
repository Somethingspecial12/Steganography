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
import numpy as np
from scipy.stats import chisquare
import math


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.setWindowTitle("Steganography Application")
        self.setGeometry(100, 100, 1500, 900)
        self.setFixedSize(1500, 900)
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
        #self.detection_ui.detectButton.clicked.connect(self.single_image_steganography_detection)

        
      
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
        self.single_stego_path = None




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
    


    
    #comparing two images clean and stego images method     
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
        label.setPixmap(pixmap.scaled(350, 350, Qt.KeepAspectRatio))
        label.setFixedSize(350, 350)



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

        # Now implement detection logic based on the histogram difference
        # You can define a threshold for detection
        total_diff = np.sum([np.sum(cv2.absdiff(clean_hist, stego_hist)) for clean_hist, stego_hist in zip(clean_histograms, stego_histograms)])

        # Define a threshold for considering the image as having steganography
        threshold = 1000  # You may need to fine-tune this value based on experiments

        if total_diff > threshold:
            print("Possible steganography detected based on histogram analysis.")
        else:
            print("No significant signs of steganography.")
    



    def display_histogram_on_label(self, image_path):
        if not os.path.exists(image_path):
            print(f"File does not exist: {image_path}")
            return
        else:
            print(f"File exists: {image_path}")
        
        # Load the saved histogram image and display it in the QLabel
        pixmap = QtGui.QPixmap(image_path)
        self.detection_ui.histogramLabel.setPixmap(pixmap.scaled(600, 700, Qt.KeepAspectRatio))


    #second method(first used method) - calculating histogram for single image :
    def show_histogram_analysis2(self):
        if self.filename:
            print(f"Filename in histogram analysis: {self.filename}")  # Debugging line
            self.show_histogram(self.filename)
        else:
            text = "No image selected for analysis."
            dlg = CustomDialog(text)
            dlg.exec()

    def show_histogram(self, image_path):
        if not image_path or not os.path.exists(image_path):
            print(f"Invalid image path: {image_path}")
            return
        
        image = cv2.imread(image_path)
        if image is None:
            print(f"Failed to load image from {image_path}.")
            return

        # Define the correct color list for histogram
        color = ['b', 'g', 'r']  # Blue, Green, Red channels
        plt.figure(figsize=(6, 4))  # Set figure size
        
        for i, col in enumerate(color):
            hist = cv2.calcHist([image], [i], None, [256], [0, 256])
            plt.plot(hist, color=col)
            plt.xlim([0, 256])
        
        # Save the plot as an image
        histogram_image_path = 'histogram.png'
        plt.savefig(histogram_image_path)
        plt.close()  # Close the plot after saving
        
        # Display the histogram image in a QLabel
        self.display_histogram_on_label(histogram_image_path)




    #third method for single image detection - calculating chi square, entropology and Rs analysis
    def single_image_steganography_detection(self):
        self.single_stego_path, _ = QFileDialog.getOpenFileName(self, 'Select Image for Detection', '', "Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*.*)")
        
        if not self.single_stego_path:
            print("No image selected.")
            return
        
        # Call the detection function
        self.detect_steganography(self.single_stego_path)



    def detect_steganography(self, image_path):

        if not os.path.exists(image_path):
            print("Invalid image path.")
            return

        image = cv2.imread(image_path)
        if image is None:
            print("Failed to load image.")
            return

        # Step 1: Calculate the histogram for the image
        histograms = []
        colors = ('b', 'g', 'r')
        for i, color in enumerate(colors):
            hist = cv2.calcHist([image], [i], None, [256], [0, 256])
            histograms.append(hist)

        

        # Step 2: Calculate statistical tests (e.g., chi-square or entropy)
        chi_square_value = self.perform_chi_square_test(image)
        entropy_value = self.calculate_entropy(image)
        #rs_analysis_result = self.rs_analysis(image_path)

        chi_square_threshold = 0.05
        entropy_threshold = 7.5  # This is an arbitrary example, tune it based on your needs

        if chi_square_value > chi_square_threshold or entropy_value < entropy_threshold: #or rs_analysis_result:
            print("Suspicious image. Possible steganography detected.")
        else:
            print("No significant signs of steganography.")

    


    def perform_chi_square_test(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

        expected_freq = np.mean(hist)  # Average frequency as the expected distribution
        chi_square_value, p_value = chisquare(hist.flatten(), [expected_freq]*256)
        
        return chi_square_value  # Or you can return p-value to determine the threshold



    

    def calculate_entropy(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
        hist_prob = hist / hist.sum()

        # Ensure each element is a scalar by accessing `p[0]`
        entropy = -np.sum([float(p[0]) * math.log2(float(p[0])) for p in hist_prob if p[0] != 0])
        return entropy


            

    def rs_analysis(self,image_path):
        #Step 1: Load image
        
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            print(f"Failed to load image: {image_path}")
            return None

        height, width = image.shape

        # Step 2: Define block size (e.g., 2x2 blocks)
        block_size = 2

        def smoothness(block):
            # Measure smoothness of a block by calculating the sum of absolute differences between neighboring pixels
            diffs = []
            diffs.append(abs(int(block[0, 0]) - int(block[0, 1])))
            diffs.append(abs(int(block[0, 0]) - int(block[1, 0])))
            diffs.append(abs(int(block[1, 0]) - int(block[1, 1])))
            diffs.append(abs(int(block[0, 1]) - int(block[1, 1])))
            return sum(diffs)

        def flip_lsb(block):
            # Flip the least significant bit of each pixel in the block
            return block ^ 1

        regular_count = 0
        singular_count = 0

        # Step 3: Iterate over the image by block size
        for i in range(0, height - block_size + 1, block_size):
            for j in range(0, width - block_size + 1, block_size):
                block = image[i:i+block_size, j:j+block_size]

                # Calculate the smoothness of the original block
                original_smoothness = smoothness(block)

                # Flip the least significant bits (LSBs) of the block
                flipped_block = flip_lsb(block)

                # Calculate the smoothness of the flipped block
                flipped_smoothness = smoothness(flipped_block)

                # Step 4: Classify the block
                if flipped_smoothness > original_smoothness:
                    # If flipping increases smoothness, it's a regular block
                    regular_count += 1
                elif flipped_smoothness < original_smoothness:
                    # If flipping decreases smoothness, it's a singular block
                    singular_count += 1

        # Step 5: Calculate R-S ratio
        total_blocks = regular_count + singular_count
        if total_blocks == 0:
            print("No blocks analyzed.")
            return None

        regular_ratio = regular_count / total_blocks
        singular_ratio = singular_count / total_blocks

        print(f"Regular blocks: {regular_count}, Singular blocks: {singular_count}")
        print(f"Regular ratio: {regular_ratio:.4f}, Singular ratio: {singular_ratio:.4f}")

        # Step 6: Steganography detection logic
        # If regular and singular groups become more balanced, it suggests possible LSB steganography
        ratio = abs(regular_ratio - singular_ratio)

        if ratio < 0.1:
            print("Suspicious image. Possible steganography detected. called from RS analysis")
            return True  # Steganography likely
        
        else:
            print("No significant signs of steganography. called from RS analysis")
            return False
            



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
