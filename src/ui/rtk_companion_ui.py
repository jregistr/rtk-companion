from aqt.qt import QDialog, QVBoxLayout
from aqt import qt
from aqt.utils import showInfo
from .kanji_finder_ui import KanjiFinder


class RTKCompanionUI(object):
    def __init__(self, companion_window: QDialog):
        companion_window.setObjectName("RTK Companion")
        # companion_window.resize(1000, 900)
        # companion_window.setMinimumSize(QSize(500, 450))
        # companion_window.setAutoFillBackground(False)
        outer_layout = QVBoxLayout()
        companion_window.setLayout(outer_layout)

        finder = KanjiFinder()
        outer_layout.addLayout(finder)
