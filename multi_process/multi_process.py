import multiprocessing
from multiprocessing import Manager
import traceback

l = [1, 2, 3]

def add_key(dic,i):
    try:
        # print(id(dic))
        # print(id(dic))
        # print(id(dic['images'][0]))
        # print(id(dic['images'][0]))
        # print(id(dic['images'][0]))
        # print(id(dic['images'][0]))
        temp = dic['images']
        temp_i = temp[i]
        temp_i['iscrowd'] = 0
        temp.append(temp_i)
        print(temp_i)
        dic['images'] = temp

    except Exception:
        traceback.print_exc()

if __name__ == '__main__':

    p_dataset = Manager().dict(
        {
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
        ]
    }
    )
    pool = multiprocessing.Pool(processes=3)
    for i in range(3):
        pool.apply(add_key, args=(p_dataset,i))
    pool.close()
    pool.join()
    print(p_dataset)

# pool = multiprocessing.Pool(processes=3)
# for i in range(1):
#     pool.apply(add_key, args=(p_dataset,i))

# pool.close()
# pool.join()

# print(p_dataset)

# dic = Manager().dict()
# lst = Manager().list()
# dic_template = [{'name':'jyz'}, {'age':1}]
# def add_key(dic,i):
#     dic.update(dic_template[i])
#
#
# pool = multiprocessing.Pool(processes=2)
# for i in range(2):
#     pool.apply_async(add_key, args=(dic,i,))
#
# pool.close()
# pool.join()
#
# print(dic)