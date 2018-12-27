# -*- coding:utf-8 -*-
__author__ = "Heather"
if __name__ == '__main__':
    print(ord('A'))
    print(ord('中'))
    print(chr(66))
    print(chr(25991))
    print('\u4e2d\u6587')
    print('ABC'.encode('ascii'))
    print('中文'.encode('utf-8'))
    #print('中文'.encode('ascii'))
    print(b'ABC'.decode('ascii'))
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
    #print(b'\xe4\xb8\xad\xff'.decode('utf-8'))
    print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))

    print(len('ABC'))
    print(len('中文'))
    print(len(b'ABC'))
    print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
    print(len('中文'.encode('utf-8')))

    print('hello,%s'%'world')
    print('hi,%s,you have $%d'%('michael',1000))
    print('Age: %s. Gender: %s' % (25, True))
    print('growth rate: %d %%' % 7)

    print( 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
