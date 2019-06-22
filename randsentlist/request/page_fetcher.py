import random
import threading

import wikipedia


class PageFetcher:
    LOCK = threading.Lock()

    def random_wiki_page(self):
        title = ""
        while len(title) < 10:
            title = wikipedia.random(1)
        try:
            page = wikipedia.page(title)
        except wikipedia.DisambiguationError as e:
            options = [option for option in e.options if "(Disambiguation)" not in option]
            s = random.choice(options)
            page = wikipedia.page(s)
        except wikipedia.PageError:
            page = wikipedia.page(wikipedia.random(1))
        return page

    def _fetch_page(self, cache):
        while True:
            page = self.random_wiki_page()
            PageFetcher.LOCK.acquire()
            print(len(cache))
            if page not in cache:
                cache.append(page)
                PageFetcher.LOCK.release()
                break
            PageFetcher.LOCK.release()

    def random_wiki_pages(self, num_pages):

        cache = []
        threads = [threading.Thread(target=self._fetch_page, args=(cache,)) for _ in range(num_pages)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        return cache

    def set_language(self, language):
        if language not in wikipedia.languages():
            raise ValueError(f"{language} is not a valid language code or it is not supported")
        wikipedia.set_lang(language)
