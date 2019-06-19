import re


class SentenceProcessor:
    def __init__(self):
        self._minimum_length = 30

    def _long_enough(self, sentence):
        return len(sentence) >= self._minimum_length

    def _is_not_equation(self, sentence: str):
        return not any(c in sentence for c in ["\\", "=", "+", "-", "*", "/", ":"])

    def _is_single_line(self, sentence: str):
        return "\n" not in sentence

    def _is_valid_sentence(self, sentence):
        return self._long_enough(sentence) and self._is_not_equation(sentence) and self._is_single_line(sentence)

    def _clean_hyperlinks(self, sentence):
        return re.sub("\[(.*?)\]", "", sentence)

    def to_sentences(self, text):
        sentences = [sentence for sentence in text.split(".") if self._is_valid_sentence(sentence)]
        sentences = list(map(self._clean_hyperlinks, sentences))
        sentences.sort(key=len, reverse=True)
        return sentences
