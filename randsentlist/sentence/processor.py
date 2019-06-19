import re

from randsentlist.sentence.validator import Validator


class SentenceProcessor:
    def __init__(self):
        self._minimum_length = 30

    def _clean_hyperlinks(self, sentence):
        return re.sub("\[(.*?)\]", "", sentence)

    def to_sentences(self, text):
        sentences = [sentence for sentence in text.split(".") if Validator.is_valid_sentence(sentence)]
        sentences = list(map(self._clean_hyperlinks, sentences))
        sentences.sort(key=len, reverse=True)
        return sentences
