class URLShortener:
    def __init__(self):
        self.urls = {}
        self.counter = 1

    def shorten(self, url):
        short = f"short.ly/{self.counter}"
        self.urls[short] = url
        self.counter += 1
        return short

    def expand(self, short_url):
        return self.urls.get(short_url)
