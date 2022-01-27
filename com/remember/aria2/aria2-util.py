import aria2p



if __name__ == '__main__':
    aria2 =  aria2p.Client(
        host="http://1.15.94.39",
        port=6800,
        secret="n3BRTC0mZeBw2x14Xzwt"
    )

    aria2.add_uri(uris=["https://dev8apk.baidupan.com/110613bb/2021/11/01/807dc93a796fd9bca7e0b0b1ef45df87.dmg?st=E7vyq5vc49OD33eB1Z7oXw&e=1636179949&b=BRgAbQFvVjoAElB0CzoDYVRnCTlUMAtSUTVbeFdhBD8FeQEwCFdRfFI1UzVRNFV_aBWIOYwMsUWVVLwtZBilfuwXLAIAB5VbuANtQNwtqAylUMQl8VAoLUlFvWzdXMwRxBTwBLwhrUTtSalMrUWVVPAU3&fi=55471448&pid=222"])