import re
import json

__re_p2ppl = re.compile(r' href="(https://xhamster.com/photos/gallery/\d+/\d+)"')
def page_to_pic_page_list(page: str):
    return __re_p2ppl.findall(page)


__re_pp2p = re.compile(r'window.initials = (.+?);')
def pic_page_to_pics(pic_page: str) -> list:
    return list([i['imageURL'] for i in json.loads(__re_pp2p.search(pic_page).groups(0)[0])['photosGalleryModel']['photos']['items']])