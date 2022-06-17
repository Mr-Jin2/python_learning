
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
import copy
import math
import os.path
import sys

# from mmcv import Config
#
# cfgs = Config.fromfile('classification_pipe.json')
# print(cfgs.pipeline_name)
# print(cfgs.get('jyz'))
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

# import  sys
# print(sys.path)
#
# from pytest import  console_main
# d1 = dict(name='jyz', age=28)
# d2 = dict(name='male')
# a=1
# b=2
# def f(*args, **kwargs):
#     print(args)
#     print(kwargs)
# d1.update(d2)
# print(d1)
import time

from  loguru import  logger

import numpy as np
import  uwsgi_test

# def f(**kwargs):
#     print(kwargs)
# # lo : logger
# f()
#
# d = {}
# # d.update(None)
# # print(d)
#
# default = dict(status=True, remove_action=False)
# d.update(default)
# print(d)
# path = '/home/jyz/PycharmProjects/python_learning/venv/bin/python /home/jyz/PycharmProjects/python_learning/main.py'
# # if path.endswith('py'):
# #     print(True)
# print(os.path.join(os.path.join(path, ".."), 'main.py'))

# lst = ['a', 'b', 'c', 'a']
# print(lst.index('a'))
#
# # print(type(lst), lst)
# # print(list(lst))
# # a = set()
# # a.add('a')
# # a.add('a')
# # print(a)
# # dic = dict(
# #     a=[],
# #     b=dict()
# # )
# # print(dic)
# img = set()
# img.add('a')
# img.add('b')

# from collections import Counter
# a = [1,2,3,4,5,5,3]
# count_res = Counter(a)
# print(count_res)
# print([k for k,v in count_res.items() if v>2 ])
# res = [(k,v) for k,v in count_res.items() if v>2 ]
# a, b = [k for k,v in count_res.items() if v>2 ], [(k,v) for k,v in count_res.items() if v>2 ]
# print(a, b)
# s = sum([i[1] for i in res] )
# print(s)
# for i in map(sum,[[1,2],[3,4]]):
#     print(i)
# for i in res:
#     print('yes')
#
# dic = {'name':'jyz'}
# def f(d):
#     d.update({'name':'jyw'})
# f(dic)
# print(dic)
# if {'name':{}}:
#     print('yes')
# if not all([1,0]):
#     print('yes')

# dic = {'name':'jyz', 'age':{'y':2020,'m':3}}
# dic.pop('name')
# dic['age'].pop('y')
# print(dic)


# import random
# l = random.sample(range(10000),3)
# print(l)
# print(l.pop())
# print(l.pop())
# print(l)
#
# dic_lst = [{'name':'a'}, {'name':'b'}]
#
# print(f'info is {dic_lst}')
# a = dic_lst[0]
# b = dic_lst[1]
# c = [a,b]
# dic_lst.remove(b)
# print(dic_lst)

# def split(list_a, chunk_size):
#   for i in range(0, len(list_a), chunk_size):
#       yield list_a[i:i + chunk_size]
#
# chunk_size = 2
# my_list = [1,2,3,4,5,6,7,8,9]
# print(list(split(my_list, chunk_size)))



# from tqdm import tqdm
# l=[
#     {'name':[{'0':'mike'}, {'1':'nike'}]},
#     {'name':'b'}
# ]
# print('l[0] id is ' ,id(l[0]))
# def m(dic:dict):
#     for k,v in dic.items():
#         dic[k] = 'jyz'
#
# name = l[0]['name']
# for i in tqdm(name):
#     print(id(i))
#     m(i)
# print(l)
# m(l[0])
# print(l)

dataset = {
    "images": [
        {
            "id": 0,
            "file_name": "0.jpg"
        },
        {
            "id": 2,
            "file_name": "2.jpg"
        },
        {
            "id": 3,
            "file_name": "3.jpg"
        }
    ],
    'name':'j'
}

# L = []
# l1 = [1,2]
# l2 = [3,4]
# L.extend(l1)
# L.extend(l2)
# # L.append(l1)
# # L.append(l2)
# print(L)

