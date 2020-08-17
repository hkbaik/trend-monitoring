import sys
import threading
from collect import collect_ranking, collect_news
from esmodule import insert
from check import check_category
from extract import extract_keyword_textrank
from datetime import datetime


def run(elastic_search=True):
    date = datetime.utcnow()
    ranking = collect_ranking()
    docs = []

    for rank, word in enumerate(ranking):
        print(str(rank+1) + '   collecting')

        category, related_search_word = check_category(word)
        news_titles, news_links = collect_news(word)
        related_keyword = extract_keyword_textrank(word, news_links)

        doc = dict()
        doc['ranking'] = rank + 1
        doc['word'] = word
        doc['category'] = category
        doc['related_search_word'] = related_search_word
        doc['related_keyword'] = related_keyword
        doc['news_title'] = news_titles[0]
        doc['timestamp'] = date

        docs.append(doc)

    print(docs)

    if elastic_search:
        insert(docs)

    return docs


def repeat(elastic_search=True, interval_second=600):
    timer = threading.Timer(interval_second, run)
    timer.start()
    run(elastic_search)


if __name__ == '__main__':
    repeat(elastic_search=True)
