from os import path
from aqt.qt import QWebEngineView, QUrl
from ..project import support_files_path

KOOHIE_URL = "https://kanji.koohii.com"
TRIM_SCRIPT_FN = "trimStoriesPage.js"


def load_trim_script():
    trim_js_fn = path.join(support_files_path, TRIM_SCRIPT_FN)
    with open(trim_js_fn, "r", encoding="utf-8") as js_file:
        return js_file.read()


class AddCardsKoohieWebview(QWebEngineView):
    def __init__(self):
        super(AddCardsKoohieWebview, self).__init__(parent=None)
        self.trim_page_script = load_trim_script()
        self.loadFinished.connect(self.page_finished_loading)

    def go_to_koohie(self):
        koohie_url = QUrl(KOOHIE_URL)
        self.load(koohie_url)

    def trim_story_page(self):
        script = self.trim_page_script
        story_page = self.page()
        story_page.runJavaScript(script)

    def go_to_story(self, heisig_number: str):
        # Example URL: "https://kanji.koohii.com/study/kanji/700"
        url_str = "%s/study/kanji/%s" % (KOOHIE_URL, heisig_number)
        url = QUrl(url_str)
        self.load(url)

    def page_finished_loading(self):
        page_url: QUrl = self.url()
        page_url_str: str = page_url.toString()
        find_sub = page_url_str.find("/study/kanji/")
        if find_sub != -1:
            self.trim_story_page()
