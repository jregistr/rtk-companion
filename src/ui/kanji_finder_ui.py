from aqt.qt import QHBoxLayout, QVBoxLayout, QGridLayout, Qt
from aqt import qt


class KanjiFinder(QVBoxLayout):
    def __init__(self):
        super(KanjiFinder, self).__init__()
        self.setAlignment(Qt.AlignTop)
        self.addLayout(kanji_scroll_display_add(self))
        self.addLayout(kanji_additional_info(self))


# <editor-fold desc="Kanji Scroll, Kanji info Display, and Additional Kanji info">
def kanji_scroll_display_add(finder: KanjiFinder) -> qt.QLayout:
    layout = QHBoxLayout()
    layout.addLayout(kanji_scroll_search(finder), 1)
    layout.addLayout(kanji_summary_group(finder), 5)
    return layout


def kanji_additional_info(finder: KanjiFinder) -> qt.QLayout:
    layout = QHBoxLayout()
    layout.setContentsMargins(8, 0, 8, 0)

    # Create Widgets
    finder.primitives_label = qt.QLabel()
    finder.more_meanings_label = qt.QLabel()

    # Set widget properties / style
    finder.primitives_label.setStyleSheet("font-size: 20px")
    finder.more_meanings_label.setStyleSheet("font-size: 20px")

    # Add MVP placeholders
    finder.primitives_label.setText("冖 女 巾 ヨ")
    finder.more_meanings_label.setText("Freer, Lady, Siting, Relax, Foobar")

    # Add to layout
    layout.addWidget(finder.primitives_label, 3, Qt.AlignLeft)
    layout.addWidget(finder.more_meanings_label, 6, Qt.AlignRight)
    return layout


def kanji_scroll_search(finder: KanjiFinder) -> qt.QLayout:
    layout = QGridLayout()

    # Create widgets
    finder.search_box = qt.QLineEdit()
    finder.left_btn = qt.QPushButton("<<")
    finder.right_btn = qt.QPushButton(">>")
    finder.search_btn = qt.QPushButton("Search")

    # Set widget properties / style
    finder.search_box.setStyleSheet("text-align: center;")

    # Add to layout
    layout.addWidget(finder.search_box, 0, 0, 1, 2)
    layout.addWidget(finder.left_btn, 1, 0)
    layout.addWidget(finder.right_btn, 1, 1)
    layout.addWidget(finder.search_btn, 2, 0, 1, 2)
    return layout


def kanji_summary_group(finder: KanjiFinder) -> qt.QLayout:
    # 12 cell grid
    layout = QGridLayout()

    # Create widgets
    finder.kanji_keyword = qt.QLabel()
    finder.kanji_hnumber = qt.QLabel()
    finder.add_update_btn = qt.QPushButton("Add")
    finder.kanji_display = qt.QLabel()
    finder.kanji_user_story = qt.QPlainTextEdit()

    # Widget properties / style
    finder.kanji_user_story.setMinimumWidth(600)
    finder.kanji_user_story.setMaximumHeight(100)
    finder.kanji_display.setStyleSheet("font-size: 100px")

    # Set MVP placeholders
    finder.kanji_user_story.setPlainText("""Lorem ipssimply dummy text of the printing and typesetting industry. Lorem Ipsum has been the 
industry’s standard dummy text ever since the 1500s. when an unknown printer took a galley of type 
and scrambled it to make a type specimen book. It has survived not only five centuries, but also 
the leap into electronic typesetting, remaining essentially unchanged.""")
    finder.kanji_display.setText("婦")
    finder.kanji_keyword.setText("Younger Sister")
    finder.kanji_hnumber.setText("231")

    # Add to layout
    layout.addWidget(finder.kanji_keyword, 0, 0, 1, 4)
    layout.addWidget(finder.kanji_hnumber, 0, 5)
    layout.addWidget(finder.add_update_btn, 0, 8, 1, 4)
    layout.addWidget(finder.kanji_display, 1, 0, 2, 2)
    layout.addWidget(finder.kanji_user_story, 1, 3, 2, 9)
    return layout
# </editor-fold>

# <editor-fold desc="Kanji Stroke Order">

# </editor-fold>
