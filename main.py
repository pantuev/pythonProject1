# ======= execise for test in OOP
class A:
    def __init__(self):
        print('A')


class B:
    def MM(self):
        print('B')


class C(A):
    def __init__(self):
        print('C')


class D(A, B):
    pass


for i in A, B, C, D:
    a = i()
# ======================
print('================')


# ======================
class A:
    def __init__(self):
        print('A')


class B:
    pass


class C(A):
    def __init__(self):
        print('C')


class D(C, B):
    pass


for i in A, B, C, D:
    a = i()
# ======================
print('================')


# ======================
class A:
    pass


class B:
    def __init__(self):
        print('B')


class C(A):
    def __init__(self):
        print('C')


class D(A, B):
    pass


for i in A, B, C, D:
    a = i()
# ======================
print('================')


# ======================
class A:
    def __init__(self):
        print('A')


class B:
    def __init__(self):
        print('B')


class C(A):
    pass


class D(C, B):
    pass


for i in A, B, C, D:
    a = i()
# =====================
print('================')


# ======================
class A:
    def __init__(self):
        print('A')


class B:
    def MM(self):
        print('B')


class C(A):
    def __init__(self):
        print('C')


class D(A, B):
    pass


for i in A, B, C, D:
    a = i()
# ======================
print('================')


# ======================
class A():
    def __init__(self):
        print('A')


class B:
    pass


class C(A):
    def __init__(self):
        print('C')


class D(C, B):
    pass


for i in A, B, C, D:
    a = i()
# ======================
print('================')


# ======================
class A():
    pass


class B():
    def __init__(self):
        print('B')


class C(A):
    def __init__(self):
        print('C')


class D(A, B):
    pass


for i in A, B, C, D:
    a = i()
# ======================
print('================')


# ======================
class A:
    def __init__(self):
        print('A')


class B(A):
    pass


class C(A):
    pass


class D(C, B):
    pass


for i in A, B, C, D:
    a = i()
# ======================
print('================')
# ======================
