'''
编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问，用起来就像下面这样:

'''

class Dict(dict):
    '''
    >>> d = Dict(a=1, b=2)
    >>> d['a']
        1
    >>>d.a
        1
    '''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key): #当访问的属性不存在时，调用该方法
        try:
            return self[key]
        except KeyError:
            raise AttributeError("没有这个key")
    def __setattr__(self, key, value):
        self[key] = value

class FishTank:
    def 

if __name__ == '__main__':
    d = Dict(3,4,name='jyz',gender='male')
    print(d.id, d.name, d['gender'])