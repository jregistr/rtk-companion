from aqt import gui_hooks, mw as main_window
from aqt.editor import Editor
from aqt.addcards import AddCards
from aqt import utils
from anki.hooks import wrap
from anki.notes import Note
from .ui.components import add_button_web_btn
from aqt.qt import QHBoxLayout, QVBoxLayout, QWidget, QLayout, QPushButton, QUrl, QWebEngineView
from .ui import dockable_widget
from .ui import AddCardsKoohieBrowser
from .data import heisigkanjis
from pprint import pprint


CMD_RTK_FILL = "run_fill_rtk"
CMD_STORIES_TOGGLE = "toggle_stories"

stories_browser = None
stories_browser_displayed = False


def cb_editor_did_load_note_hook(editor: Editor):
    if editor.addMode:
        add_button_web_btn(editor, "RTK", "rtk-btn", CMD_RTK_FILL)
        add_button_web_btn(editor, "Stories", "rtk-stories", CMD_STORIES_TOGGLE)
        global stories_browser
        if stories_browser is None:

            add_cards: AddCards = editor.web.parent().parent()
            assert(isinstance(add_cards, AddCards))
            old_add_cards_layout = add_cards.layout()
            new_vbox = QVBoxLayout()

            while old_add_cards_layout.count() > 0:
                ui_obj = old_add_cards_layout.takeAt(0)
                if ui_obj.widget() is None or isinstance(ui_obj, QLayout):
                    new_vbox.addLayout(ui_obj.layout())
                else:
                    new_vbox.addWidget(ui_obj.widget())

            trash = QWidget()
            trash.setLayout(old_add_cards_layout)
            fill_widget = QWidget()
            fill_widget.setLayout(new_vbox)

            new_add_cards_layout = QHBoxLayout()
            new_add_cards_layout.setContentsMargins(0, 0, 0, 0)
            new_add_cards_layout.setSpacing(0)
            new_add_cards_layout.addWidget(fill_widget, 2)
            add_cards.setLayout(new_add_cards_layout)

            browser_layout = QHBoxLayout()
            new_add_cards_layout.addLayout(browser_layout)

            # web = QWebEngineView()
            # web.load(QUrl("https://google.com"))
            stories_browser = AddCardsKoohieBrowser()
            stories_browser.load(QUrl("https://kanji.koohii.com/"))
            browser_layout.addWidget(stories_browser, 10)


def cb_editor_unfocused_field_hook(changed: bool, editor_note: Note, cur_fid: int):
    number_value_string = editor_note["Number"]
    if number_value_string:
        kanji_info = heisigkanjis.kanji_info_by_number(number_value_string)
        editor_note["Character"] = kanji_info["kanji"]
        editor_note["Keyword"] = kanji_info["keyword"]
        st_img_fn = kanji_info["stroke_order_fn"]
        editor_note["Stroke Order"] = '<img src="%s">' % st_img_fn
        return True
    else:
        return False


def cb_command_from_js_bridge(editor: Editor, cmd: str):
    if cmd == CMD_RTK_FILL:
        pass
    elif cmd == CMD_STORIES_TOGGLE:
        add_cards: AddCards = editor.web.parent().parent().parent()
        assert(isinstance(add_cards, AddCards))
        # some_note = Note(main_window.col, editor.note.mo)
        # edin["Character"] = "ZZZ Foobar"
        model_id = 1593059310637
        note = Note(main_window.col, {"id": model_id}, None)
        note["Character"] = "Goobar"
        img_str = "paste-44b50bfd3adbc3672bec0a5a469383e313bc8275.jpg"
        note["Stroke Order"] = '<img src="%s">' % img_str
        editor.setNote(note)

        # edin = editor.note
        # edin.fields[0] = "Super Foobar"
        # with open("_debug_file.txt", "a") as debug_fn:
        #     debug_fn.write("FOO")
        #     if edin is not None:
        #         debug_fn.write("Not None")
        #         bla = edin["Character"]
        #         debug_fn.write(str(bla))
        #     else:
        #         debug_fn.write("It was None")
        #         utils.showInfo("It was None")


        # add_cards = editor.web.parent().parent().parent()
        #
        # with open("_debug_file.txt", "a") as debug_fn:
        #     t = str(type(add_cards))
        #     debug_fn.write(t)
        #     inf = dir(add_cards)
        #     pprint(inf, debug_fn)
        #



gui_hooks.editor_did_load_note.append(cb_editor_did_load_note_hook)
# gui_hooks.editor_did_unfocus_field.append(cb_editor_unfocused_field_hook)
Editor.onBridgeCmd = wrap(Editor.onBridgeCmd, cb_command_from_js_bridge)
# dockable_widget.add_dock(main_window)
