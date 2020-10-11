from typing import Dict, Optional
from json import load as load_json
from os import path
from ..project import support_files_path
from zipfile import ZipFile
from aqt.utils import showWarning
from anki.collection import Collection

kanjis = None
KANJI_DATA_FN = "kanji_data.json"
KANJI_STRK_ZIP_FN = "stroke-orders.zip"

KEY_NUMBER = "number"
KEY_KANJI = "kanji"
KEY_KEYWORD = "keyword"
KEY_STROKE_ORDR = "stroke_order_fn"


def load_kanjis():
    global kanjis
    if kanjis is None:
        kanjis_fn_path = path.join(support_files_path, KANJI_DATA_FN)
        with open(kanjis_fn_path, "r", encoding="utf-8") as kanji_db_json:
            kanjis = load_json(kanji_db_json)


def kanji_info_by_number(number: str) -> Optional[Dict[str, str]]:
    if kanjis is None:
        load_kanjis()

    if kanjis is not None:
        return next((x for x in kanjis if x["number"] == number), None)
    else:
        return None


def get_stroke_order_frame(kanji_info: Dict[str, str], col: Collection) -> Optional[str]:
    strk_fn = kanji_info[KEY_STROKE_ORDR]
    if strk_fn is not None:
        zip_fn = path.join(support_files_path, KANJI_STRK_ZIP_FN)
        try:
            with ZipFile(zip_fn, "r") as strk_zip:
                stroke_order_bytes = strk_zip.read(strk_fn)
                media_frame = col.media.writeData(strk_fn, stroke_order_bytes)
                return media_frame
        except FileNotFoundError:
            showWarning("Stroke order zip file not found at: %s" % zip_fn)
        except KeyError:
            showWarning("Looks like the stroke order image file %s is not in the archeive" % strk_fn)
    else:
        return None
