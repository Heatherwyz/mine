# -*- coding:utf-8 -*-
__author__ = "Heather"
import json
if __name__ == '__main__':
    print("python json 标准库解析示例")

    #python对象转化为json对象
    data = [{'a':1,'b':2,'c':3,'d':4,'e':5}]

    json_data = json.dumps(data)

    print("before:")
    print(type(data))
    print(data)
    print("-"*40)
    print(type(json_data))
    print(json_data)

    print()
    print("json->python")
    python_data = json.loads(json_data)
    print(type(python_data))
    print(python_data)