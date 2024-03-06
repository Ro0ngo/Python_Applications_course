from PySide6.QtGui import Qt, QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget


class CounterApp(QMainWindow):
    def __init__(self):
        super(CounterApp, self).__init__()
        self.setWindowTitle("Программа-счётчик")

        self.counter = 0

        self.label = QLabel(str(self.counter), self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont("Times", 20)
        font.setBold(True)
        self.label.setFont(font)

        increase_button = QPushButton("Увеличить", self)
        increase_button.clicked.connect(self.increase_counter)

        reset_button = QPushButton("Сбросить", self)
        reset_button.clicked.connect(self.reset_counter)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(increase_button)
        layout.addWidget(reset_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def increase_counter(self):
        self.counter += 1
        self.label.setText(str(self.counter))

    def reset_counter(self):
        self.counter = 0
        self.label.setText(str(self.counter))


if __name__ == '__main__':
    app = QApplication([])
    window = CounterApp()
    window.setGeometry(400, 200, 600, 400)
    window.show()
    app.exec()
