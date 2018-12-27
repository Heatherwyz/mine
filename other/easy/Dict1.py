d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Adam'] = 67
print(d['Adam'])
d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])
print('Thomas' in d)

print(d.get('Thomas'))
print(d.get('Thomas', -1))

d.pop('Bob')
print(d)


a = [1, 2, 3]
s = set(a)
print(type(a))
print(type(s))
print(s)
s = set([1, 1, 2, 2, 3, 3])
print(s)
s.add(4)
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1&s2)
print(s1|s2)

print("--"*20)
b = (1, 2, 3)
c = (1, [2, 3])
m1 = set(b)
m2 = set(c)
print(type(b))
print(type(c))
print(m1)
print(m2)
n1 = dict(b)
n2 = dict(c)
print(n1)
print(n2)