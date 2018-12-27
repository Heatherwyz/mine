# -*- coding:utf-8 -*-
__author__ = "Heather"
import json
if __name__ == '__main__':
    print("python json格式化示例")
    data =  [{'a':1,'b':2,'c':3,'d':4,'e':5}]
    json_data = json.dumps(data,sort_keys = True,indent=4,separators=(',',':'))
    print(json_data)