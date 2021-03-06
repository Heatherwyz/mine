import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float))&isinstance(b,(int,float))&isinstance(c,(int,float)):
        raise TypeError('bad opreand type')
    else:
        d = b * b - 4 * a * c
        if d < 0:
            return ('方程无实数根')
        else:
            x1 = (- b + math.sqrt(d))/2/a
            x2 = (- b - math.sqrt(d))/2/a
            return x1,x2

if __name__ == '__main__':
    # 测试:
    print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
    print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

    if quadratic(2, 3, 1) != (-0.5, -1.0):
        print('测试失败')
    elif quadratic(1, 3, -4) != (1.0, -4.0):
        print('测试失败')
    else:
        print('测试成功')