import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QLabel


class SeasonInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Информация о временах года")
        self.setGeometry(300, 300, 300, 150)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.spring_radio = QRadioButton("Весна")
        self.summer_radio = QRadioButton("Лето")
        self.autumn_radio = QRadioButton("Осень")
        self.winter_radio = QRadioButton("Зима")

        self.spring_radio.setChecked(True)

        self.spring_radio.toggled.connect(self.display_info)
        self.summer_radio.toggled.connect(self.display_info)
        self.autumn_radio.toggled.connect(self.display_info)
        self.winter_radio.toggled.connect(self.display_info)

        layout.addWidget(self.spring_radio)
        layout.addWidget(self.summer_radio)
        layout.addWidget(self.autumn_radio)
        layout.addWidget(self.winter_radio)

        self.info_label = QLabel()
        layout.addWidget(self.info_label)

        self.display_info()

    def display_info(self):
        if self.spring_radio.isChecked():
            self.info_label.setText("Весна - время расцвета природы и пробуждения после зимы.")
        elif self.summer_radio.isChecked():
            self.info_label.setText("Лето - время яркого солнца, отпусков и отдыха на природе.")
        elif self.autumn_radio.isChecked():
            self.info_label.setText("Осень - время урожая, красивых осенних листьев и прохладных вечеров.")
        elif self.winter_radio.isChecked():
            self.info_label.setText("Зима - время снегопадов, новогодних праздников и зимних видов спорта.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SeasonInfo()
    window.show()
    sys.exit(app.exec())
