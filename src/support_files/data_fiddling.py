import json
import re


def asci_to_unicode_and_dump():
    json_array = ""
    with open("kanji_data.json") as json_file:
        json_array = json.load(json_file)

    with open("kanji_data.json", "w") as json_file:
        json.dump(json_array, json_file, ensure_ascii=False)


# Let's capitalize all keywords like they are titles
def capilize_like_titles_and_dump():
    json_array = ""
    with open("kanji_data.json") as json_file:
        json_array = json.load(json_file)
        for kanji_info in json_array:
            keyword = kanji_info["keyword"]
            keyword = str.title(keyword)
            regex = '(A|The|Of|Yet|Or|On|To|In|For|By|And|An|But|Either|Neither|At|As)(?![a-zA-Z])'
            keyword = re.sub(regex, '{}',
                             keyword).format(*map(str.lower, re.findall(regex, keyword)))
            first = str.upper(keyword[0:1])
            rest = keyword[1:]
            keyword = first + rest

            words = keyword.split()
            if len(words) > 1:
                last_capped = str.capitalize(words[-1])
                together = " ".join(words[:-1])
                keyword = together + " " + last_capped

            kanji_info["keyword"] = keyword

    with open("kanji_data.json", "w") as json_file:
        json.dump(json_array, json_file, ensure_ascii=False)


capilize_like_titles_and_dump()
