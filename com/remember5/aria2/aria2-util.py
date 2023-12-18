import aria2p

# 测试使用aria
# pip3 install aria2p
if __name__ == '__main__':
    aria2 = aria2p.Client(
        host="",
        port=6800,
        secret=""
    )

    uris = ["xxxx.png", "yyyy.png"]
    aria2.add_uri(uris=uris)
