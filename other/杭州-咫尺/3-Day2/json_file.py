# -*- coding:utf-8 -*-
__author__ = "Heather"
import json
if __name__ == '__main__':
    print("python 写json串实例")
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
    fp = open('json_write.json','w')
    json.dump(data,fp,sort_keys=True,indent=4,separators=(',',':'))
    fp.close()