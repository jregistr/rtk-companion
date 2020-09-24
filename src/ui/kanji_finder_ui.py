from aqt.qt import QHBoxLayout, QGridLayout, QWidget, QPushButton, QLineEdit


class KanjiFinder(QHBoxLayout):
    def __init__(self):
        super(KanjiFinder, self).__init__()
        search_scroll_layout = QGridLayout()
        self.addLayout(search_scroll_layout)

        search_field = QLineEdit("Hello")
        search_field.resize(200, 50)
        search_scroll_layout.addWidget(search_field, 0, 0, 1, 2)
