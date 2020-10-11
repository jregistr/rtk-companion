from aqt.qt import QWidget, QHBoxLayout, QPushButton
from aqt.editor import Editor
from aqt.qt import QWebEngineView, QUrl

KOOHIE_URL = "https://kanji.koohii.com"


class AddCardsKoohieWebview(QWebEngineView):
    def __init__(self):
        super(AddCardsKoohieWebview, self).__init__(parent=None)

    def go_to_koohie(self):
        koohie_url = QUrl(KOOHIE_URL)
        self.load(koohie_url)

    def go_to_story(self, heisig_number: str):
        # Example URL: "https://kanji.koohii.com/study/kanji/700"
        url_str = "%s/study/kanji/%s" % (KOOHIE_URL, heisig_number)
        url = QUrl(url_str)
        self.load(url)
