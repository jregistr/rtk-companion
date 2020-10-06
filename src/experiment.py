from aqt import gui_hooks
from aqt.editor import Editor
from anki.hooks import wrap
from typing import List, Any, Callable


def html_buttons_call_back(info: List[Any]):
    pass


def add_button(editor: Editor, btn_text: str, btn_id: str, cmd: str, callback: Callable[[List[Any]], None]):
    html_text = """
    (() => {
        let rendered = false;
        if (!document.getElementById('%s')) {
            document.getElementById('topbutsleft').innerHTML += `<button id='%s' onclick='pycmd("%s")'>%s</button> `; 
        } else {
            rendered = true;
        }
        return [rendered];
    })();
    """ % (btn_id, btn_id, cmd, btn_text)

    editor.web.evalWithCallback(html_text, callback)


def hook_for_editor_did_load_note(editor: Editor):
    if not editor.addMode:
        return
    add_button(editor, "Rtk", "rtk-btn", "run_fill_rtk", html_buttons_call_back)
    add_button(editor, "Koohie", "koohie-btn", "toggle_koohie", html_buttons_call_back)


def command_from_html_btn_bridge(editor: Editor.onBridgeCmd, cmd: str):
    pass


gui_hooks.editor_did_load_note.append(hook_for_editor_did_load_note)
Editor.onBridgeCmd = wrap(Editor.onBridgeCmd, command_from_html_btn_bridge)
