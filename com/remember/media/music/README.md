# 咪咕爬虫

## 使用工具
- python3.8,selenium,requests,xlwt,xlrd
- chromedriver,charles


## 思路
- 进入每个页面，点击播放，然后获取getPlayInfo的response(如下)，音乐有不同品质到bq,hq,sq
```
{
"returnCode":"000000",
"msg":"成功",
"data":{
    "bqPlayInfo":{
            "playUrl":"xxx.mp3",
            "formatId":"020007",
            "salePrice":null,
            "bizType":"00",
            "bizCode":null
        },
    "hqPlayInfo":{
        "playUrl":"xxx.mp3",
        "formatId":"020010",
        "salePrice":null,
        "bizType":"00",
        "bizCode":null
        },
    "sqPlayInfo":{
        "playUrl":"xxx.flac",
        "formatId":"011002",
        "salePrice":null,
        "bizType":"00",
        "bizCode":null
        }
    }
}
```
- charles抓包导出并保存所有的结果
- python读取charles所有文件，获取开头为getPlayInfo*的文件，并读取保存到excel
- 通过xlwt,xlrd,requests批量下载已知音乐(目前没做多线程)



