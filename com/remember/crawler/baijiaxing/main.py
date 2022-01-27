# 发起请求
import requests
# 解析报文
from bs4 import BeautifulSoup


# 1. 获取网站返回信息
base_url = "http://tools.2345.com"
baijiaxing_url = "http://tools.2345.com/baijx/"

# 2. 向网站发起一个请求
baijiaxing_rsp = requests.get(baijiaxing_url)

# 3. 判定状态码，如果状态码是200，就代表请求成功
if baijiaxing_rsp.status_code == 200:
    # 格式化html
    bs = BeautifulSoup(baijiaxing_rsp.content, 'html.parser')
    # 寻找所有到a标签，因为姓氏和地址都在a标签里
    ass = bs.find(id="xdiv").find_all("a")
    # 这个是百家姓到列表，结构是
    # 赵 = /baijx/1.htm
    # 钱 = /baijx/2.htm
    # 可以用bjx_list['赵'] 来获取姓氏到请求地址
    bjx_list = {}

    # 这里是解析a标签到
    for a in ass:
        # 这个就是a标签里到姓氏文字
        bjx = a.contents[0]
        # 这个是a标签里的跳转地址
        href = a['href']
        # 保存两个属性到bjx_list里面，形成结构化
        bjx_list[bjx] = base_url + href

    print(bjx_list)

    print("====以上全部是解析过程====")

    print("开始爬数据")

    url = bjx_list['贾']
    print("贾=", url)
    # 开始爬"赵" 的页面信息，首先发起一个请求到赵到页面上
    surname = requests.get(url)
    # 判定返回结果状态码是不是200
    if surname.status_code == 200:
        # 如果进了if，就代表请求成功了
        print("请求页面成功，开始获取数据")
        # 先格式化html代码
        surname_html = BeautifulSoup(surname.content,"html.parser")
        # 然后打印一下，查看是不是正确
        # print(surname_html)

        items = surname_html.find_all(attrs="dectxt_item")
        for item in items:
            print(item.text)













