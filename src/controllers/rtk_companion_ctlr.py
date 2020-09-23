from aqt.qt import QDialog
from ..ui import RTKCompanionUI


class RTKCompanionCTLR(QDialog):
    def __init__(self, parent_widget):
        super(RTKCompanionCTLR, self).__init__(parent_widget,)
        self.ui = RTKCompanionUI()
        self.ui.setupUi(self)
