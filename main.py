from wikipedia_search import WikipediaSearch

def main():
    wiki_search = WikipediaSearch()
    user_query = input("Введите поисковый запрос: ")
    search_results = wiki_search.search_articles(user_query)

    if not search_results:
        print("Ничего не найдено.")
        return

    wiki_search.display_search_results(search_results)

    try:
        user_choice = int(input("Введите номер статьи для открытия: "))
        if 1 <= user_choice <= len(search_results):
            selected_article = search_results[user_choice - 1]
            wiki_search.open_article_page(selected_article['pageid'])
        else:
            print("Неверный выбор.")
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число.")

if __name__ == "__main__":
    main()
