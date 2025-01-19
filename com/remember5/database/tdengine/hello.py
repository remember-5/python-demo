from taosrest import RestClient
from flask import Flask, app

app = Flask(__name__)
# https://docs.taosdata.com/api/taospy/taosrest/restclient.html#taosrest.restclient.RestClient.sql
client = RestClient(
    url="http://10.0.23.81:6041",
    user="root",
    password="uRcqOhkjO6",
    database="photovoltaic",
    timeout=30
)


def client_info():
    """
    查看database和stables
    """
    # show database;
    res: dict = client.sql("SHOW DATABASES;")
    print(res)
    # show stables;
    res: dict = client.sql("SHOW STABLES;")
    print(res)


def get_all_table_data():
    """
    获取所有表的数据信息
    """
    result = []
    table_list: dict = client.sql("SHOW STABLES;")
    for _ in table_list["data"]:
        stables_name = _[0]
        print(stables_name)
        # 获取最后一条数据
        sql = "select * from " + stables_name
        print(sql)
        table_data: dict = client.sql(sql)
        print(table_data)
        result.append(table_data)
    return result


def get_ps_data():
    """
    获取电站发电信息
    """
    data: dict = client.sql(
        "SELECT PS_id, PS_install_power, stamp_time,EM_day_current, day_radiation FROM DWS_PVPP_DAY")
    result = []
    for _ in data["data"]:
        stamp_time = str(_[2])
        _data = {
            "ps_id": _[0],
            "ps_install_power": _[1],
            "stamp_time": stamp_time[0:4] + "-" + stamp_time[4:6] + "-" + stamp_time[6:],
            "em_day_current": _[3],
            "day_radiation": _[4]
        }
        result.append(_data)
    return result


@app.route("/")
def hello_world():
    return get_ps_data()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
