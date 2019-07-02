import logging
import random

from randsentlist.filename.filename import unique_filename
from randsentlist.latex.latex_writer import LatexWriter
from randsentlist.request.page_fetcher import PageFetcher
from randsentlist.sentence.processor import SentenceProcessor

_logger = logging.getLogger(__name__)


class ListGenerator:
    def __init__(self):
        self._writer = LatexWriter()
        self._fetcher = PageFetcher()
        self._processor = SentenceProcessor()

    def set_language(self, language):
        self._fetcher.set_language(language)

    def random_sentences_file(self, sentences_per_file, num_files):
        if sentences_per_file <= 0:
            raise ValueError("The number of sentences per file should be positive")
        if num_files <= 0:
            raise ValueError("The number of files should be positive")
        for _ in range(num_files):
            out_sentences = set()
            name = unique_filename()
            while len(out_sentences) < sentences_per_file:
                pages = self._fetcher.random_wiki_pages(sentences_per_file - len(out_sentences))
                _logger.info("Processing sentences...")
                sentences = [self._processor.to_sentences(page.content) for page in pages]
                _logger.info("Cherrypicking sentences...")
                picked = [sentence[random.randint(0, len(sentence) - 1)] for sentence in sentences if sentence]
                for sentence in picked:
                    if len(out_sentences) >= sentences_per_file:
                        break
                    out_sentences.add(sentence)
            _logger.info("Writing sentences to file...")
            self._writer.write_iterable_to_latex_file(out_sentences, name)
