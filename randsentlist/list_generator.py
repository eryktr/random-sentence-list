from randsentlist.latex.latex_writer import LatexWriter
from randsentlist.request.page_fetcher import PageFetcher
from randsentlist.sentence.processor import SentenceProcessor


class ListGenerator:
    def __init__(self, num_sentences):
        self._num_sentences = num_sentences
        self._writer = LatexWriter("tmp")
        self._fetcher = PageFetcher()
        self._processor = SentenceProcessor()
