from aqt import mw
from aqt.utils import showInfo
from aqt.qt import QAction
from typing import Sequence
import anki.backend_pb2 as pb

debug_file_name = "./rtk-debug.txt"


def test_function():
    decks = mw.col.decks
    ids_names = decks.all_names_and_ids(True)
    names = [pair.name for pair in ids_names]
    as_string = '\n'.join(names)
    as_string = as_string.join("\n-----------------\n")

    my_models = mw.col.models
    model_ids_names = my_models.all_names_and_ids()
    model_names = [pair.name for pair in model_ids_names]
    # model_names = model_names[0:10]
    model_names_string = '\n'.join(model_names)

    with open(debug_file_name, "w") as debug_fn:
        debug_fn.write(model_names_string)
        debug_fn.flush()

    # f = open("BoomShaka.txt", "w")
    # f.write(model_names_string)

    # as_string = as_string.join(model_names_string)

    # showInfo("%s" % as_string)


action = QAction("Rtk Companion", mw)
action.triggered.connect(test_function)
mw.form.menuTools.addAction(action)
