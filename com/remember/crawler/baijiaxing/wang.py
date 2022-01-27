import requests
from bs4 import BeautifulSoup

base_url = "http://tools.2345.com"
baijiaxing_url = "http://tools.2345.com/baijx/"


def get_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, "html.parser")


def get_surname_info(name, url):
    text = get_url(url).find_all(attrs="conm_box dectxt")[0].text
    print(text)


for a in get_url(baijiaxing_url).find(id="xdiv").find_all("a"):
    get_surname_info(a.contents[0], base_url + a['href'])
