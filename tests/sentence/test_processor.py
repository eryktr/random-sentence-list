from randsentlist.sentence.processor import SentenceProcessor


class TestProcessor:
    def setup_method(self):
        self.processor = SentenceProcessor()

    def test_long_enough(self):
        passing = "The quick brown fox jumps over the lazy dog"
        failing = "Shame, indeed"
        assert self.processor._long_enough(passing)
        assert not self.processor._long_enough(failing)

    def test_clean_hyperlins(self):
        hyperlinked = "The man[1], standing next to my aunt[21], is his uncle[999]"
        cleaned = self.processor._clean_hyperlinks(hyperlinked)
        assert cleaned == "The man, standing next to my aunt, is his uncle"
