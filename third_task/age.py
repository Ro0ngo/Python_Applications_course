import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDateTimeEdit, QTextEdit, QPushButton
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QDateTime


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Расчет возраста")

        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        window_width = 300
        window_height = 200
        window_x = screen_geometry.width() // 2 - window_width // 2
        window_y = screen_geometry.height() // 2 - window_height // 2

        self.setGeometry(window_x, window_y, window_width, window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.birth_date_edit = QDateTimeEdit()
        self.birth_date_edit.setDisplayFormat("yyyy.MM.dd hh:mm")
        self.birth_date_edit.setCalendarPopup(True)
        self.birth_date_edit.setDateTime(QDateTime.currentDateTime())
        layout.addWidget(QLabel("Дата рождения:"))
        layout.addWidget(self.birth_date_edit)

        calculate_button = QPushButton("Рассчитать")
        calculate_button.clicked.connect(self.calculate_age)
        layout.addWidget(calculate_button)

        self.result_textedit = QTextEdit()
        self.result_textedit.setReadOnly(True)
        layout.addWidget(self.result_textedit)

    def calculate_age(self):
        birth_datetime = self.birth_date_edit.dateTime()
        current_datetime = QDateTime.currentDateTime()

        age_seconds = birth_datetime.secsTo(current_datetime)

        age_years = age_seconds // (365 * 24 * 60 * 60)
        age_seconds %= (365 * 24 * 60 * 60)
        age_hours = age_seconds // (60 * 60)
        age_seconds %= (60 * 60)
        age_minutes = age_seconds // 60
        age_seconds %= 60

        result_text = f"Лет: {age_years}\n"
        result_text += f"Часов: {age_hours}\n"
        result_text += f"Минут: {age_minutes}\n"
        result_text += f"Секунд: {age_seconds}"

        self.result_textedit.setText(result_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AgeCalculator()
    window.show()
    sys.exit(app.exec())
