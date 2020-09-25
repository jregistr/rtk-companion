from aqt.qt import QHBoxLayout, QGridLayout, Qt, QPushButton, QLineEdit


class KanjiFinder(QHBoxLayout):
    def __init__(self):
        super(KanjiFinder, self).__init__()
        self.setAlignment(Qt.AlignTop)

        scroller_layout, *_ = kanji_scroller()
        self.addLayout(scroller_layout)


def kanji_scroller():
    grid_layout = QGridLayout()
    search_field = QLineEdit("Hello")
    grid_layout.addWidget(search_field, 0, 0, 1, 2)

    left_right_layout = QHBoxLayout()
    left_right_layout.setAlignment(Qt.AlignTop)
    grid_layout.addLayout(left_right_layout, 1, 0, 1, 2)

    left_btn = QPushButton("<")
    right_btn = QPushButton(">")
    left_right_layout.addWidget(left_btn, 0)
    left_right_layout.addWidget(right_btn, 0)

    search_btn = QPushButton("Search")
    grid_layout.addWidget(search_btn, 2, 0, 1, 2)
    return grid_layout, search_field, left_btn, right_btn, search_btn
