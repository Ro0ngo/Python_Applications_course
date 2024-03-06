from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("You won't be able to click on me.")

        self.label = QLabel("Отпущена", self)
        self.QFont("Times", 20)

        self.btn = QPushButton(self)
