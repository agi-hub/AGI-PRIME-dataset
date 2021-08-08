import numpy as np
from skimage import transform
import os
import matplotlib
matplotlib.use('Agg')
from PIL import Image
import random
import matplotlib.pyplot as plt
import util
import math
import time

def numb(X,Y,nu):
    list0=random.sample(X,nu)
    list1=random.sample(Y,nu)
    return list0,list1

def number(list0,list1,img,temp):
    for sign in range (len(list0)):
        x=list0[sign]
        y=list1[sign]
        temp[x:x+img.shape[0], y:y + img.shape[1], 0] = img[:, :, 0]
        temp[x:x+img.shape[0], y:y + img.shape[1], 1] = img[:, :, 1]
        temp[x:x+img.shape[0], y:y + img.shape[1], 2] = img[:, :, 2]
    return temp
img_huidu = util.read_image(path='./svg-png-gray/')
img_back = util.read_image(path='./background/')

def math_match(path,json_data_list,mode=1,back=True):
    all_num = len(json_data_list)
    str0=['+','-','*','**','>','<']
    for j in range(6):
        # start_time = time.time()
        if mode==1:
            a = random.randint(0, len(img_huidu)//9*8 - 1)
        if mode==2:
            a = random.randint(len(img_huidu) // 9 * 8 - 1,len(img_huidu)-1)
        ba = random.randint(0, len(img_back) - 1)
        backpic = img_back[ba]
        list=[]
        if j==0:
            b=random.randint(1, 9)
            c=random.randint(1, 9)
            d=b+c
        if j==1:
            b = random.randint(1, 9)
            c = random.randint(1, 9)
            d = b - c
        if j==2:
            b = random.randint(1, 9)
            c = random.randint(1, 9)
            d=b*c
        if j==3:
            b = random.randint(1, 9)
            c = random.randint(1, 2)
            d = b ** c
        if j==4:
            b = random.randint(1, 9)
            c = random.randint(1, 9)
            if b>c:
                d = 1
            else:
                d = 0
        if j==5:
            b = random.randint(1, 9)
            c = random.randint(1, 9)
            if b<c:
                d = 1
            else:
                d = 0



        L1 = random.sample(range(1, 10), b)
        L2 = random.sample(range(1, 10), c)
        list.append(L1)
        list.append(L2)
        count=0
        # print(time.time()- start_time)
        # start_time = time.time()

        for l in list:
            for p in l:
                plt.subplot(3, 3, p)
                # temp = (np.ones((4800*2, 6400*2 , 3)) * 255).astype(np.uint8)
                img = img_huidu[a]
                plt.imshow(img)
                plt.axis('off')
            if count == 0:
                name0 = str(j+all_num) + '-' + str(count) + '.jpg'
                path_name = os.path.join(path, name0)
                plt.savefig(path_name)
                # plt.show()
                plt.clf()  # 清图
                if back == True:
                    util.blend_two_images(image=path_name, background=backpic)
                name0 = name0 + ';'
            if count == 1:
                name1 = str(j+all_num) + '-' + str(count) + '.jpg'
                path_name = os.path.join(path, name1)
                plt.savefig(path_name)
                # plt.show()
                plt.clf()  # 清图
                if back == True:
                    util.blend_two_images(image=path_name, background=backpic)
                name1 = name1 + ';'

            count = count + 1


        # print(time.time() - start_time)
        structure_str = str0[j]
        data_simple = {'img_name': name0 + name1 , 'Text': structure_str, 'Out': d}
        print(j+all_num)
        json_data_list[str(j+all_num)] = data_simple
    return json_data_list
if __name__ == '__main__':
    pass
