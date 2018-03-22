# -*- coding:utf-8 -*-
__author__ = "Heather"
if __name__ == '__main__':
    classmates = ['Michael', 'Bob', 'Tracy']
    print('classmates:',classmates)
    print('type:',type(classmates))
    print('len:',len(classmates))
    print('索引：',classmates[0],classmates[1],classmates[2],classmates[-1],classmates[-3])
    #往list中追加元素到末尾
    classmates.append('Adam')
    print('classmates1:',classmates)
    #把元素插入到指定的位置，比如索引号为1的位置
    classmates.insert(1,'Jack')
    print('classmates2:',classmates)
    #删除list末尾的元素
    classmates.pop()
    print('删除后的：',classmates)
    #删除指定位置的元素，用pop(i)方法，其中i是索引位置
    classmates.pop(1)
    print('第二次删除：',classmates)
    #把某个元素替换成别的元素，可以直接赋值给对应的索引位置
    classmates[1]='Sarah'
    print('替换后的：',classmates)

    L = ['Apple', 123, True]
    print('L:',L)
    s = ['python', 'java', ['asp', 'php'], 'scheme']
    print('s:',s)
    print('len(s):',len(s))

    L = []
    print('L:',L)
    print('len(L):',len(L))