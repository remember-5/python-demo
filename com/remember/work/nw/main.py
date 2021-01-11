import json
import requests


def run():
    # 读取文件
    json_data = {}
    with open('data.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
    print('这是文件中的json数据：', json_data)
    print('这是读取到文件数据的数据类型：', type(json_data))

    prefix_url = "http://gov.snkoudai.com/static/js/{key}.{value}.js"
    prefix_url_map = "http://gov.snkoudai.com/static/js/{key}.{value}.js.map"
    for k in json_data:
        url = prefix_url.format(key=k,value=json_data[k])
        url_map = prefix_url_map.format(key=k,value=json_data[k])

        res = requests.get(url)
        with open('js/{}.{}.js'.format(k, json_data[k]), 'wb') as f:
            f.write(res.content)

        res_map = requests.get(url_map)
        with open('js/{}.{}.js.map'.format(k, json_data[k]), 'wb') as f:
            f.write(res_map.content)

if __name__ == '__main__':
    run()
