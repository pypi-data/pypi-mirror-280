"""
CLASH_PROXY

CLASH_PROXY_DICT

def cookies2dict(cookie_str: str) -> dict
"""

# httpx 用字符串
CLASH_PROXY = "http://127.0.0.1:7890"
# requests 用字典
CLASH_PROXY_DICT = {
    "http": CLASH_PROXY,
    "https": CLASH_PROXY,
}


def cookies2dict(cookies: str) -> dict:
    """
    把 cookies 字符串转换为字典

    cookie_str: str

    return: dict

    例如

    auth_token=824f3b553233b3f95436414e38d68e2c8a2380e7; ct0=6d9a80641d43b17852fda03513f200d2b3be76cba4c5b210326eb1689854553ddfa878424fe7517462a619268a9489a08a961c41e006722e0077f9bb2cc20830b943e50c4fabbf3158b42de5221c3f07

    ↓

    {'auth_token': '824f3b553233b3f95436414e38d68e2c8a2380e7', 'ct0': '6d9a80641d43b17852fda03513f200d2b3be76cba4c5b210326eb1689854553ddfa878424fe7517462a619268a9489a08a961c41e006722e0077f9bb2cc20830b943e50c4fabbf3158b42de5221c3f07'}
    """
    cookies_dict = {}
    for cookie in cookies.split(";"):
        key, value = cookie.strip().split("=")
        cookies_dict[key] = value
    return cookies_dict

if __name__ == "__main__":
    pass