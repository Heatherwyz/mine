# -*- coding:utf-8 -*-
__author__ = "Heather"
import urllib.request
if __name__ == '__main__':
    url = "http://www.baidu.com"
    response = urllib.request.urlopen(url)
    print("status:","-"*30,"\n",response.status)
    print("reason","-"*30,"\n",response.reason)
    print("headers","-"*30,"\n",response.headers)
    print("read","-"*30,"\n",response.read().decode("utf-8"))