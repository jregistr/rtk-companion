from aqt.qt import QDialog, Qt
from ..ui import RTKCompanionUI


class RTKCompanionCTLR(QDialog):
    def __init__(self, parent_widget):
        flags = Qt.Window \
                | Qt.CustomizeWindowHint\
                | Qt.WindowCloseButtonHint\
                | Qt.WindowFullscreenButtonHint\
                | Qt.WindowMinimizeButtonHint

        super(RTKCompanionCTLR, self).__init__(parent_widget, flags)
        # self.setModal(True)
        self.ui = RTKCompanionUI(self)
