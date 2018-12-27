# -*- coding:utf-8 -*-
__author__ = "WYZ"
# import os
# import json
# import sys
import requests

headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
        }
for gp in range(2244, 2245):  # 在此处修改股票代码遍历区间，特殊的如代码为 000021 请直接写作 21，执行过程会自动补全为000021
    gp = str(gp).zfill(6)
    url1 = "http://eq.10jqka.com.cn/ccyd/interface/timeShareOpenApi.php?code=" + gp
    response1 = requests.request("POST", url1, headers=headers)
    url2 = "http://testm.10jqka.com.cn/chensixiong/upload/event/upload.php"
    data2 = "&action=hset&code="+gp+"&submit=%E6%8F%90%E4%BA%A4&value="+response1.text
    response2 = requests.request("POST", url2, data=data2, headers=headers)
    url3 = "http://testm.10jqka.com.cn/ccyd/interface/timeShareOpenApi.php?code="+gp
    response3 = requests.request("POST", url3, headers=headers)
    if response1 == response3:
        print("OK")
    else:
        print("线上接口内容="+response1.text)
        print("测试接口内容="+response3.text)