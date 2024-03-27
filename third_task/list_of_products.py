import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QLabel, QDoubleSpinBox, QPushButton


class ProductPurchase(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Покупка продуктов")
        self.setGeometry(300, 300, 300, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.products = {
            "Хлеб (1 шт)": 29.99,
            "Молоко (1 шт)": 59.99,
            "Яйца (1 шт)": 199.99,
            "Сыр (100 г)": 249.99,
            "Масло (1 шт)": 89.99
        }

        self.checkboxes = []
        self.spinboxes = []

        for product, price in self.products.items():
            checkbox = QCheckBox(f"{product} - {price:.2f} руб.")
            layout.addWidget(checkbox)
            self.checkboxes.append(checkbox)

            spinbox = QDoubleSpinBox()
            spinbox.setRange(0, 100)
            spinbox.setValue(0)
            spinbox.valueChanged.connect(self.update_price)
            layout.addWidget(spinbox)
            self.spinboxes.append(spinbox)

        self.total_label = QLabel("Общая стоимость: 0.00 руб.")
        layout.addWidget(self.total_label)

        calculate_button = QPushButton("Рассчитать")
        calculate_button.clicked.connect(self.calculate_total)
        layout.addWidget(calculate_button)

    def update_price(self):
        total = 0
        for checkbox, spinbox in zip(self.checkboxes, self.spinboxes):
            if checkbox.isChecked():
                product_name, product_price = checkbox.text().split(" - ")
                product_price = float(product_price.split()[0])
                quantity = spinbox.value()
                cost = product_price * quantity
                total += cost
            else:
                checkbox.setStyleSheet("")

        self.total_label.setText(f"Общая стоимость: {total:.2f} руб.")

    def calculate_total(self):
        total = 0
        for checkbox, spinbox in zip(self.checkboxes, self.spinboxes):
            if checkbox.isChecked():
                product_name, product_price = checkbox.text().split(" - ")
                product_price = float(product_price.split()[0])
                quantity = spinbox.value()
                cost = product_price * quantity
                total += cost
                checkbox.setStyleSheet("font-weight: bold;")
            else:
                checkbox.setStyleSheet("")

        self.total_label.setText(f"Общая стоимость: {total:.2f} руб.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductPurchase()
    window.show()
    sys.exit(app.exec())
