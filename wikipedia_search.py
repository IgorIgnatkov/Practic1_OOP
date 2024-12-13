import requests
import urllib.parse
import webbrowser

class WikipediaSearch:
    def __init__(self):
        self.base_url = "https://ru.wikipedia.org/w/api.php"

    def search_articles(self, query):
        encoded_query = urllib.parse.quote(query)
        search_url = f"{self.base_url}?action=query&list=search&utf8=&format=json&srsearch={encoded_query}"
        response = requests.get(search_url)
        data = response.json()
        return data['query']['search']

    def display_search_results(self, search_results):
        print("Результаты поиска:")
        for index, result in enumerate(search_results, start=1):
            print(f"{index}. {result['title']}")

    def open_article_page(self, page_id):
        article_url = f"https://ru.wikipedia.org/w/index.php?curid={page_id}"
        webbrowser.open(article_url)
