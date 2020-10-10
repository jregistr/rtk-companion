from json import load as load_json
from typing import Dict, Optional

kanjis = None
KANJI_DATA_FN = "kanji_data.json"


def load_kanjis():
    global kanjis
    if kanjis is None:
        with open(KANJI_DATA_FN, "r") as kanji_db_json:
            kanjis = load_json(kanji_db_json)


def kanji_info_by_number(number: str) -> Optional[Dict[str, str]]:
    if kanjis is None:
        load_kanjis()

    if kanjis is not None:
        return next((x for x in kanjis if x["number"] == number), None)
    else:
        return None
