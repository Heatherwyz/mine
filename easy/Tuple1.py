# -*- coding:utf-8 -*-
__author__ = "Heather"
if __name__ == '__main__':
    classmates =  ('Michael', 'Bob', 'Tracy')
    print(classmates)

    t = (1, 2)
    print('t:',t)
    t = ()
    print('t:',t)
    t = (1)
    print('t:', t)
    t = (1,)
    print('t:', t)

    t = ('a', 'b', ['A', 'B'])
    t[2][0] = 'X'
    t[2][1] = 'Y'
    print(t)