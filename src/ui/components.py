from aqt.editor import Editor
from typing import List, Any, Callable


def add_button(editor: Editor, btn_text: str, btn_id: str, cmd: str):
    html_text = """
    (() => {
        var btn = document.getElementById('%s');
        if (!btn) {
            document.getElementById('topbutsleft').innerHTML += `<button id='%s' onclick='pycmd("%s")'>%s</button> `;
        }
        return []
    })();
    """ % (btn_id, btn_id, cmd, btn_text)

    editor.web.evalWithCallback(html_text, lambda _: None)
