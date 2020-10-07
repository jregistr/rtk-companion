from aqt import gui_hooks, mw, addcards
from aqt.addcards import AddCards
from aqt.editor import Editor
from aqt.fields import FieldDialog
from anki.hooks import wrap
from anki.cards import Card
from anki.notes import Note
from typing import List, Any, Callable


model_id = 1593059310637
deck_id = 1591395939518
collection = mw.col
# note = Note(collection, {"id": model_id}, None)


def html_buttons_call_back(info: List[Any]):
    with open("zooom-shaka.txt", "w", encoding="utf-8") as debug_fn:
        debug_fn.write("WOOOOOWW")
        debug_fn.flush()


def add_button(editor: Editor, btn_text: str, btn_id: str, cmd: str, callback: Callable[[List[Any]], None]):
    html_text = """
    (() => {
        document.getElementById('topbutsleft').innerHTML += `<button id='%s' onclick='pycmd("%s")'>%s</button> `; 
        return []
    })();
    """ % (btn_id, cmd, btn_text)

    editor.web.evalWithCallback(html_text, html_buttons_call_back)


def hook_for_editor_did_load_note(editor: Editor):
    if not editor.addMode:
        return
    add_button(editor, "Rtk", "rtk-btn", "run_fill_rtk", html_buttons_call_back)
    add_button(editor, "Koohie", "koohie-btn", "toggle_koohie", html_buttons_call_back)


def command_from_html_btn_bridge(editor: Editor, cmd: str):
    if cmd == "run_fill_rtk":
        maybe_add_cards: AddCards = editor.web.parent().parent()
        assert (isinstance(maybe_add_cards, AddCards))

        # with open("boom-shaka.txt", "a", encoding="utf-8") as debug_fn:
        #     debug_fn.write(cmd)
        #     debug_fn.write("yuuuups")
        #     debug_fn.write("\n")
        #     debug_fn.flush()
        #     editor_note = editor.note
        #     if editor.note:
        #         debug_fn.write("Alright, note exists, \n")
        #         editor_note.fields[0] = "foooBar"
        #         editor_note.fields[1] = "zzDooo"
        #         maybe_add_cards.form.fieldsArea.setStyleSheet("background-color:red;")
        #         # from pprint import pprint
        #         # varsz = dir(maybe_add_cards.form.fieldsArea)
        #         # pprint(varsz, debug_fn)

        def callback(info):
            with open("boom-shaka.txt", "a", encoding="utf-8") as debug_fn:
                debug_fn.write(str(info))
                debug_fn.flush()

        js = """
                (() => {
                var fields_inner = document.getElementById('fields').innerHTML; 
                return fields_inner
                })();
                """
        editor.web.evalWithCallback(js, callback)
        # fields = editor_note.fields
        # first_value = str(fields[0])
        # debug_fn.write(first_value)

    elif cmd == "toggle_koohie":
        pass


gui_hooks.editor_did_load_note.append(hook_for_editor_did_load_note)
Editor.onBridgeCmd = wrap(Editor.onBridgeCmd, command_from_html_btn_bridge)
