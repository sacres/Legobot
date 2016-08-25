import requests
from Lego import Lego


class WikipediaTopFinder(Lego):
    def listening_for(self, message):
        return message['text'].split()[0] == '!wtf'

    def handle(self, message):
        baseurl = 'https://en.wikipedia.org/w/index.php?search='
        search_params = '%20'.join(message['text'].split()[1:])
        r = requests.get(baseurl + search_params)
        if r.status_code == 200:
            return "I found this: " + r.url
        else:
            return "I could not reach Wikipedia. Sorry."
