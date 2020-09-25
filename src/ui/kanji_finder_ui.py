from aqt.qt import QHBoxLayout, QVBoxLayout, QGridLayout, Qt
from aqt import qt


class KanjiFinder(QHBoxLayout):
    def __init__(self):
        super(KanjiFinder, self).__init__()
        self.setAlignment(Qt.AlignTop)

        scroller_layout, *_ = kanji_scroller()
        desc_kanji, *_ = kanji_desc()

        self.addLayout(scroller_layout)
        self.addLayout(desc_kanji)


def kanji_scroller():
    grid_layout = QGridLayout()
    search_field = qt.QLineEdit()
    grid_layout.addWidget(search_field, 0, 0, 1, 2)

    left_right_layout = QHBoxLayout()
    left_right_layout.setContentsMargins(0, 0, 0, 0)

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
    top, meaning, number, upsert = kanji_desc_top()

    vbox.addLayout(top)
    return vbox, meaning, number, upsert


def kanji_desc_top():
    top_line = QHBoxLayout()
    top_line.setAlignment(Qt.AlignTop)

    meaning_label = qt.QLabel()
    meaning_label.setText("Younger Sister")
    # meaning_label.resize(150, 50)
    meaning_label.setMinimumWidth(150)
    meaning_label.setFixedHeight(50)

    number_label = qt.QLabel()
    number_label.setText("231")
    number_label.resize(30, 50)

    upsert_btn = qt.QPushButton("Add")
    upsert_btn.setFixedHeight(50)
    upsert_btn.setMinimumWidth(100)

    top_line.addWidget(meaning_label)
    top_line.addWidget(number_label)
    top_line.addWidget(upsert_btn, 0, Qt.AlignRight)
    return top_line, meaning_label, number_label, upsert_btn
