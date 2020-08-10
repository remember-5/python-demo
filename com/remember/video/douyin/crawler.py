import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from browsermobproxy import Server

if __name__ == '__main__':

    # 演示一下使用proxy抓network
    # https://github.com/lightbody/browsermob-proxy
    # 配置browsermob-proxy
    server = Server(r'/Users/wangjiahao/server/soft/browsermob-proxy-2.1.4/bin/browsermob-proxy')
    server.start()

    # 开始代理
    proxy = server.create_proxy()
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
    driver = webdriver.Chrome(chrome_options=chrome_options)

    video_url = "https://www.iesdouyin.com/share/user/3927074991252420?sec_uid=MS4wLjABAAAA_yPZkOcy2p9ZQW-7ZxsJY1iR2nSSR0zJXivrTlwQI18tjeoAq5E-wmr8s_Iagwsu&u_code=h620e5ii&app=aweme&utm_campaign=client_share&utm_medium=ios&tt_from=copy&utm_source=copy"
    proxy.new_har("douyin", options={'captureHeaders': True, 'captureContent': True})
    driver.get(video_url)

    result = proxy.har

    for entry in result['log']['entries']:
        _url = entry['request']['url']
        print(_url)
        # 根据URL找到数据接口
        if "/web/api/v2/aweme/iteminfo" in _url:
            _response = entry['response']
            _content = _response['content']['text']
            # 获取接口返回内容
            print(_content)

    server.stop()
    driver.quit()
