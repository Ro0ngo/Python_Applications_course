from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, \
    QLineEdit
from PySide6.QtCore import Qt


class CalculatorApp(QMainWindow):
    def __init__(self):
        super(CalculatorApp, self).__init__()
        self.setWindowTitle("Простой калькулятор")

        self.num1_input = QLineEdit(self)
        self.num2_input = QLineEdit(self)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.num1_input)
        input_layout.addWidget(self.num2_input)

        add_button = QPushButton("+", self)
        add_button.clicked.connect(lambda: self.calculate('+'))

        subtract_button = QPushButton("-", self)
        subtract_button.clicked.connect(lambda: self.calculate('-'))

        multiply_button = QPushButton("*", self)
        multiply_button.clicked.connect(lambda: self.calculate('*'))

        divide_button = QPushButton("/", self)
        divide_button.clicked.connect(lambda: self.calculate('/'))

        power_button = QPushButton("Возведение в степень", self)
        power_button.clicked.connect(self.calculate_power)

        button_layout = QHBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(subtract_button)
        button_layout.addWidget(multiply_button)
        button_layout.addWidget(divide_button)
        button_layout.addWidget(power_button)

        self.result_label = QLabel("", self)
        font = QFont("Times", 20)
        font.setBold(True)
        self.result_label.setFont(font)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.result_label)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def calculate(self, operation):
        operation_str = ""
        result = ""
        num1 = int(self.num1_input.text())
        num2 = int(self.num2_input.text())

        match operation:
            case "*":
                result = num1 * num2
                operation_str = "*"
            case "+":
                result = num1 + num2
                operation_str = "+"
            case "-":
                result = num1 - num2
                operation_str = "-"
            case "/":
                result = num1 / num2
                operation_str = "/"

        self.result_label.setText(f"{num1} {operation_str} {num2} = {result}")

    def calculate_power(self):
        num1 = int(self.num1_input.text())
        num2 = int(self.num2_input.text())

        result = num1 ** num2
        self.result_label.setText(f"{num1} <sup>{num2}</sup> = {result}")


if __name__ == '__main__':
    app = QApplication([])
    window = CalculatorApp()
    window.setGeometry(400, 200, 300, 200)
    window.show()
    app.exec()
