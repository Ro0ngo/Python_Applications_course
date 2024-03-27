import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QDateEdit, QTextEdit, QPushButton
from PySide6.QtCore import QDate, QDateTime


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Расчет возраста")
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.birth_date_edit = QDateEdit()
        self.birth_date_edit.setCalendarPopup(True)
        self.birth_date_edit.setDate(QDate.currentDate())
        layout.addWidget(QLabel("Дата рождения:"))
        layout.addWidget(self.birth_date_edit)

        calculate_button = QPushButton("Рассчитать")
        calculate_button.clicked.connect(self.calculate_age)
        layout.addWidget(calculate_button)

        self.result_textedit = QTextEdit()
        self.result_textedit.setReadOnly(True)
        layout.addWidget(self.result_textedit)

    def calculate_age(self):
        birth_date = self.birth_date_edit.date()
        current_datetime = QDateTime.currentDateTime()

        age_seconds = birth_date.daysTo(current_datetime.date()) * 24 * 60 * 60

        age_years = age_seconds // (365 * 24 * 60 * 60)
        age_seconds %= (365 * 24 * 60 * 60)
        age_hours = age_seconds // (60 * 60)
        age_seconds %= (60 * 60)

        result_text = f"Возраст: {age_years} лет\n"
        result_text += f"Возраст: {age_hours} часов\n"
        result_text += f"Возраст: {age_seconds} секунд"

        self.result_textedit.setText(result_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AgeCalculator()
    window.show()
    sys.exit(app.exec())
