from aqt.qt import QWidget, QHBoxLayout, QPushButton
from aqt.editor import Editor
from aqt.qt import QWebEngineView, QUrl


class AddCardsKoohieWebview(QWebEngineView):
    def __init__(self):
        super(AddCardsKoohieWebview, self).__init__(parent=None)

    def go_to_koohie(self):
        koohie_url = QUrl("https://kanji.koohii.com/")
        self.load(koohie_url)
