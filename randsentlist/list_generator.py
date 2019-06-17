from randsentlist.filename.filename import unique_filename
from randsentlist.latex.latex_writer import LatexWriter
from randsentlist.request.page_fetcher import PageFetcher
from randsentlist.sentence.processor import SentenceProcessor


class ListGenerator:
    def __init__(self):
        self._writer = LatexWriter()
        self._fetcher = PageFetcher()
        self._processor = SentenceProcessor()

    def set_language(self, language):
        self._fetcher.set_language(language)

    def random_sentences_file(self, sentences_per_file, num_files):
        for _ in range(num_files):
            sentences = set()
            name = unique_filename()
            while len(sentences) < sentences_per_file:
                pages = self._fetcher.random_wiki_pages(sentences_per_file)
                longest_sentences = [self._processor.to_sentences(page.content)[0] for page in pages]
                for sentence in longest_sentences:
                    sentences.add(sentence)
            self._writer.write_iterable_to_latex_file(sentences, name)
