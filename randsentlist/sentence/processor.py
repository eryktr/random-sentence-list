class SentenceProcessor:
    def __init__(self):
        self._minimum_length = 30

    def _long_enough(self, sentence):
        return len(sentence) >= self._minimum_length

    def to_sentences(self, text):
        sentences = (sentence for sentence in text.split(".") if self._long_enough(sentence))
        return sorted(sentences, key=len, reverse=True)
