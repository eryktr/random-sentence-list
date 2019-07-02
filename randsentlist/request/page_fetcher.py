import logging
from multiprocessing.dummy import Pool as ThreadPool

import wikipedia

_logger = logging.getLogger(__name__)


class PageFetcher:

    def random_wiki_page(self):
        title = ""
        while len(title) < 10:
            title = wikipedia.random(1)
        return wikipedia.page(title)

    def _random_wiki_page(self, task_id):
        for attempt in range(1, 11):
            try:
                _logger.info(f"Thread {task_id} fetching a page ")
                page = self.random_wiki_page()
                _logger.info(f"Thread {task_id} has fetched its page.")
                return page
            except:
                _logger.info(f"Thread {task_id}: failed for the {attempt} time.")

    def random_wiki_pages(self, num_pages):
        pool = ThreadPool(20)
        results = pool.map(self._random_wiki_page, [i for i in range(num_pages)])
        return results

    def set_language(self, language):
        _logger.info(f"Setting language to {language}")
        if language not in wikipedia.languages():
            raise ValueError(f"{language} is not a valid language code or it is not supported")
        wikipedia.set_lang(language)
        _logger.info(f"Language has been set to {language}")
