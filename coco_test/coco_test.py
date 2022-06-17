import json

anno_path = '/home/jyz/Downloads/coco_dataset/annotations_trainval2017/annotations/captions_val2017.json'
# # anno_json = json.load(open(anno_path, 'r'))
# # print(anno_json)
#
from pycocotools.coco import COCO
coco = COCO(annotation_file=anno_path)
annIDs = coco.getAnnIds(imgIds=range(1000))
print(annIDs)

# info = [{'name':['xl','pf']},{'age':[20, 20]}]
# with open('info.json','w') as fp:
#     fp.write(json.dumps(info))
#
# with open('info.json', 'r') as fp:
#     info = json.load(fp)
# print(type(info))
# print(type(info[0]))

d = {'name':'jyz', 'gender':'male'}
for i in d:
    print(i)