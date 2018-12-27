print(abs(100))
print(abs(-20))
print(max(1,2))
print(max(2,3,1,-5))

print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))
a = abs
print(a(-1))

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#my_abs('A')
my_abs(1,2)
