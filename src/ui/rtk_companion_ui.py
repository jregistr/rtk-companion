from aqt.qt import QDialog, QDialogButtonBox, Qt, QRect
from aqt.utils import showInfo


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
    def setupUi(self, dialog):
        dialog.setObjectName("Dialog")
        dialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
