from aqt.qt import QLayout, QHBoxLayout, QVBoxLayout, QGridLayout, Qt
from aqt import qt


class KanjiFinder(QHBoxLayout):
    def __init__(self):
        super(KanjiFinder, self).__init__()
        self.setAlignment(Qt.AlignTop)

        scroller_layout, *_ = kanji_scroller()
        self.addLayout(scroller_layout)


def kanji_scroller():
    grid_layout = QGridLayout()
    search_field = qt.QLineEdit("Hello")
    grid_layout.addWidget(search_field, 0, 0, 1, 2)

    left_right_layout = QHBoxLayout()
    left_right_layout.setAlignment(Qt.AlignTop)
    grid_layout.addLayout(left_right_layout, 1, 0, 1, 2, Qt.AlignTop)

    left_btn = qt.QPushButton("<")
    right_btn = qt.QPushButton(">")
    left_right_layout.addWidget(left_btn, 0, Qt.AlignTop)
    left_right_layout.addWidget(right_btn, 0, Qt.AlignTop)

    search_btn = qt.QPushButton("Search")
    grid_layout.addWidget(search_btn, 2, 0, 1, 2, Qt.AlignTop)
    return grid_layout, search_field, left_btn, right_btn, search_btn


def kanji_desc():
    vbox = QVBoxLayout()
    vbox.setAlignment(Qt.AlignTop)
