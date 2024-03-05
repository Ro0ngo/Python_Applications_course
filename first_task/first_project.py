from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('First project')

        self.label = QLabel("Hello my wonderful Wooooooooooooooooooooooooooooooooooooooooooooooooooorld!", self)
        self.label.setMinimumWidth(self.width())
        self.label.setMinimumHeight(self.height())
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setMargin(10)
        font = QFont("Times", 12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.main_text = QLabel("qweqweqwe", self)
        self.main_text.move(220, 500)
        my_font = QFont("Times", 24)
        self.main_text.setFont(my_font)
        self.main_text.setMargin(10)
        self.main_text.adjustSize()
        self.main_text.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)

        self.image_label = QLabel(self)
        pixmap = QPixmap('image.jpg')
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(50, 50, self.width() - 150, self.height())
        self.image_label.hide()

        self.btn = QPushButton(self)
        self.btn.setText('Press me')
        self.btn.move(250, 250)
        self.btn.clicked.connect(self.press_btn)

    def press_btn(self):
        self.label.hide()
        self.btn.hide()
        self.main_text.hide()
        self.image_label.show()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.setGeometry(430, 200, 600, 600)
    window.show()
    app.exec()
