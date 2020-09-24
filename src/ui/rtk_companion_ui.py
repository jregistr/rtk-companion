from aqt.qt import QDialog, QDialogButtonBox, Qt, QSize, QVBoxLayout
from aqt.utils import showInfo
from .kanji_finder_ui import KanjiFinder


# class MainWindow(QDialog):
#     def __init__(self):
#         super().__init__(None, Qt.Window)

# class MyDialog(object):
#     def setupUi(self, Dialog):
#         Dialog.setObjectName("Dialog")
#         Dialog.resize(400, 300)
#         self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
#         self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
#         self.buttonBox.setOrientation(QtCore.Qt.Vertical)
#         self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
#         self.buttonBox.setObjectName("buttonBox")
#
#         self.retranslateUi(Dialog)
#         self.buttonBox.accepted.connect(Dialog.accept)
#         self.buttonBox.rejected.connect(Dialog.reject)
#         QtCore.QMetaObject.connectSlotsByName(Dialog)
#
#     def retranslateUi(self, Dialog):
#         _translate = QtCore.QCoreApplication.translate
#         Dialog.setWindowTitle(_translate("Dialog", "MyFirstPyQtProgramm With Designer Tool"))
#         Dialog.show()


class RTKCompanionUI(object):
    def __init__(self, companion_window):
        companion_window.setObjectName("RTK Companion")
        companion_window.resize(1000, 900)
        companion_window.setMinimumSize(QSize(500, 450))
        companion_window.setAutoFillBackground(False)
        self.vbox_layout = QVBoxLayout(companion_window)

        finder = KanjiFinder()
        self.vbox_layout.addLayout(finder)

    # def setupUi(self, dialog):
    #     dialog.setObjectName("Dialog")
    #     dialog.resize(400, 300)
    #     self.buttonBox = QDialogButtonBox(dialog)
    #     self.buttonBox.setGeometry(QRect(290, 20, 81, 241))
    #     self.buttonBox.setOrientation(Qt.Vertical)
    #     self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
    #     self.buttonBox.setObjectName("buttonBox")
