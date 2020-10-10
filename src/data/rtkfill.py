from aqt.editor import Editor
from anki.notes import Note
from aqt import mw, utils as anki_utils
from .heisigkanjis import kanji_info_by_number


MODEL_ID = 1593059310637


def maybe_fill_editor_rtk_data(editor: Editor):
    editor_note = editor.note
    if editor_note is not None:
        number_f_value = editor_note["Number"]
        if number_f_value:
            kanji_info = kanji_info_by_number(number_f_value)
            new_editor_note = new_note()
            new_editor_note["Number"] = number_f_value
            new_editor_note["Character"] = kanji_info["kanji"]
            new_editor_note["Keyword"] = kanji_info["keyword"]
            st_img_fn = kanji_info["stroke_order_fn"]
            new_editor_note["Stroke Order"] = '<img src="%s">' % st_img_fn
            editor.setNote(new_editor_note)
        else:
            anki_utils.showInfo("No Number value found", type="warning")
    else:
        anki_utils.showInfo("Editor Note is None", type="critical")


def new_note() -> Note:
    col = mw.col
    return Note(col, {"id": MODEL_ID}, None)
