import json
import os

import requests


def download_file():
    # 读取文件
    json_data = {}
    with open('data.json', 'r', encoding='utf8')as fp:
        json_data = json.load(fp)
    print('这是文件中的json数据：', json_data)
    print('这是读取到文件数据的数据类型：', type(json_data))

    prefix_url = "http://gov.snkoudai.com/static/js/{key}.{value}.js"
    prefix_url_map = "http://gov.snkoudai.com/static/js/{key}.{value}.js.map"
    for k in json_data:
        # url = prefix_url.format(key=k,value=json_data[k])
        url_map = prefix_url_map.format(key=k,value=json_data[k])

        # res = requests.get(url)
        # with open('js/{}.{}.js'.format(k, json_data[k]), 'wb') as f:
        #     f.write(res.content)

        res_map = requests.get(url_map)
        with open('js/{}.{}.js.map'.format(k, json_data[k]), 'wb') as f:
            f.write(res_map.content)


def decode_file():
    path = "./js"  # 文件夹目录
    files = os.listdir(path)  # 得到文件夹下的所有文件名称
    s = []
    os.chdir("./js")
    for file in files:  # 遍历文件夹
        if not os.path.isdir(file) and file.find(".js.map") != -1:  # 判断是否是文件夹，不是文件夹才打开
            # print(file)
            # s.append(file)
            # os.system("cd js \r\n")
            # os.system("pwd")
            # print("reverse-sourcemap -v {0} -o sourcecode".format(file))
            os.system("reverse-sourcemap -v {0} -o sourcecode".format(file))
            # f = open(path + "/" + file);  # 打开文件
            # iter_f = iter(f);  # 创建迭代器
            # str = ""
            # for line in iter_f:  # 遍历文件，一行行遍历，读取文本
            #     str = str + line
            # s.append(str)  # 每个文件的文本存到list中

    print(len(s))  # 打印结果

if __name__ == '__main__':
    # download_file()
    decode_file()