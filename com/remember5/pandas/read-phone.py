import json
import os

import pandas as pd


def traverse_files(folder_path):
    list1 = []
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                # 处理文件内容，例如打印或进行其他操作
                list1.append(content)
    return list1


if __name__ == '__main__':
    phones = []

    excel_path = '/Users/wangjiahao/Downloads/phone.xlsx'
    file_path = '/Users/wangjiahao/Downloads/weixin.sd.189.cn_7443/mall-portal/xiaobai/order'
    list1 = traverse_files(file_path)
    for x in list1:
        json_obj = json.loads(x)
        data = json_obj['data']
        if data is not None:
            data = json.loads(data)
            for p in data:
                phoneNumber = p['phoneNumber']
                phones.append(phoneNumber)

    data = {
        "phone": phones,
    }
    df = pd.DataFrame(data, columns=["phone"])
    df.to_excel(excel_path)
