import random
from multiprocessing.dummy import Pool as ThreadPool

import wikipedia


class PageFetcher:

    def random_wiki_page(self):
        title = ""
        while len(title) < 10:
            title = wikipedia.random(1)
        try:
            page = wikipedia.page(title)
        except wikipedia.DisambiguationError as e:
            options = [option for option in e.options if "(Disambiguation)" not in option
                       and "(disambiguation)" not in option
                       and e.title != option]
            s = random.choice(options)
            page = wikipedia.page(s)
        except wikipedia.PageError:
            page = wikipedia.page(wikipedia.random(1))
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
