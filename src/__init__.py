from aqt import mw
from aqt.utils import showInfo
from aqt.qt import QAction
from typing import Sequence
import anki.backend_pb2 as pb
from anki.cards import Card
from anki.notes import Note
from anki.decks import DeckManager
from shutil import copyfile
from . import project
from os import path

debug_file_name = "./rtk-debug.txt"


def test_function():
    col = mw.col
    model_id = 1593059310637
    deck_id = 1591395939518
    # col.models.all_names_and_ids()
    # deck = col.decks.byName("Experimenting")
    # media_dir = mw.col.media.dir()
    # support_dir = project.support_files
    #
    # cat_img = path.join(support_dir, "octocat.png")
    # copyfile(cat_img, path.join(media_dir, "octocat.png"))

    note = Note(col, {"id": model_id}, None)
    note.fields[0] = "カファばカファば"
    note.fields[1] = "A kafaba keyword"
    # ゆ-bw.png
    note.fields[2] = "120"
    note.fields[3] = "The amazing story about the Ka character is amazing."
    note.fields[4] = '<img src="octocat.png">'

    col.add_note(note, deck_id)
    col.save()
    mw.deckBrowser.refresh()


# def test_function():
#     # Study RTK-2dff4 -----> 1593059310637 <- model id
#     # Experimenting   -----> 1591395939518 <- deck
#     col = mw.col
#     model_id = 1593059310637
#     fronts = []
#     for cid in col.find_notes("mid:1593059310637"):
#         note = col.getNote(cid)
#         front = note.fields[0]
#         fronts_string = '\n'.join(fronts)
#         cards = note.cards()
#         card: Card = cards[0]
#
#
#         fronts.append(front)
#
#
#     with open(debug_file_name, "w", encoding="utf-8") as debug_fn:
#         debug_fn.write(fronts_string)
#         debug_fn.write("--------------------------------=-=-=\n\n")


# def test_function():
#     mw.addonManager.getConfig(__name__)
#     decks = mw.col.decks
#     ids_names = decks.all_names_and_ids(True)
#     names = [' ------- '.join([pair.name, str(pair.id)]) for pair in ids_names]
#     as_string = '\n'.join(names)
#     as_string = as_string.join("\n-----------------\n")
#
#     my_models = mw.col.models
#     model_ids_names = my_models.all_names_and_ids()
#     model_names = [' -----> '.join([pair.name, str(pair.id)]) for pair in model_ids_names]
#     # model_names = model_names[0:10]
#     model_names_string = '\n'.join(model_names)
#
#     with open(debug_file_name, "w") as debug_fn:
#         debug_fn.write(as_string)
#         debug_fn.write("--------------------------------=-=-=\n\n")
#
#         debug_fn.write(model_names_string)
#         debug_fn.flush()
#
#     # f = open("BoomShaka.txt", "w")
#     # f.write(model_names_string)
#
#     # as_string = as_string.join(model_names_string)
#
#     # showInfo("%s" % as_string)


action = QAction("Rtk Companion", mw)
action.triggered.connect(test_function)
mw.form.menuTools.addAction(action)
