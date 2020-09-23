from aqt import mw
from aqt.qt import QAction

from .controllers import RTKCompanionCTLR

parent = mw
rtk = RTKCompanionCTLR(parent)


def show_window():
    rtk.show()


action = QAction("Rtk Companion", mw)
action.triggered.connect(show_window)
mw.form.menuTools.addAction(action)
