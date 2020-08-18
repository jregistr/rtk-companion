from aqt import mw
from aqt.utils import showInfo
from aqt.qt import QAction


def test_function():
    card_count = mw.col.cardCount()
    showInfo("Number of Cards: %d" % card_count)


action = QAction("Rtk Companion", mw)
action.triggered.connect(test_function)
mw.form.menuTools.addAction(action)