from aqt.qt import QWidget, QHBoxLayout, QPushButton
from aqt.editor import Editor
from aqt.qt import QHBoxLayout, QVBoxLayout, QWidget, QLayout, QWebEngineView


class AddCardsKoohieBrowser(QWebEngineView):
    def __init__(self):
        super(AddCardsKoohieBrowser, self).__init__(parent=None)
        # self.load
        # layout = QHBoxLayout()
        # self.setLayout(layout)
        # layout.addWidget(QPushButton("Stuff"))
