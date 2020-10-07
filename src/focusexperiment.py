from aqt import gui_hooks, mw, addcards
from aqt.addcards import AddCards
from aqt.editor import Editor
from aqt.fields import FieldDialog
from anki.hooks import wrap
from anki.cards import Card
from anki.notes import Note
from typing import List, Any, Callable


def add_button(editor: Editor, btn_text: str, btn_id: str, cmd: str, callback: Callable[[List[Any]], None]):
    html_text = """
    (() => {
        document.getElementById('topbutsleft').innerHTML += `<button id='%s' onclick='pycmd("%s")'>%s</button> `; 
        return []
    })();
    """ % (btn_id, cmd, btn_text)

    editor.web.evalWithCallback(html_text, callback)


def html_buttons_call_back(info: List[Any]):
    pass


def hook_for_editor_did_load_note(editor: Editor):
    if not editor.addMode:
        return
    add_button(editor, "Rtk", "rtk-btn", "run_fill_rtk", html_buttons_call_back)
    add_button(editor, "Koohie", "koohie-btn", "toggle_koohie", html_buttons_call_back)


def command_from_html_btn_bridge(editor: Editor, cmd: str):
    pass


def on_focus_was_lost(flag, editor_n, fidx):
    editor_n[fidx] = "Fooobar woooah wow, okay"
    with open("boom-shaka-bug.txt", "a", encoding="utf-8") as debug_fn:
        debug_fn.write(str(type(flag)))
        debug_fn.write(str(type(editor_n)))
        debug_fn.write(str(type(fidx)))
        debug_fn.flush()


gui_hooks.editor_did_load_note.append(hook_for_editor_did_load_note)
Editor.onBridgeCmd = wrap(Editor.onBridgeCmd, command_from_html_btn_bridge)
gui_hooks.editor_did_unfocus_field.append(on_focus_was_lost)
