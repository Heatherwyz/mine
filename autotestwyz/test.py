# -*- coding:utf-8 -*-
__author__ = "WYZ"

import urllib.request,re
#qq = "http://testm.10jqka.com.cn/ccyd/data/timeShareEvent/" #若要遍历测试环境，请去掉前面的#
qq = "http://eq.10jqka.com.cn/ccyd/interface/timeShareOpenApi.php?code="
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
headers = {'User-Agent': user_agent}
for gp in range(1, 10):  # 在此处修改股票代码遍历区间，特殊的如代码为 000021 请直接写作 21，执行过程会自动补全为000021
    gp = str(gp).zfill(6)
    url1 = qq + gp
    xx = None
    print(url1)
    request = urllib.request.Request(url1,xx,headers)
    respond = urllib.request.urlopen(request)
    answer = respond.read()
    print(respond.text)
    answer = answer.decode('unicode_escape')

    # if re.search("申购时间",answer) is not None :
    #     print ("")
    #     print (gp, end='')
    #     print (answer)
    # else:
    #     if int(gp) % 150 == 0:
    #         print("-")
    #     else:
    #         print("-", end='')