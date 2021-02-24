import time
import random

import pymysql

db = pymysql.connect("192.168.161.189", "root", "123456", "spring_boot_demo")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

desc_list = ['搜索医院', '查看医院详情', '访问首页', '医院导航']
method_list = ['search', 'details', 'index', 'navigation']
search_word = [
    '松江',
    '中心',
    '第一',
    '妇幼',
    '第五',
    '九亭',
    '精神',
    '卫生',
    '曙光',
    '泗泾',
    '医院',
    'songjiang',
    '九亭镇',
    '泗泾镇',
    'shuguang',
    '松江区',
    '上海'
]
details_list = [
    '上海市松江区中心医院',
    '上海市松江区泗泾医院',
    '上海曙光医院(松江分院)',
    '上海市第五康复医院',
    '上海市松江区松江区妇幼保健院',
    '上海市松江区精神卫生中心',
    '上海市松江区九亭医院',
    '上海市松江区岳阳街道社区卫生服务中心',
    '上海市松江区永丰街道社区卫生服务中心',
    '上海市松江区中山街道社区卫生服务中心',
    '上海市松江区方松街道社区卫生服务中心',
    '上海市松江区车墩镇社区卫生服务中心',
    '上海市松江区新桥镇社区卫生服务中心',
    '上海市松江区洞泾镇社区卫生服务中心',
    '上海市松江区九亭镇社区卫生服务中心',
    '上海市松江区泗泾镇社区卫生服务中心',
    '上海市松江区佘山镇社区卫生服务中心',
    '上海市松江区小昆山镇社区卫生服务中心',
    '上海市松江区石湖荡镇社区卫生服务中心',
    '上海市松江区新浜镇社区卫生服务中心',
    '上海市松江区泖港镇社区卫生服务中心',
    '上海市松江区叶榭镇社区卫生服务中心'
]
navigation_list = [
    '上海市松江区中山中路746号',
    '上海市松江区泗泾镇泗通路389号(近9号线泗泾站)',
    '上海市松江区中山东路39号',
    '上海市松江区乐都路279号',
    '上海市松江区西林北路1010号',
    '上海市松江区塔汇路209号',
    '上海市松江区九新公路155号',
    '上海市松江区阔街21号',
    '上海市松江区荣乐西路1039号',
    '上海市松江区施惠路451号',
    '上海市松江区文诚路805号',
    '上海市松江区虬长路168号',
    '上海市松江区新南街268号',
    '上海市松江区长兴东路1566号',
    '上海市松江区九亭镇易富路128号',
    '上海市松江区泗泾镇江川北路108号',
    '上海市松江区佘新路18号',
    '上海市松江区文翔路6300号',
    '上海市松江区石湖新路105号',
    '上海市松江区共青路1237号',
    '上海市松江区新宾路436号',
    '上海市松江区叶权路210号'

]


class GenerateTime:
    '''
    a1 = (2020, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（2020-01-01 00：00：00）
    a2 = (2020, 12, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（2020-12-31 23：59：59）
    '''

    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def run(self):
        start = time.mktime(self.a1)  # 生成开始时间戳
        end = time.mktime(self.a2)  # 生成结束时间戳
        t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
        date_touple = time.localtime(t)  # 将时间戳生成时间元组
        date = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
        return date

def generate_date(beginDate, endDate, index):
    date_list = []
    for i in range(0, index):
        date_list.append(GenerateTime(beginDate, endDate).run())
    return date_list


def generate_index(a1, a2, index):
    date_list = generate_date(a1, a2, index)
    for i in range(0, index):
        sql = """
                INSERT INTO wjw_log(description, type, method, params, create_date) VALUES ('%s', '%s', '%s', '%s', '%s')
               """ % (desc_list[2], "INFO", method_list[2], "", date_list[i])
        # print(sql)
        cursor.execute(sql)
    # 提交到数据库执行
    db.commit()


def generate_details(a1, a2, index):
    date_list = generate_date(a1, a2, index)
    for i in range(0, index):
        param = details_list[random.randint(0, len(details_list) - 1)]
        sql = """
               INSERT INTO wjw_log(description, type, method, params, create_date) VALUES ('%s', '%s', '%s', '%s', '%s')
              """ % (desc_list[1], "INFO", method_list[1], param, date_list[i])
        # print(sql)
        cursor.execute(sql)
        # 提交到数据库执行
    db.commit()


def generate_search(a1, a2, index):
    date_list = generate_date(a1, a2, index)
    for i in range(0, index):
        param = search_word[random.randint(0, len(search_word) - 1)]
        sql = """
               INSERT INTO wjw_log(description, type, method, params, create_date) VALUES ('%s', '%s', '%s', '%s', '%s')
              """ % (desc_list[0], "INFO", method_list[0], param, date_list[i])
        # print(sql)
        cursor.execute(sql)
        # 提交到数据库执行
    db.commit()


def generate_navigation(a1, a2, index):
    date_list = generate_date(a1, a2, index)
    for i in range(0, index):
        param = navigation_list[random.randint(0, len(navigation_list) - 1)]
        sql = """
               INSERT INTO wjw_log(description, type, method, params, create_date) VALUES ('%s', '%s', '%s', '%s', '%s')
              """ % (desc_list[3], "INFO", method_list[3], param, date_list[i])
        # print(sql)
        cursor.execute(sql)
        # 提交到数据库执行
    db.commit()


def run():
    dec_num = 56  # 2月访问量56
    jan_num = 165  # 1月访问量165
    feb_num = 153  # 2月访问量153

    dec_begin = (2020, 12, 1, 8, 0, 0, 0, 0, 0)
    dec_end = (2020, 12, 31, 20, 0, 0, 0, 0, 0)
    jan_begin = (2021, 1, 1, 8, 0, 0, 0, 0, 0)
    jan_end = (2021, 1, 31, 20, 0, 0, 0, 0, 0)
    feb_begin = (2021, 2, 1, 8, 0, 0, 0, 0, 0)
    feb_end = (2021, 2, 23, 20, 0, 0, 0, 0, 0)

    # 访问首页
    generate_index(dec_begin, dec_end, dec_num)
    generate_index(jan_begin, jan_end, jan_num)
    generate_index(feb_begin, feb_end, feb_num)

    # 查看医院详情
    generate_details(dec_begin, dec_end, dec_num + random.randint(1, 100))
    generate_details(jan_begin, jan_end, jan_num + random.randint(1, 100))
    generate_details(feb_begin, feb_end, feb_num + random.randint(1, 100))
    # 搜索医院
    generate_search(dec_begin, dec_end, dec_num + random.randint(50, 200))
    generate_search(jan_begin, jan_end, jan_num + random.randint(50, 100))
    generate_search(feb_begin, feb_end, feb_num + random.randint(50, 100))

    # 医院导航
    generate_navigation(dec_begin, dec_end, dec_num + random.randint(1, 100))
    generate_navigation(jan_begin, jan_end, jan_num + random.randint(1, 100))
    generate_navigation(feb_begin, feb_end, feb_num + random.randint(1, 100))


if __name__ == '__main__':
    run()
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("Database version : %s " % data)

    # 关闭数据库连接
    db.close()
