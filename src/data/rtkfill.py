from typing import Dict
from aqt.editor import Editor
from anki.notes import Note
from anki.collection import Collection
from aqt import utils as anki_utils
from . import heisigkanjis
from .heisigkanjis import KEY_KEYWORD, KEY_NUMBER, KEY_KANJI
from ..ui import AddCardsKoohieWebview


def maybe_fill_editor_rtk_data(col: Collection, editor: Editor, stories_view: AddCardsKoohieWebview):
    editor_note = editor.note
    if editor_note is not None:
        number_f_value = editor_note["Number"]
        if number_f_value:
            kanji_info = heisigkanjis.kanji_info_by_number(number_f_value)
            if kanji_info is not None:
                new_editor_note = kanji_info_to_note(kanji_info, editor_note.mid, col)
                editor.setNote(new_editor_note)
                if stories_view.isVisible():
                    stories_view.go_to_story(number_f_value)
            else:
                anki_utils.showInfo("Could not find kanji info for heisig number: %s" %
                                    number_f_value)
        else:
            anki_utils.showInfo("No Number value found", type="warning")
    else:
        anki_utils.showInfo("Editor Note is None", type="critical")


def kanji_info_to_note(kanji_info: Dict, note_id: int, col: Collection) -> Note:
    new_note = Note(col, {"id": note_id})
    stroke_order = None
    try:
        stroke_order = heisigkanjis.get_stroke_order_frame(kanji_info, col)
    except Exception:
        anki_utils.showWarning("Unable to determine stroke order image")

    new_note["Number"] = kanji_info[KEY_NUMBER]
    new_note["Character"] = kanji_info[KEY_KANJI]
    new_note["Keyword"] = kanji_info[KEY_KEYWORD]
    if stroke_order is not None:
        new_note["Stroke Order"] = '<img src="%s">' % stroke_order

    return new_note
