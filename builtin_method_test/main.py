
# (1, 'a')
# (2, 'b')
# (3, 'c')
# lst = ['a', 'b', 'c']
# for i in enumerate(lst, 1):
#     print(i)

# import os.path as osp
# curr_path = osp.dirname(osp.abspath(__file__))
# print(curr_path)
# print(osp.abspath(__file__))
#
# class A:
#     name = 'name'
#
#     def f1(self,name):
#         print(name)
#
# a=A()
# a.f1()
#
from mmcv import Config

# cfgs = Config.fromfile('classification_pipe.json')
# print(type(cfgs))  # <class 'mmcv.utils.config.Config'>
# # # groups = cfgs.get('group')
# # for group in groups:
# #     print(group.get('operations')[0].get('input_stream'))
# print(cfgs.pretty_text)

# d = {
#     'person':{'name':'jyz'}
# }
#
#
# def f(person:dict =None):
#     print(person)
#
# f(**d)
import json

# lst = [('jyz','male'), ('zxj','female')]
# cotent = ''
#
# for i in lst:
#     cotent += f"{i[0]} {i[1]}\n"
#
# with open('item.txt','w', encoding='utf-8') as fp:
#     fp.write(cotent)

# path = '0/train/anno/train.json '
# print(path.strip().split('/'))

import  sys
print(sys.path)

from pytest import  console_main