# dir = '/home/jyz/Downloads/voc_dataset/Annotations/'
# lst = os.listdir(dir)
# file_name = [l.split('.')[0] for l in lst]
# print(len(file_name))
# with open('/home/jyz/Downloads/voc_dataset/voc.txt','w') as f:
#     s = '\n'.join(file_name)
#     f.write(s)

# p1 = 'home/Desktop'
# p2 = 'tmp'
# p3 = '/home'
# p4 = ''
#
# path1 = os.path.join(p1, p2) # 两个相对路径
# path2 = os.path.join(p1, p2, p3) # 绝对路径前的结果被丢弃
# path3 = os.path.join(p1, p4,p2, p4) # 空字符串在最后一项，则在拼接结果中添加/
#
# print('path1: ', path1)
# print('path2: ', path2)
# print('path3: ', path3)
# l = [1, 2, 3]
# print(id(l[0]), id(l[1]), id(l[2]))
# for i in range(len(l)):
#     print(id(i))
#     l[i] += 1
#     print(id(i))
# print(l)
# d = {'name':'jyz'}
# d.update({'age':20})
# print(d)

# ls1 = [1,2,3,4,5]
#
# ls2 = ls1.copy()
# print(id(ls1))
# print(id(ls2))

# a = ['a', 1, [1,2]]
# b = a
# c = copy.copy(a)
# d = copy.deepcopy(a)
#
#
# print(f'a is: {a} , id is: {id(a)}')
# print(f'b is: {b} , id is: {id(b)}')
# print(f'c is: {c} , id is: {id(c)}')
# print(f'd is: {d} , id is: {id(d)}')
#
# # 对对象本身进行修改
# a.append(2)
#
# print(f'a is: {a} , id is: {id(a)}')
# print(f'b is: {b} , id is: {id(b)}')
# print(f'c is: {c} , id is: {id(c)}')
# print(f'd is: {d} , id is: {id(d)}')
#
# # 修改嵌套对象
# a[2].append(3)
#
# print(f'a is: {a} , id is: {id(a)}')
# print(f'b is: {b} , id is: {id(b)}')
# print(f'c is: {c} , id is: {id(c)}')
# print(f'd is: {d} , id is: {id(d)}')
#
# print(f'1 id in a is {id(a[1])}')
# print(f'1 id in b is {id(b[1])}')
# print(f'1 id in c is {id(c[1])}')
# print(f'1 id in d is {id(d[1])}')
#
# print(f'a is {a}')
# print(f'{id(a[1])}, {id(a[2][0])}')

# a = ['a', 1, [1,2]]
# b = a[-1:]
# print(f'a is: {a} , id is: {id(a)}')
# print(f'b is: {b} , id is: {id(b)}')
#
# a[2].append(3)
# print(f'a is: {a} , id is: {id(a)}')
# print(f'b is: {b} , id is: {id(b)}')

# lst = [dict(name='jyz'), dict(name='jyw'), dict(name='jtr')]
# l2 = []
#
#
# for i in lst:
#     l2.append(i)
# print(id(lst[0]))
# print(id(l2[0]))
# lst[0]['name']='sb'
# print(l2)
# # lst = [1,2,3]
# # for i in lst:
# #     print(i)
# #     lst.remove(i)
# #     print(lst)



import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# For static images:
IMAGE_FILES = ['images/u.jpg']
with mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.5) as face_detection:
  for idx, file in enumerate(IMAGE_FILES):
    image = cv2.imread(file)
    # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
    results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw face detections of each face.
    if not results.detections:
      continue
    annotated_image = image.copy()
    for detection in results.detections:
      print('Nose tip:')
      print(mp_face_detection.get_key_point(
          detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
      mp_drawing.draw_detection(annotated_image, detection)
    cv2.imwrite('/tmp/annotated_image' + str(idx) + '.png', annotated_image)

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_face_detection.FaceDetection(
    model_selection=0, min_detection_confidence=0.5) as face_detection:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_detection.process(image)

    # Draw the face detection annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.detections:
      for detection in results.detections:
        mp_drawing.draw_detection(image, detection)
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()

