import wikipedia


class PageFetcher:

    def random_wiki_page(self):
        return wikipedia.page(wikipedia.random(1)[1])

    def random_wiki_pages(self, num_pages):
        cache = []
        found = 0
        while found < num_pages:
            page = self.random_wiki_page()
            if page not in cache:
                cache.append(page)
                found += 1
        return cache

    def set_language(self, language):
        if language not in wikipedia.languages():
            raise ValueError(f"{language} is not a valid language code or it is not supported")
        wikipedia.set_lang(language)
