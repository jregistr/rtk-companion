from aqt.editor import Editor


def add_button_web_btn(editor: Editor, btn_text: str, btn_id: str, cmd: str):
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
