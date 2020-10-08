from typing import Dict


kanjis = [
    {
        "number": "700",
        "kanji": "抗",
        "keyword": "confront",
        "stroke_order_fn": "paste-20dda0b5f63d565af1113dadb168c58336f1cfc0.jpg"
    },
    {
        "number": "701",
        "kanji": "批",
        "keyword": "criticism",
        "stroke_order_fn": "paste-21de3cb1b4bcf42f503ba65b77ea1b219de9ef08.jpg"
    },
    {
        "number": "702",
        "kanji": "招",
        "keyword": "beckon",
        "stroke_order_fn": "paste-25a37d1c0add01a52adf777de15756f9eb352b19.jpg"
    },
    {
        "number": "703",
        "kanji": "拓",
        "keyword": "clear the land",
        "stroke_order_fn": "paste-31dffe009e71554dd18e6f824dd1aab5b195933f.jpg"
    },
    {
        "number": "704",
        "kanji": "拍",
        "keyword": "clap",
        "stroke_order_fn": "paste-44b50bfd3adbc3672bec0a5a469383e313bc8275.jpg"
    }
]


def kanji_info_by_number(number: str) -> Dict[str, str]:
    return next((x for x in kanjis if x["number"] == number), None)
