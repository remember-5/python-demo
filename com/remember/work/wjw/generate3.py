# 这个版本是模拟人进入的场景
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

hospital_list = [
    {'name': '上海市松江区中心医院', 'address': '上海市松江区中山中路746号'},
    {'name': '上海市松江区泗泾医院', 'address': '上海市松江区泗泾镇泗通路389号(近9号线泗泾站)'},
    {'name': '上海曙光医院(松江分院)', 'address': '上海市松江区中山东路39号'},
    {'name': '上海市第五康复医院', 'address': '上海市松江区乐都路279号'},
    {'name': '上海市松江区松江区妇幼保健院', 'address': '上海市松江区西林北路1010号'},
    {'name': '上海市松江区精神卫生中心', 'address': '上海市松江区塔汇路209号'},
    {'name': '上海市松江区九亭医院', 'address': '上海市松江区九新公路155号'},
    {'name': '上海市松江区岳阳街道社区卫生服务中心', 'address': '上海市松江区阔街21号'},
    {'name': '上海市松江区永丰街道社区卫生服务中心', 'address': '上海市松江区荣乐西路1039号'},
    {'name': '上海市松江区中山街道社区卫生服务中心', 'address': '上海市松江区施惠路451号'},
    {'name': '上海市松江区方松街道社区卫生服务中心', 'address': '上海市松江区文诚路805号'},
    {'name': '上海市松江区车墩镇社区卫生服务中心', 'address': '上海市松江区虬长路168号'},
    {'name': '上海市松江区新桥镇社区卫生服务中心', 'address': '上海市松江区新南街268号'},
    {'name': '上海市松江区洞泾镇社区卫生服务中心', 'address': '上海市松江区长兴东路1566号'},
    {'name': '上海市松江区九亭镇社区卫生服务中心', 'address': '上海市松江区九亭镇易富路128号'},
    {'name': '上海市松江区泗泾镇社区卫生服务中心', 'address': '上海市松江区泗泾镇江川北路108号'},
    {'name': '上海市松江区佘山镇社区卫生服务中心', 'address': '上海市松江区佘新路18号'},
    {'name': '上海市松江区小昆山镇社区卫生服务中心', 'address': '上海市松江区文翔路6300号'},
    {'name': '上海市松江区石湖荡镇社区卫生服务中心', 'address': '上海市松江区石湖新路105号'},
    {'name': '上海市松江区新浜镇社区卫生服务中心', 'address': '上海市松江区共青路1237号'},
    {'name': '上海市松江区泖港镇社区卫生服务中心', 'address': '上海市松江区新宾路436号'},
    {'name': '上海市松江区叶榭镇社区卫生服务中心', 'address': '上海市松江区叶权路210号'},
]
# 医院生成权重
hospital_list_weights = [
    8,
    6,
    8,
    6,
    7,
    5,
    5,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
]


class GenerateTime:
    """
    a1 = (2020, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（2020-01-01 00：00：00）
    a2 = (2020, 12, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（2020-12-31 23：59：59）
    """

    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def generate_date(self):
        start = time.mktime(self.a1)  # 生成开始时间戳
        end = time.mktime(self.a2)  # 生成结束时间戳
        t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
        date_touple = time.localtime(t)  # 将时间戳生成时间元组
        date = time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
        return date

    def generate_date_list(self, index):
        date_list = []
        for i in range(0, index):
            date_list.append(self.generate_date())
        return date_list

    def generate_datetime(self):
        start = time.mktime(self.a1)  # 生成开始时间戳
        end = time.mktime(self.a2)  # 生成结束时间戳
        t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
        date_touple = time.localtime(t)  # 将时间戳生成时间元组
        datetime = time.strftime("%Y-%m-%d %H:%M:%S", date_touple)  # 将时间元组转成格式化字符串（1976-05-21）
        return datetime

    def generate_datetime_list(self, index):
        datetime_list = []
        for i in range(0, index):
            datetime_list.append(self.generate_datetime())
        return datetime_list


def exec_sql(description, method, param, datetime):
    sql = """
            INSERT INTO wjw_log(description, type, method, params, create_date) VALUES ('%s', '%s', '%s', '%s', '%s')
           """ % (description, "INFO", method, param, datetime)
    cursor.execute(sql)
    db.commit()


def do_search(datetime):
    param = search_word[random.randint(0, len(search_word)-1)]
    exec_sql(desc_list[0], method_list[0], param, generate_sql_datetime(datetime))


def do_details(datetime):
    param = random.choices(hospital_list,hospital_list_weights)[0]['name']
    exec_sql(desc_list[1], method_list[1], param, generate_sql_datetime(datetime))


def do_navigation(datetime):
    param = random.choices(hospital_list, hospital_list_weights)[0]['address']
    exec_sql(desc_list[3], method_list[3], param, generate_sql_datetime(datetime))


def generate_sql_datetime(datetime):
    _s = time.mktime(time.strptime(datetime, '%Y-%m-%d %H:%M:%S')) + random.randint(1, 300)
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(_s))


def exec_by_date_list(date_list):
    # 获取要生成的index数量
    date_len = len(date_list)

    for i in range(0, date_len):
        date = date_list[i].split('-')  # 获取日期，为了规定在白天访问
        a1 = (int(date[0]), int(date[1]), int(date[2]), 8, 0, 0, 0, 0, 0)
        a2 = (int(date[0]), int(date[1]), int(date[2]), 19, 59, 59, 59, 59, 59)
        # 首先生成index的，这个datetime是访问首页的时间
        datetime = GenerateTime(a1, a2).generate_datetime()
        exec_sql(desc_list[2], method_list[2], "", datetime)  # 生成访问首页记录

        for i in range(0,random.randint(2, 10)):
            do_search(datetime)  # 生成搜索记录
            do_details(datetime)  # 生成详情记录
            do_navigation(datetime)  # 生成导航记录


def run():
    # 12月访问量56, 1月访问量165,2月访问量153 生成一共的天数，然后加入进去
    dec_num = 56
    jan_num = 165
    feb_num = 153

    # 月份时间限制,随机生成date,最后获取的date数组，一个属性代表的一个用户，站在用户的角度
    dec_begin = (2020, 12, 1, 0, 0, 0, 0, 0, 0)
    dec_end = (2020, 12, 31, 23, 59, 59, 59, 59, 59)
    jan_begin = (2021, 1, 1, 0, 0, 0, 0, 0, 0)
    jan_end = (2021, 1, 31, 23, 59, 59, 59, 59, 59)
    feb_begin = (2021, 2, 1, 0, 0, 0, 0, 0, 0)
    feb_end = (2021, 2, 23, 23, 59, 59, 59, 59, 59)

    # 首页，固定天数
    dec_date_list = GenerateTime(dec_begin, dec_end).generate_date_list(dec_num)
    jan_date_list = GenerateTime(jan_begin, jan_end).generate_date_list(jan_num)
    feb_date_list = GenerateTime(feb_begin, feb_end).generate_date_list(feb_num)

    exec_by_date_list(dec_date_list)  # 12月
    exec_by_date_list(jan_date_list)  # 1月
    exec_by_date_list(feb_date_list)  # 2月


if __name__ == '__main__':
    run()
    # print(time.time())
    # print(hospital_list[0])
    # print(random.choices(hospital_list,hospital_list_weights))
    # 关闭数据库连接
    db.close()
