from pathlib import Path
from typing import List, Set

from unidecode import unidecode

from word_ending_finder.vie_data import DATA


class WordEnding:
    def __init__(self, data: List[str] = DATA) -> None:
        self.data = data

    def get_words(self, word_ending: str, exact: bool = True) -> Set[str]:
        out = []
        for x in self.data:
            if exact:
                if x[::-1][: len(word_ending)][::-1] == word_ending:
                    try:
                        out.append(x.split()[-1])
                    except:
                        out.append(x)
            else:
                temp = unidecode(word_ending)
                if temp[::-1][: len(word_ending)][::-1] == word_ending:
                    try:
                        out.append(x.split()[-1])
                    except:
                        out.append(x)
        return set(out)
