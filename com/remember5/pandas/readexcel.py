import pandas as pd

# 使用插件是pandas
if __name__ == '__main__':
    path= "/Users/wangjiahao/Downloads/test.xlsx"
    # 2.把Excel文件中的数据读入pandas
    df = pd.read_excel(path)
    print(df)
    # 3.读取excel的某一个sheet
    # df = pd.read_excel(path, sheet_name='Sheet1')
    # print(df)
    # # # 4.获取列标题
    # print(df.columns)
    # # # 5.获取列行标题
    # print(df.index)
    # # 6.制定打印某一列
    # print("=========")
    # print(df["name"])
    # print(type(df["name"]))
    name = df["name"]
    print(name[0])
    print(name[1])
    print("=====")


    age = df["age"]
    print(age[0])
    print(age[1])
    print("=====")

    address = df["address"]
    print(address[0])
    print(address[1])

    # # 7.描述数据
    # print(df.describe())