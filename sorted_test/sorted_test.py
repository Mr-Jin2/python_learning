
# 1. sorted有返回值,key传入的函数作用于将要排序的可迭代对象的每一个元素
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#
# def by_name(i):
#     return i[0]
#
# def by_score(i):
#     return i[1]
# print(by_name(L))
#
# L2 = sorted(L, key=by_name)
# L22 = sorted(L, key=lambda i:i[0])
# print(L2)
# print(L22)
# L3 = sorted(L, key=by_score)
# L33 = sorted(L, key=lambda i:i[1])
# print(L3)
# print(L33)

exam_res = {
    'Mike':75,
    'Judy':88,
    'Cris':57
}
# print(sorted(exam_res))
# # for i in exam_res.items():
# #     print(i,type(i))
print(sorted(exam_res.items(), key=lambda i:i[1], reverse=True))

l = [3,5,2]
l.sort()
print(l)

for i in exam_res:
    print(i)

for i in exam_res.items():
    print(i)