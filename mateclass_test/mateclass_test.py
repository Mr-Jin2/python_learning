
class Mymetaclass(type):

    def __call__(cls, *args, **kwargs):
        print('metaclass call')
        return super().__call__(*args, **kwargs)

class Myclass(metaclass=Mymetaclass):
    def __init__(self, name):
        self.name = name



c = Myclass('m')
# print(c())
# Mymetaclass('Mymetaclass', (object,), dict(name='jyz'))()

