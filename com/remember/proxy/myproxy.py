from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request

# 定义代理服务器的主机名和端口号
PROXY_HOST = '127.0.0.1'
PROXY_PORT = 8888


class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 构建目标URL
        target_url = self.path

        # 构建请求对象
        req = urllib.request.Request(target_url)

        try:
            # 发送请求并获取响应
            response = urllib.request.urlopen(req)

            # 获取响应的内容和状态码
            content = response.read()
            status_code = response.getcode()

            # 返回响应给客户端
            self.send_response(status_code)
            self.end_headers()
            self.wfile.write(content)

        except urllib.error.HTTPError as e:
            # 如果出现HTTP错误，返回错误状态码给客户端
            self.send_error(e.code, e.reason)


if __name__ == '__main__':
    # 创建代理服务器并指定处理程序
    proxy_server = HTTPServer((PROXY_HOST, PROXY_PORT), ProxyHandler)
    print(f'Proxy server is running on {PROXY_HOST}:{PROXY_PORT}')

    # 启动代理服务器
    proxy_server.serve_forever()
