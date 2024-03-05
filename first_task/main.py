from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from book import Book


class Window(QMainWindow):
    def __init__(self, books):
        super().__init__()
        self.setWindowTitle('Books Information')

        self.books = books

        self.label = QLabel("", self)
        self.label.setMinimumWidth(self.width())
        self.label.setMinimumHeight(self.height())
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setMargin(10)
        font = QFont("Times", 12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setWordWrap(True)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(60, 50, self.width(), self.height())
        self.image_label.hide()

        self.btn = QPushButton(self)
        self.btn.setText('Show Book Info')
        self.btn.move(250, 500)
        self.btn.clicked.connect(self.show_book_info)

    def show_book_info(self):
        if self.books:
            book = self.books.pop(0)
            info_str = book.get_info_string()
            pixmap = QPixmap(f"{book.cover_filename}")
            self.image_label.setPixmap(pixmap)
            self.image_label.show()
            self.label.setText(info_str)
            self.label.show()
        else:
            self.label.setText("No more books to display.")
            self.image_label.hide()


if __name__ == '__main__':
    app = QApplication([])
    book1 = Book("Практикум по курсу обыкновенных дифференциальных уравнений", "С.Д.Глызин, А.О.Толбей", 67,
                 "differential_equations.jpg")
    book2 = Book("Элементы теории множеств и математической логики", "Л.Ю.Белова, В.А.Башкин, Ю.А.Белов", 78,
                 "math_logic.jpg")
    biblioteka = [book1, book2]
    window = Window(biblioteka)
    window.setGeometry(430, 200, 600, 600)
    window.show()
    app.exec()
