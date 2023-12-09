import os
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("image_viewer.ui", self)  # load the file.ui into the class
        self.show()
        self.current_file = "01.jpg" # Default image
        pixmap = QtGui.QPixmap(self.current_file)
        pixmap = pixmap.scaled(self.width(), self.height()) 
        self.label.setPixmap(pixmap)  # our label is the image
        self.label.setMinimumSize(1, 1)
        self.file_list = None
        self.file_counter = None
        self.actionOpen_Image.triggered.connect(self.open_image) # connecting the menu item "Open Image" (when triggered), with the function "open_image"
        self.actionOpen_Directory.triggered.connect(self.open_directory) # connecting the menu item "Open Directory" (when triggered), with the function "open_directory"
        self.pushButton_next.clicked.connect(self.next_image)
        self.pushButton_previous.clicked.connect(self.previous_image)
        
    def resizeEvent(self, event):
        try: # to avoid error when calling resizeEvent() before init() in which current_file is defined
            pixmap = QtGui.QPixmap(self.current_file)
        except:
            pixmap = QtGui.QPixmap("01.jpg")
        pixmap = pixmap.scaled(self.width(), self.height())
        self.label.setPixmap(pixmap)
        self.label.resize(self.width(), self.height())
    
    def open_image(self):
        options = QFileDialog.Options() # maybe options is not necessary 
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Image Files (*.png, *.jpg)", options = options)

        if filename != "":
            self.current_file = filename
            pixmap = QtGui.QPixmap(self.current_file)
            pixmap = pixmap.scaled(self.width(), self.height())
            self.label.setPixmap(pixmap)

    def open_directory(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.file_list = [directory + "/" + f for f in os.listdir(directory) if f.endswith(".png") or f.endswith(".jpg")]
        self.file_counter = 0
        self.current_file = self.file_list[self.file_counter]
        pixmap = QtGui.QPixmap(self.current_file)
        pixmap = pixmap.scaled(self.width(), self.height())
        self.label.setPixmap(pixmap)

    def next_image(self):
        if self.file_counter is not None:
            self.file_counter += 1
            self.file_counter %= len(self.file_list)  # to go back to the beginning of the list when reaching the end
            self.current_file = self.file_list[self.file_counter]
            pixmap = QtGui.QPixmap(self.current_file)
            pixmap = pixmap.scaled(self.width(), self.height())
            self.label.setPixmap(pixmap)            

    def previous_image(self):
        if self.file_counter is not None:
            self.file_counter -= 1
            self.file_counter %= len(self.file_list)  # to go back to the beginning of the list when reaching the end
            self.current_file = self.file_list[self.file_counter]
            pixmap = QtGui.QPixmap(self.current_file)
            pixmap = pixmap.scaled(self.width(), self.height())
            self.label.setPixmap(pixmap)            


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()

