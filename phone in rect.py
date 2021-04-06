import os
import cv2
import json
import random

split_list = []
os.mkdir("D:/dataset")  # создание папки на диске D
for i in os.listdir('D:/dataset phone'):
    split_list.append(i.split("."))
for filename in split_list:
    if filename[1] in ["jpg", "jpeg", "png"]:
        name = ".".join(filename)
        img = cv2.imread("D:/dataset phone/{}".format(name), cv2.IMREAD_UNCHANGED)
        json_file = "D:/dataset phone/{}.json".format(filename[0])
        with open(json_file, 'r', encoding='utf-8') as f:
            coord = json.load(f)
        res_img = cv2.rectangle(img, (coord[1][0], coord[1][1]), (coord[1][2], coord[1][3]), (0, 255, 255), 5)
        name_file = 'D:/dataset/{}.jpg'.format(random.randint(0, 1000))
        cv2.imwrite(name_file, res_img) # запись изображений в папку
