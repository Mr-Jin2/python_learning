# 一. 底层（object）的__new__才能生产出一个实例
# 1. 如果不重写__new__，那么直接调的就是底层的__new__，但如果重写__new__，务必要显示地调用super().__new__，且要保证有直接调到底层new的通路
# 2. 此时无论多少层继承关系，cls都是要实例化的那个类
# 3. 使用metaclass相当于用C(name,)的方式生成对应类，即调用了元类的__call__方法

class A:

    def __new__(cls, *args, **kwargs): #不写*args和**kwargs
        print('A new is called, cls is', cls)
        return super().__new__(cls)

    def __init__(self, name):
        self.name =name


class B(A):
    pass

    def __new__(cls,*args):
        #print('args is ', args)

        return super().__new__(cls)

    def __init__(self, name):
        print('init is start')
        self.name = name
        print('init is end')
        print('instance dict is:',self.__dict__)

    def __setattr__(self, key, value):
        print('setattr is called')
        object.__setattr__(self, key, value)

    @classmethod
    def get_dict(cls):
        print('__dict__ is :', cls.__dict__)

    def fun(self):
        pass

b = B(name=3)
c = B(4)
d = B(5)
d.fun = print(3)
print(id(getattr(d,'fun')))
print(id(b.fun), id(c.fun), id(d.fun), id(B.fun))
print(B.__dict__)
print(b.__dict__)
print(c.__dict__)
print(dir(d))
print(dir(B))



# class C(type):
#
#     def __new__(cls, *args, **kwargs):
#         print('C new is called, cls is', cls)
#         return super().__new__(cls, *args, **kwargs)
#
#     def __call__(cls, *args, **kwargs):
#         print('C call is called')
#         return super().__call__(*args, **kwargs)
#
#
# class D(metaclass=C):
#
#     def __new__(cls, *args, **kwargs):
#         print('D new is called')
#         return super().__new__(cls)
#
#     pass

# print(D())
