from monitering.collect import collect_ranking, collect_news


def test_collect_ranking():
    result = collect_ranking()
    assert len(result) == 10

    for word in result:
        assert type(word) == str and word != ''
        news_titles, news_links = collect_news(word)

        assert len(news_titles) == 5
        assert len(news_links) == 5

        for i in range(0, 5):
            assert type(news_titles[i]) == str
            assert news_titles[i] != ''
            assert type(news_links[i]) == str
            assert news_links[i] != ''
            assert news_links[i][0:4] == 'http'

#
# def test_naver_main():
#     url = 'https://www.naver.com/'
#     selector = '#header > div.special_bg > div > div.logo_area > h1 > a > span'
#     result = crawling(url, selector)
#     naver = result[0].text
#     assert type(naver) == str
#     assert naver == '네이버'
