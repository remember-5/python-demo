import requests
from lxml import etree

base_url = "https://test.ustc.edu.cn/"


def get_url(url):
    res = requests.get(url)
    if res.status_code == 200:
        x = etree.HTML(res.content)
        print(type(x))


if __name__ == '__main__':
    get_url(base_url)
