from aqt import gui_hooks, mw as main_window
from aqt.editor import Editor
from aqt import utils
from anki.hooks import wrap
from anki.notes import Note
from .ui.components import add_button
from .data import heisigkanjis


CMD_RTK_FILL = "run_fill_rtk"
CMD_STORIES_TOGGLE = "toggle_stories"


def cb_editor_did_load_note_hook(editor: Editor):
    if editor.addMode:
        add_button(editor, "RTKz", "rtk-btn", CMD_RTK_FILL)
        add_button(editor, "Stories", "rtk-stories", CMD_STORIES_TOGGLE)


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
        pass


gui_hooks.editor_did_load_note.append(cb_editor_did_load_note_hook)
gui_hooks.editor_did_unfocus_field.append(cb_editor_unfocused_field_hook)
Editor.onBridgeCmd = wrap(Editor.onBridgeCmd, cb_command_from_js_bridge)
