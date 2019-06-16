import re

class SentenceProcessor:
    def __init__(self):
        self._minimum_length = 30

    def _long_enough(self, sentence):
        return len(sentence) >= self._minimum_length

    def _clean_hyperlinks(self, sentence):
        return re.sub("\[(.*?)\]", "", sentence)

    def to_sentences(self, text):
        sentences = [sentence for sentence in text.split(".") if self._long_enough(sentence)]
        sentences = list(map(self._clean_hyperlinks, sentences))
        sentences.sort(key=len, reverse=True)
        return sentences
