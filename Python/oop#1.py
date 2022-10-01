class B(object):
    a = 23
    b = 45
    def f(self): print('method f in class B')
    def g(self): print('method g in class B')
    print(a)
    print(b)
class C(B):
    b = 67
    c = 89
    d = 123
    print(b)
    print(c)
    print(d)
    def g(self): print('method g in class C')
    def h(self): print('method h in class C')
x = C()
print('here')
print(x.d)
x.d = 77
x.e = 88
