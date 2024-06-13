import re
import time


import requests

import sqlite_utils

channel = "30010005"
# 101 主卡 201副卡
card_type = "10100002"
# 身份证
cert_id = "220802198307261517"


def get_sale_groups():
    """
    get sale groups
    """
    url = "https://m.sh.189.cn/business-api/yunKd/getSalesGroupsv2"

    payload = {
        "channel": "30010005",
        "publishstatus": "2",
        "shelvesType": "号卡"
    }

    headers = {
        "Host": "m.sh.189.cn",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "code": "ea0a67cebec122c5a0fe8fc3582f89ebd8839ed2f1f8dda5d120c225",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 NetType/WIFI MicroMessenger/6.8.0(0x16080000) MacWechat/3.8(0x13080012) XWEB/30515 Flue",
        "Origin": "https://m.sh.189.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://m.sh.189.cn/spahgo/aggregate_page/aggregate_page.html?authTime=1717737431",
        "Accept-Language": "en",
        "Content-Type": "application/json",
        "Cookie": "business-api=YmE0ZDI4ZjktZDRmMi00NTE0LWI0YzItNmViMDhkMzY3NTMz; infoepoch.go=beff34ac8142042743cbe2efd40997ea; _gscu_1708861450=97698774fln4tq59; Hm_lvt_15f3a5c5bd043f9dcee10253e2032754=1717737430; SHOP-JSESSION-ID=Yzg4NTY3ZjEtOTI4MC00ZWIxLWJhYjktODA3YjE3OWZhMmQ1; zhizhendata2015jssdkcross=%7B%22distinct_id%22%3A%22MThjYWEzZjViNzNkNDEtMDZmZjRjMzNmOGZhMDdjLTc0N2I1MTVjLTIwNzM2MDAtMThjYWEzZjViNzRkZDE%3D%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22_latest_utm_ch%22%3A%22wx%22%2C%22_latest_utm_sd1%22%3A%2217600277246%22%2C%22_latest_utm_sd2%22%3A%22412722199805077730%22%7D%2C%22login_type%22%3A%22%22%2C%22utms%22%3A%7B%7D%2C%22latest_utms%22%3A%7B%22_latest_utm_ch%22%3A%22wx%22%2C%22_latest_utm_sd1%22%3A%2217600277246%22%2C%22_latest_utm_sd2%22%3A%22412722199805077730%22%7D%2C%22%24device_id%22%3A%2218caa3f5b73d41-06ff4c33f8fa07c-747b515c-2073600-18caa3f5b74dd1%22%7D; Hm_lpvt_15f3a5c5bd043f9dcee10253e2032754=1717738592"
    }

    return requests.request("POST", url, json=payload, headers=headers)


def get_phone_by_sale_id(query_sale, page=1):
    url = "https://emall.sh.189.cn/shop/number/pool/search"

    payload = {
        "saleId": query_sale,
        "channel": channel,
        "certId": cert_id,
        "cartType": "1",
        "countryId": "",
        "count": 0,
        "cardType": card_type,
        "page": page,
        "searchKey": ""
    }
    headers = {
        "Host": "emall.sh.189.cn",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 NetType/WIFI MicroMessenger/6.8.0(0x16080000) MacWechat/3.8(0x13080012) XWEB/30515 Flue",
        "token": "80261b65f88db829403a659b4dd8ecd4",
        "Origin": "https://emall.sh.189.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://emall.sh.189.cn/mall/",
        "Accept-Language": "en",
        "Content-Type": "application/json",
        "Cookie": "_gscu_1708861450=97698774fln4tq59; SHOP-JSESSION-ID=Yzg4NTY3ZjEtOTI4MC00ZWIxLWJhYjktODA3YjE3OWZhMmQ1; zhizhendata2015jssdkcross=%7B%22distinct_id%22%3A%22MThjYWEzZjViNzNkNDEtMDZmZjRjMzNmOGZhMDdjLTc0N2I1MTVjLTIwNzM2MDAtMThjYWEzZjViNzRkZDE%3D%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22_latest_utm_ch%22%3A%22wap%22%2C%22_latest_utm_sd1%22%3A%22%22%2C%22_latest_utm_sd2%22%3A%22412722199805077730%22%7D%2C%22login_type%22%3A%22%22%2C%22utms%22%3A%7B%7D%2C%22latest_utms%22%3A%7B%22_latest_utm_ch%22%3A%22wap%22%2C%22_latest_utm_sd1%22%3A%22%22%2C%22_latest_utm_sd2%22%3A%22412722199805077730%22%7D%2C%22%24device_id%22%3A%2218caa3f5b73d41-06ff4c33f8fa07c-747b515c-2073600-18caa3f5b74dd1%22%7D"
    }

    return requests.request("POST", url, json=payload, headers=headers)


class HaoKa:
    def __init__(self):
        self.db = sqlite_utils.Database("telecom_phone.db")

    def init_table(self):
        """
        init database table
        """
        self.init_sale_table()
        self.init_phone_pool_table()

    def init_sale_table(self):
        if self.db["sale"].exists() is False:
            self.db.execute(
                """
                create table sale
                    (
                        id          integer not null
                            constraint table_name_pk
                                primary key autoincrement,
                        sale_id     integer not null,
                        sale_name   TEXT    not null,
                        url         TEXT    not null,
                        query_sale  integer,
                        create_time TEXT
                    );
                """
            )

    def init_phone_pool_table(self):
        if self.db["phone_pool"].exists() is False:
            self.db.execute(
                """
                create table phone_pool
                    (
                        phone       integer not null
                            constraint phone_pool_pk
                                unique,
                        sale_id     integer not null,
                        create_time TEXT
                    );
                """
            )

    def get_sale(self):
        response = get_sale_groups()
        if response.status_code == 200 and response.json()['status'] == 200:
            for item in response.json()['data']:
                for group in item['groupSales']:
                    pattern = r"/(\d+)\.html"
                    sale_id, sales_name, submit_href_url = group['saleId'], group['salesName'], group[
                        'submitHrefUrl']
                    match = re.search(pattern, submit_href_url)
                    print(sale_id, sales_name, submit_href_url, "none" if match is None else match.group(1))
                    self.db.execute("delete from sale where sale_id = ?", (sale_id,))
                    self.db['sale'].insert(
                        {
                            'sale_id': sale_id,
                            'sale_name': sales_name,
                            'url': submit_href_url,
                            'query_sale': "" if match is None else match.group(1),
                            'create_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        }
                    )
        print("获取套餐失败")

    def get_phone_number(self, sale_id, query_sale, page=1):
        response = get_phone_by_sale_id(query_sale, page)
        if response.status_code == 200 and response.json()['code'] == 200:
            for p in response.json()['data']['numbers']:
                phone = p['id']
                if self.db.execute("select * from phone_pool where phone = ?", [phone]).fetchone() is None:
                    self.db['phone_pool'].insert({
                        'sale_id': sale_id,
                        'phone': phone,
                        'create_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    })
                    print('sale_id %s query_sale %s phone %s added' % sale_id, query_sale, phone)
                else:
                    print('sale_id %s query_sale %s phone %s already exists' % sale_id, query_sale, phone)
        if page + 1 < 100:
            self.get_phone_number(sale_id, query_sale, page + 1)

    def get_phone(self):
        for sale in self.db.query("select * from sale"):
            self.get_phone_number(sale['sale_id'], sale['query_sale'])

    def close_db(self):
        self.db.close()


if __name__ == '__main__':
    haoka = HaoKa()
    haoka.init_table()
    # haoka.get_sale()
    haoka.get_phone()
    haoka.close_db()
