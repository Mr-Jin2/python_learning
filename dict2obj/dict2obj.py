# 使得字典对象可以像属性那样用.访问
import os.path


class Dict2Obj(dict):

    def __getattr__(self, key):
        print('getattr is called')
        if key not in self:
            return None
        else:
            value = self[key]
            if isinstance(value,dict):
                value = Dict2Obj(value)
            return value

dic = {
    'zone':{
        'city':'shenzhen',
        'location':'sx tech building'
    },
    'code':{
        'frontend':'vue',
        'backend':'python'
    }
}

# dic2obj = Dict2Obj(dic)
# print(type(dic2obj.zone.name))

# print(os.path.dirname(__file__))
# path = os.path.join(os.path.dirname(__file__),"..")
# with open(os.path.join(path,'main.py')) as f:
#     for i in f.readlines():
#         print(i)

def f1():
    f2()
    print('f1')

def f2():
    print('f2')

s = '<name>horse</name>'
print(s.strip())