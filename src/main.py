import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from GUI import Ui_Window

class MainWindow(Ui_Window):
    def __init__(self, app_MainWindow):
        Ui_Window.__init__(self)
        self.setupUi(app_MainWindow)
        self.dir = os.getcwd()
        self.index = 0
        self.load_images()
        self.pushNext.clicked.connect(self.next_image)
        self.pushPrevious.clicked.connect(self.prev_image)
        self.pushBrowse.clicked.connect(self.dir_browse)
        
    def dir_browse(self):
        self.dir = QFileDialog.getExistingDirectory()
        self.load_images()

    def next_image(self):
        filename = self.lineEdit.text()
        if not filename == self.imagelist[self.index]:
            image_path1 = os.path.join(self.dir, self.imagelist[self.index])
            image_path2 = os.path.join(self.dir, filename)
            os.rename(image_path1, image_path2)
            self.load_images()
        self.index += 1
        if self.index >= len(self.imagelist):
            self.index = 0
        self.display_image()
        
    def prev_image(self):
        filename = self.lineEdit.text()
        if not filename == self.imagelist[self.index]:
            image_path1 = os.path.join(self.dir, self.imagelist[self.index])
            image_path2 = os.path.join(self.dir, filename)
            os.rename(image_path1, image_path2)
            self.load_images()
        self.index -= 1
        if self.index < 0:
            self.index = len(self.imagelist) -1
        self.display_image()
        
    def display_image(self):
        image = self.imagelist[self.index]
        image_path = os.path.join(self.dir, image)
        image_profile = QtGui.QImage(image_path) #QImage object
        image_profile = image_profile.scaled(480,510, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image_profile))
        self.lineEdit.setText(image)
        

    def load_images(self):
        self.lineBrowse.setText(self.dir)
        imagelist = []
        for file in os.listdir(self.dir):
            if file.endswith(".jpg") or file.endswith(".gif") or file.endswith(".png") or file.endswith(".bmp"):
                imagelist.append(file)
        if len(imagelist) == 0:
            self.msgbox("Select a folder with images.")
            self.dir_browse()
        else:
            self.index = 0
            self.imagelist = imagelist
            self.display_image()
        
    def msgbox(self, str):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(str)
        msg.setWindowTitle("Information")
        msg.exec_()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget_MainWindow = QtWidgets.QWidget()
    widget_MainWindow.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowCloseButtonHint)
    app_MainWindow = MainWindow(widget_MainWindow)
    
    widget_MainWindow.show()
    
    sys.exit(app.exec_())
