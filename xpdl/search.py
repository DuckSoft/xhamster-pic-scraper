import requests
import re


def keyword_to_search_page(sess: requests.Session, keywords: str) -> str:
    return sess.get(url="https://xhamster.com/search/photos", params={"q": keywords}).content.decode()


__re_sp2ul = re.compile(r'href="(https://xhamster.com/photos/gallery/.+?)"')
def search_page_to_url_list(page: str):
    return __re_sp2ul.findall(page)

