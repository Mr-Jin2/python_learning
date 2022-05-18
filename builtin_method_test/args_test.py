'''
测试*args和**kwargs的使用方法

'''

def receive_args(*args, **kwargs):
    # print(f'args type is: {type(args)}, args[0] is: {args[0]}, args[1 ] is: {args[1]}，args[2] is: {args[2]}')
    # print(f"kwargs type is: {type(kwargs)}, name is: {kwargs['name']}, gender is: {kwargs['gender']}")
    print('args is: ',args)
    print('kwargs is: ',kwargs)

if __name__ == '__main__':
    a = 0
    b = 1
    c = 2
    t = (0,1,2,3)
    d = {'name':'jyz','gender':'male'}
    receive_args(*t,a,**d)

    # receive_args(0,1,2,name='jyz',gender='male')


