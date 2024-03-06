from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("You won't be able to click on me.")

        self.label = QLabel("Кнопка Отпущена", self)
        self.label.setFixedSize(300, 50)
        font = QFont("Times", 20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setGeometry(190, 100, self.width(), self.height())

        self.btn = QPushButton(self)
        self.btn.setCheckable(True)
        self.btn.setText("Попробуй нажать")
        self.btn.move(215, 400)
        self.btn.setFixedSize(200, 50)
        self.btn.pressed.connect(self.onButtonPressed)
        self.btn.released.connect(self.onButtonReleased)
        self.btn.setStyleSheet(
            "QPushButton{"
            "background-color: lightblue;"
            "border: 2px solid;"
            "border-radius: 7px;"
            "}"
            "QPushButton:hover{"
            "background-color: lightgreen;"
            "}"
            "QPushButton:pressed{"
            "background-color: lightcoral;"
            "}"
        )

    def onButtonPressed(self):
        self.label.setText("Кнопка нажата")

    def onButtonReleased(self):
        self.label.setText("Кнопка отпущена")


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.setGeometry(430, 200, 600, 600)
    window.show()
    app.exec()
