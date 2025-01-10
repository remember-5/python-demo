import warnings
import urllib3
from elasticsearch import Elasticsearch

# 禁用警告
warnings.filterwarnings("ignore")
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 基础认证连接
es = Elasticsearch(
    "https://192.168.0.123:31007",
    basic_auth=("elastic", "12345678"),
    verify_certs=False  # 开发环境可以禁用证书验证
)

# 测试连接
print(es.info())
