
# 测试getattr()
class A(object):

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def cls_add(self):
        return self.num1 + self.num2

if __name__ == '__main__':
    a = A(1,2)
    cls_attr = getattr(a,'cls_add')
    print(cls_attr())
