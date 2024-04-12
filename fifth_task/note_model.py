from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListView, \
    QLabel, QTabWidget
from PySide6.QtCore import Qt, QStringListModel


class NoteModel(QStringListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.notes = []

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.notes[index.row()]
        return None

    def rowCount(self, parent=None):
        return len(self.notes)

    def addNote(self, note):
        if note.strip():
            self.notes.append(note)
            self.setStringList(self.notes)

    def removeNotes(self, indexes):
        for index in sorted(indexes, reverse=True):
            del self.notes[index.row()]
        self.setStringList(self.notes)


class Product:
    def __init__(self, name, quantity, weight_per_unit):
        self.name = name
        self.quantity = quantity
        self.weight_per_unit = weight_per_unit

    def total_weight(self):
        return self.quantity * self.weight_per_unit


class ProductListModel(QStringListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.products = []

    def updateModel(self):
        data = []
        total_weight = 0
        for product in self.products:
            data.append(f"{product.name}: {product.quantity} шт, общий вес: {product.total_weight()} кг")
            total_weight += product.total_weight()
        data.append(f"Суммарный вес продуктов: {total_weight} кг")
        self.setStringList(data)

    def addProduct(self, product):
        self.products.append(product)
        self.updateModel()

    def removeProduct(self, row):
        del self.products[row]
        self.updateModel()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Заметки и продукты")
        layout = QVBoxLayout()

        tab_widget = QTabWidget()

        note_tab = QWidget()
        note_layout = QVBoxLayout()
        note_tab.setLayout(note_layout)

        self.note_input = QLineEdit()
        note_layout.addWidget(self.note_input)

        add_note_button = QPushButton("Добавить заметку")
        add_note_button.clicked.connect(self.addNote)
        note_layout.addWidget(add_note_button)

        self.remove_notes_button = QPushButton("Удалить выбранные заметки")
        self.remove_notes_button.clicked.connect(self.removeNotes)
        note_layout.addWidget(self.remove_notes_button)

        self.note_list = QListView()
        note_layout.addWidget(self.note_list)

        self.note_model = NoteModel()
        self.note_list.setModel(self.note_model)

        tab_widget.addTab(note_tab, "Заметки")

        product_tab = QWidget()
        product_layout = QVBoxLayout()
        product_tab.setLayout(product_layout)

        product_form_layout = QHBoxLayout()
        product_layout.addLayout(product_form_layout)

        product_form_layout.addWidget(QLabel("Название:"))
        self.product_name_input = QLineEdit()
        product_form_layout.addWidget(self.product_name_input)

        product_form_layout.addWidget(QLabel("Количество:"))
        self.product_quantity_input = QLineEdit()
        product_form_layout.addWidget(self.product_quantity_input)

        product_form_layout.addWidget(QLabel("Масса единицы продукта (кг):"))
        self.product_weight_input = QLineEdit()
        product_form_layout.addWidget(self.product_weight_input)

        add_product_button = QPushButton("Добавить продукт")
        add_product_button.clicked.connect(self.addProduct)
        product_layout.addWidget(add_product_button)

        self.remove_products_button = QPushButton("Удалить выбранные продукты")
        self.remove_products_button.clicked.connect(self.removeProducts)
        product_layout.addWidget(self.remove_products_button)

        self.product_list = QListView()
        product_layout.addWidget(self.product_list)

        self.product_model = ProductListModel()
        self.product_list.setModel(self.product_model)

        tab_widget.addTab(product_tab, "Продукты")

        layout.addWidget(tab_widget)

        self.setLayout(layout)

    def addNote(self):
        note = self.note_input.text()
        self.note_model.addNote(note)
        self.note_input.clear()

    def removeNotes(self):
        indexes = self.note_list.selectedIndexes()
        if indexes:
            self.note_model.removeNotes(indexes)

    def addProduct(self):
        name = self.product_name_input.text()
        quantity = int(self.product_quantity_input.text())
        weight_per_unit = float(self.product_weight_input.text())

        product = Product(name, quantity, weight_per_unit)
        self.product_model.addProduct(product)

        self.product_name_input.clear()
        self.product_quantity_input.clear()
        self.product_weight_input.clear()

    def removeProducts(self):
        indexes = self.product_list.selectedIndexes()
        if indexes:
            for index in indexes:
                self.product_model.removeProduct(index.row())


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
