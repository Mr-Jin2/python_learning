# 生成器的应用

# 一、构造一个生成器
# 1. map，map的返回值是一个生成器
iter1 = map(lambda x:x, [0,1,2])

print(type(map))
print(next(iter1)) # 一个个访问
for i in iter1: # 使用for访问
    print(i)
    break
print(list(iter1)) # 转化为列表访问

#2. 使用()
iter2 = (x for x in range(3))
print(next(iter2))

#3.yield
def iter3():
    for i in range(3):
        yield i

print('iter1 type is:',type(iter1))
print('iter2 type is:',type(iter2))
print('iter3() type is:',type(iter3()))

#4. 使用生成器构菲波那契数列,数列下标从1开始
def fib(n):
    a,b,i = 0,1,0
    while i<n:
        yield b
        a,b = b,a+b
        i += 1

def get_fib(n):
    # 此时fib(n)是一个生成器
    gener = fib(n)
    for i in range(n-1):
        next(gener)
    return next(gener)

print(get_fib(3))

