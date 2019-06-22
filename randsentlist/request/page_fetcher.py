from multiprocessing.dummy import Pool as ThreadPool

import wikipedia


class PageFetcher:

    def random_wiki_page(self):
        title = ""
        while len(title) < 10:
            title = wikipedia.random(1)
        try:
            page = wikipedia.page(title)
        except wikipedia.DisambiguationError:
            page = self.random_wiki_page()
        except wikipedia.PageError:
            page = self.random_wiki_page()
        return page

    def _random_wiki_page(self, task_id):
        return self.random_wiki_page()

    def random_wiki_pages(self, num_pages):
        pool = ThreadPool(20)
        results = pool.map(self._random_wiki_page, [i for i in range(num_pages)])
        return results

    def set_language(self, language):
        if language not in wikipedia.languages():
            raise ValueError(f"{language} is not a valid language code or it is not supported")
        wikipedia.set_lang(language)
