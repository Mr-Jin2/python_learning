
class A(object):

    def __init__(self, name,age):
        self.name = name
        self.age = age

    # def __getattribute__(self, attr):
    #     print("__getattribute__ is called")
    #     try:
    #         return super().__getattribute__(attr)
    #     except AttributeError:
    #         print(f'have no attr of {attr}')

    # def __getattribute__(self, attr):
    #     print("__getattribute__ is called")
    #     try:
    #         return super().__getattribute__(attr)
    #     except AttributeError:
    #         print(f'have no attr of {attr}')

    def __getattribute__(self, attr):
        if attr not  in ['name','age']:
            raise AttributeError
        else:
           return object.__getattribute__(self, attr)

    # def __setattr__(self, key, value):
    #     print(f"__setattr__() is called, key is {key}")
    #     object.__setattr__(self, key, value)

    def __getattr__(self, attr):
        print(f"__getattr__() is called，but {attr} is not exist!")



# class A(object):
#     gender = '男'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __getattribute__(self, attr):
#         print("拦截")
#         try:
#             return super(A, self).__getattribute__(attr)
#         except AttributeError:
#             print(f'have no attr of {attr}')

if __name__ == '__main__':
    a = A('jyz',200)
    print(a.name)
    print(a.gender)
 #   print(a.name)
    # print(a.age)
    # print(a.gender)