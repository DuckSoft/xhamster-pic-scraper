# import time

# import requests

from xpdl.page import page_to_pic_page_list, pic_page_to_pics
from xpdl.search import *

sess = requests.Session()

# sess.proxies = {"http":"socks5://127.0.0.1:1080","https":"socks5://127.0.0.1:1080"}

search_page = keyword_to_search_page(sess, "korean teen")
url_list = search_page_to_url_list(search_page)

# pic_pages = [sess.get(url).content.decode() for url in url_list]
for u in url_list:

    pic_page = page_to_pic_page_list(sess.get(u).content.decode())
    for page in pic_page_to_pics(sess.get(pic_page[0]).content.decode()):
        print(page, flush=True)
        # with open("{:.0f}.jpg".format(time.time()), "bw") as f:
        #     f.write(sess.get(page).content)
        #     f.flush()
        #     f.close()
