import numpy as np
from skimage import transform
import os
import sys
rootPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(rootPath)[0]
sys.path.append(rootPath)
from PIL import Image
import random
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')


rule_num = 16
rule_nums=96

def blend_two_images(image,background,rate = 0.6):

    img2 = Image.open(image)
    # img2 = image
    # img2 = Image.open("1.jpg")
    img2 = img2.convert('RGB')

    # img1 = Image.open(background)
    img1 = background
    # img1 = Image.open("2.jpg")
    img1 = img1.convert('RGB')
    img1 = img1.resize(img2.size)

    img = Image.blend(img1, img2, rate)
    # img.show()
    img.save(image)
# def color(imge, random:int):
#     imge = np.array(imge)
#     colorlist = [0, 60, 120, 180]
#     imge = np.where(imge <= 170, colorlist[random], imge).astype(np.uint8)
#     return imge


def color(imge,random:int):
    imge = np.array(imge)
    if random == 0:
        imge[:, :, 0] = np.where(imge[:, :, 0] < 255, 255, imge[:, :, 0]).astype(np.uint8)
        imge[:, :, 1] = np.where(imge[:, :, 1] < 255, 0, imge[:, :, 1]).astype(np.uint8)
        imge[:, :, 2] = np.where(imge[:, :, 2] < 255, 0, imge[:, :, 2]).astype(np.uint8)
    if random==1:
        imge[:, :, 0] = np.where(imge[:, :, 0] < 255, 255, imge[:, :, 0]).astype(np.uint8)
        imge[:, :, 1] = np.where(imge[:, :, 1] < 255, 255, imge[:, :, 1]).astype(np.uint8)
        imge[:, :, 2] = np.where(imge[:, :, 2] < 255, 0, imge[:, :, 2]).astype(np.uint8)
    if random==2:
        imge[:, :, 0] = np.where(imge[:, :, 0] < 255, 0, imge[:, :, 0]).astype(np.uint8)
        imge[:, :, 1] = np.where(imge[:, :, 1] < 255, 255, imge[:, :, 1]).astype(np.uint8)
        imge[:, :, 2] = np.where(imge[:, :, 2] < 255, 0, imge[:, :, 2]).astype(np.uint8)
    if random==3:
        imge[:, :, 0] = np.where(imge[:, :, 0] < 255, 0, imge[:, :, 0]).astype(np.uint8)
        imge[:, :, 1] = np.where(imge[:, :, 1] < 255, 0, imge[:, :, 1]).astype(np.uint8)
        imge[:, :, 2] = np.where(imge[:, :, 2] < 255, 255, imge[:, :, 2]).astype(np.uint8)
    return imge


def resize(imge, random:int):
    size_scale = [1,0.8,0.6,0.4]
    imge = np.array(imge)
    h, w, c = imge.shape
    if size_scale[random] == 1:
        return imge
    else:
        size=(imge.shape[0]*size_scale[random],imge.shape[1]*size_scale[random],3)
        img = transform.resize(imge, size)
        img = img * 255
        img = img.astype(np.uint8)
        temp = (np.ones((h, w, c)) * 255).astype(np.uint8)
        h_ = int(h / 2 *(1-size_scale[random]))
        w_ = int(w / 2 *(1-size_scale[random]))
        temp[h_:h_+img.shape[0],w_:w_+img.shape[1],0] = img[:,:,0]
        temp[h_:h_+img.shape[0],w_:w_+img.shape[1],1] = img[:,:,1]
        temp[h_:h_+img.shape[0],w_:w_+img.shape[1],2] = img[:,:,2]
        return temp

def read_image(path):
    img = []
    fileList = os.listdir(path)
    for i in range(len(fileList)):
        name = os.path.join(path, fileList[i])
        if 'json' in name:
            continue
        if 'docx' in name:
            continue
        img.append(Image.open(name))
    return img
img_huidu =read_image(path='./svg-png-gray/')
img_back = read_image(path='./background/')


def aback(img):
    textureimg = Image.open('./background/{nu}.jpg'.format(nu=random.randint(1, 7)))
    textureimg = textureimg.resize((img.shape[1], img.shape[0]))
    textureimgdata = np.array(textureimg)
    imge = np.where(img >250, textureimgdata, img).astype(np.uint8)
    return imge

def rotate(img):
    ROTATE = random.randint(0, 3)
    if ROTATE == 0:
        img = img.transpose(Image.ROTATE_90)
    elif ROTATE == 1:
        img = img.transpose(Image.ROTATE_180)
    elif ROTATE == 2:
        img = img.transpose(Image.ROTATE_270)
    return img


def q0(path,json_data_list,back=True):
    list0 = []
    L=[]
    L3=[]
    L4=[]
    all_num = len(json_data_list)
    while  L==sorted(L3) or sorted(L4)==sorted(L3) :
        a = random.sample(range(1, 10), 3)
        a=sorted(a)
        L1 = random.sample(range(1, 10), a[0])
        L2 = random.sample(range(1, 10), a[1])
        L = L1 + L2
        L4=[]
        for l in L:
            if L.count(l) == 1:
                L4.append(l)
        L = set(L)
        L = list(L)
        L = sorted(L)
        L3 = random.sample(range(1, 10), a[2])
    list0.append(L1)
    list0.append(L2)
    list0.append(L3)
    picture=random.randint(0, len(img_huidu)-1)
    # img_huidu = read_image(path='./huidu/')
    img = img_huidu[picture]
    count=0
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    for l in list0:
        for el in l:
            plt.subplot(3, 3, el)
            plt.imshow(img)
            plt.axis('off')
        if count == 0:
            name0 = str(all_num) +'-'+str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back==True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count == 1:
            name1 = str(all_num) + '-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back==True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count == 2:
            name2 =str(all_num) + '-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'number' + '-progression'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num )] = data_simple
    return json_data_list


def q1(path,json_data_list,back=True):
    all_num = len(json_data_list)
    list0 = [[], [], []]
    while len(list0[2]) == 0:
        list0 = []
        L1 = []
        L2 = []
        L3 = []
        L4= []
        L5 = []
        while sorted(L5)==sorted(L3) or sorted(L4) == sorted(L3) or (len(L3)>len(L2) and len(L2)>len(L1)):
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            L1 = random.sample(range(1, 10), a)
            L2 = random.sample(range(1, 10), b)
            L3 = []
            L5 = []
            L = L1 + L2
            L4 = set(L1+L2)
            L4 = list(L4)
            for l in L:
                if L.count(l) == 1:
                    L3.append(l)
                if L.count(l) == 2:
                    L5.append(l)
            L5=list(set(L5))

        list0.append(L1)
        list0.append(L2)
        list0.append(L3)
    picture=random.randint(0, len(img_huidu)-1)
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    # img_huidu = read_image(path='./huidu/')
    img = img_huidu[picture]
    count=0
    for l in list0:
        for el in l:
            plt.subplot(3, 3, el)
            plt.imshow(img)
            plt.axis('off')
        if count == 0:
            name0 = str(all_num) +'-'+str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count == 1:
            name1 = str(all_num) + '-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count == 2:
            name2 = str(all_num)  + '-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'position'+'-xor'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def q2(path,json_data_list,back=True):
    all_num = len(json_data_list)
    list0 = [[], [], []]
    while len(list0[2]) == 0:
        list0 = []
        L1=[]
        L2=[]
        L3=[]
        L4=[]
        L5=[]
        while sorted(L5)==sorted(L3) or sorted(L4) == sorted(L3) or (len(L3)>len(L2) and len(L2)>len(L1)):
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            L1 = random.sample(range(1, 10), a)
            L2 = random.sample(range(1, 10), b)
            L = L1 + L2
            L4 = []
            L5 = []
            L3 = set(L)
            L3 = list(L3)
            for l in L:
                if L.count(l) == 1:
                    L4.append(l)
                if L.count(l) == 2:
                    L5.append(l)
            L5=list(set(L5))

        list0.append(L1)
        list0.append(L2)
        list0.append(L3)
    picture=random.randint(0, len(img_huidu)-1)
    # img_huidu = read_image(path='./huidu/')
    img = img_huidu[picture]
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    count=0
    for l in list0:
        for el in l:
            plt.subplot(3, 3, el)
            plt.imshow(img)
            plt.axis('off')
        if count == 0:
            name0 = str(all_num) +'-'+str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count == 1:
            name1 = str(all_num) + '-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count == 2:
            name2 = str(all_num)  + '-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'position'+'-or'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    # json_data_list[str(p) + '-' + str(i)] = data_simple
    json_data_list[str(all_num )] = data_simple
    return json_data_list

def q3(path,json_data_list,back=True):
    all_num = len(json_data_list)
    list0=[[],[],[]]
    while len(list0[2])==0:
        list0 = []
        L1=[]
        L2=[]
        L3=[]
        L4=[]
        L5=[]
        while sorted(L5) == sorted(L3) or sorted(L4) == sorted(L3) or (len(L3) > len(L2) and len(L2) > len(L1)):
            a = random.randint(1, 7)
            b = random.randint(1, 7)
            L1 = random.sample(range(1, 10), a)
            L2 = random.sample(range(1, 10), b)
            L3 = []
            L4 = []
            L = L1 + L2
            L5=list(set(L))
            for l in L:
                if L.count(l) == 2:
                    L3.append(l)
                if L.count(l) == 1:
                    L4.append(l) 
            L3 = set(L3)
            L3 = list(L3)

        list0.append(L1)
        list0.append(L2)
        list0.append(L3)
    picture=random.randint(0, len(img_huidu)-1)
    # img_huidu = read_image(path='./huidu/')
    img = img_huidu[picture]
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    count=0
    for l in list0:
        for el in l:
            plt.subplot(3, 3, el)
            plt.imshow(img)
            plt.axis('off')
        if count == 0:
            name0 = str(all_num) +'-'+str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count == 1:
            name1 = str(all_num) + '-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count == 2:
            name2 = str(all_num)  + '-'+str(count) + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'position'+'-and'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def q4(path,json_data_list,back=True):
    all_num = len(json_data_list)
    list0 = [[], [], []]
    while len(list0[2]) == 0:
        list0 = []
        L3=[]
        L4=[]
        L5=[]
        L6=[]

        while sorted(L6) == sorted(L3) or sorted(L4) == sorted(L3)or sorted(L5) == sorted(L3):
            L4 = []
            L5 = []
            a = random.randint(1, 8)
            L1 = random.sample(range(1, 10), a)
            L2 = random.sample(range(1, 10), a)
            L3 = random.sample(range(1, 10), a)
            L = L1 + L2
            L6 = list(set(L))
            for l in L:
                if L.count(l) == 1:
                    L4.append(l)
                if L.count(l) == 2:
                    L5.append(l)

        list0.append(L1)
        list0.append(L2)
        list0.append(L3)
    # img_huidu = read_image(path='./huidu/')
    count=0
    picture=random.randint(0, len(img_huidu)-1)
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    size = random.sample(range(0, 4), 3)
    size=sorted(size)
    for l in list0:
        for el in l:
            plt.subplot(3, 3, el)
            # if count == 0:
            #     img = img_huidu[picture]
            #     size = random.randint(0, 1)
            # elif count == 1:
            #     img = img_huidu[picture]
            #     size = size + 1
            # elif count == 2:
            #     img = img_huidu[picture]
            #     size = size + 1
            img = img_huidu[picture]
            img = resize(img, size[count])
            plt.imshow(img)
            plt.axis('off')

            # img = img_huidu[picture]
            # plt.imshow(img)
            # plt.axis('off')
        if count == 0:
            name0 = str(all_num) +'-'+str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count  == 1:
            name1 = str(all_num)+'-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count  == 2:
            name2 = str(all_num) +'-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'size'+'-progression'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def q5(path,json_data_list,back=True):
    all_num = len(json_data_list)
    SIZE = [[], [], []]
    while len(SIZE[2]) == 0:
        SIZE=[]
        size0 = random.randint(2, 4)
        size1 = random.randint(2, 4)

        L1 = random.sample(range(0, 4), size0)
        L2 = random.sample(range(0, 4), size1)
        L3 = []
        L = L1 + L2
        for l in L:
            if L.count(l) == 1:
                L3.append(l)
        while sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted(
                list(set(L1).union(set(L2)))) == sorted(L3):
            size0 = random.randint(2, 4)
            size1 = random.randint(2, 4)
            # size0=4
            # size1=4

            L1 = random.sample(range(0, 4), size0)
            L2 = random.sample(range(0, 4), size1)
            L3 = []
            L = L1 + L2
            for l in L:
                if L.count(l) == 1:
                    L3.append(l)
        SIZE.append(L1)
        SIZE.append(L2)
        SIZE.append(L3)

    list0 = []
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    while sorted(L6) == sorted(L3) or sorted(L4) == sorted(L3) or sorted(L5) == sorted(L3):
        L4 = []
        L5 = []
        a = random.randint(4, 8)
        L1 = random.sample(range(1, 10), a)
        L2 = random.sample(range(1, 10), a)
        L3 = random.sample(range(1, 10), a)
        L = L1 + L2
        L6 = list(set(L))
        for l in L:
            if L.count(l) == 1:
                L4.append(l)
            if L.count(l) == 2:
                L5.append(l)
    list0.append(L1)
    list0.append(L2)
    list0.append(L3)
    # img_huidu = read_image(path='./huidu/')
    count=0
    picture=random.randint(0, len(img_huidu)-1)
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    for l in list0:
        b = 0

        for el in l:
            plt.subplot(3, 3, el)
            d =SIZE[count][b]
            img = img_huidu[picture]
            img = resize(img, d)
            if b >= len(SIZE[count]) - 1:
                b = random.randint(0, len(SIZE[count]) - 1)
            else:
                b = b + 1
            plt.imshow(img)
            plt.axis('off')
            # img = img_huidu[picture]
            # plt.imshow(img)
            # plt.axis('off')
        if count == 0:
            name0 = str(all_num) +'-'+str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count  == 1:
            name1 = str(all_num)+'-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count  == 2:
            name2 = str(all_num) +'-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'size'+'-xor'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def q6(path,json_data_list,back=True):

    all_num = len(json_data_list)

    SIZE = [[], [], []]
    while len(SIZE[2]) == 0:
        SIZE=[]
        size0 = random.randint(2, 4)
        size1 = random.randint(2, 4)
        L1 = random.sample(range(0, 4), size0)
        L2 = random.sample(range(0, 4), size1)
        L = L1 + L2
        L3 = set(L)
        L3 = list(L3)
        while sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted(
                list(set(list(set(L1).union(set(L2)))).difference(set(list(set(L1).intersection(set(L2))))))) == sorted(
            L3):
            size0 = random.randint(2, 4)
            size1 = random.randint(2, 4)
            L1 = random.sample(range(0, 4), size0)
            L2 = random.sample(range(0, 4), size1)
            L = L1 + L2
            L3 = set(L)
            L3 = list(L3)
        SIZE.append(L1)
        SIZE.append(L2)
        SIZE.append(L3)

    list0 = []
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    while sorted(L6) == sorted(L3) or sorted(L4) == sorted(L3) or sorted(L5) == sorted(L3):
        L4 = []
        L5 = []
        a = random.randint(4, 8)
        L1 = random.sample(range(1, 10), a)
        L2 = random.sample(range(1, 10), a)
        L3 = random.sample(range(1, 10), a)
        L = L1 + L2
        L6 = list(set(L))
        for l in L:
            if L.count(l) == 1:
                L4.append(l)
            if L.count(l) == 2:
                L5.append(l)
    list0.append(L1)
    list0.append(L2)
    list0.append(L3)
    # img_huidu = read_image(path='./huidu/')
    count=0
    picture=random.randint(0, len(img_huidu)-1)
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    for l in list0:
        b = 0
        for el in l:
            plt.subplot(3, 3, el)
            d =SIZE[count][b]
            img = img_huidu[picture]
            img = resize(img, d)
            if b >= len(SIZE[count]) - 1:
                b = random.randint(0, len(SIZE[count]) - 1)
            else:
                b = b + 1
            plt.imshow(img)
            plt.axis('off')
            # img = img_huidu[picture]
            # plt.imshow(img)
            # plt.axis('off')
        if count == 0:
            name0 = str(all_num) +'-'+str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count  == 1:
            name1 = str(all_num)+'-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count  == 2:
            name2 = str(all_num) +'-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'size'+'-or'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num)] = data_simple
    return json_data_list
def q7(path,json_data_list,back=True):

    all_num = len(json_data_list)
    SIZE = [[], [], []]
    while len(SIZE[2]) == 0:
        SIZE=[]
        size0 = random.randint(2, 4)
        size1 = random.randint(2, 4)
        L1 = random.sample(range(0, 4), size0)
        L2 = random.sample(range(0, 4), size1)
        L3 = []
        L = L1 + L2
        for l in L:
            if L.count(l) == 2:
                L3.append(l)
        L3=set(L3)
        L3 = list(L3)
        while sorted(list(set(L1).union(set(L2)))) == sorted(L3) or \
                sorted(list(set(list(set(L1).union(set(L2)))).difference(set(list(set(L1).intersection(set(L2)))))))\
                == sorted(L3):
            size0 = random.randint(2, 4)
            size1 = random.randint(2, 4)
            L1 = random.sample(range(0, 4), size0)
            L2 = random.sample(range(0, 4), size1)
            L3 = []
            L = L1 + L2
            for l in L:
                if L.count(l) == 2:
                    L3.append(l)
            L3 = set(L3)
            L3 = list(L3)
        SIZE.append(L1)
        SIZE.append(L2)
        SIZE.append(L3)
    list0 = []
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    while sorted(L6) == sorted(L3) or sorted(L4) == sorted(L3) or sorted(L5) == sorted(L3):
        L4 = []
        L5 = []
        a = random.randint(4, 8)
        L1 = random.sample(range(1, 10), a)
        L2 = random.sample(range(1, 10), a)
        L3 = random.sample(range(1, 10), a)
        L = L1 + L2
        L6 = list(set(L))
        for l in L:
            if L.count(l) == 1:
                L4.append(l)
            if L.count(l) == 2:
                L5.append(l)
    list0.append(L1)
    list0.append(L2)
    list0.append(L3)
    # img_huidu = read_image(path='./huidu/')
    count=0
    picture=random.randint(0, len(img_huidu)-1)
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    for l in list0:
        b=0
        for el in l:
            plt.subplot(3, 3, el)
            d =SIZE[count][b]
            img = img_huidu[picture]
            img = resize(img, d)
            if b >= len(SIZE[count]) - 1:
                b = random.randint(0, len(SIZE[count]) - 1)
            else:
                b = b + 1
            plt.imshow(img)
            plt.axis('off')
            # img = img_huidu[picture]
            # plt.imshow(img)
            # plt.axis('off')
        if count == 0:
            name0 = str(all_num) +'-'+str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count  == 1:
            name1 = str(all_num)+'-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count  == 2:
            name2 = str(all_num) +'-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'size'+'-and'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def q8(path,json_data_list,back=True):
    all_num = len(json_data_list)


    list0 = []
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    while sorted(L6) == sorted(L3) or sorted(L4) == sorted(L3) or sorted(L5) == sorted(L3):
        L4 = []
        L5 = []
        a = random.randint(1, 8)
        L1 = random.sample(range(1, 10), a)
        L2 = random.sample(range(1, 10), a)
        L3 = random.sample(range(1, 10), a)
        L = L1 + L2
        L6 = list(set(L))
        for l in L:
            if L.count(l) == 1:
                L4.append(l)
            if L.count(l) == 2:
                L5.append(l)
    list0.append(L1)
    list0.append(L2)
    list0.append(L3)
    # img_huidu = read_image(path='./huidu/')
    count = 0
    picture=random.randint(0, len(img_huidu)-1)
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    colo=random.sample(range(0, 4), 3)
    colo=sorted(colo)
    for l in list0:
        for el in l:
            plt.subplot(3, 3, el)
            img = img_huidu[picture]
            img = color(img, colo[count])
            plt.imshow(img)
            plt.axis('off')
        if count == 0:
            name0 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count == 1:
            name1 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count == 2:
            name2 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'color'+'-progression'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def q9(path,json_data_list,back=True):

    all_num = len(json_data_list)
    COLO = [[], [], []]
    while len(COLO[2]) == 0:
        COLO = []
        COLO0 = random.randint(2, 4)
        COLO1 = random.randint(2, 4)
        # size0=4
        # size1=4

        L1 = random.sample(range(0, 4), COLO0)
        L2 = random.sample(range(0, 4), COLO1)
        L3 = []
        L = L1 + L2
        for l in L:
            if L.count(l) == 1:
                L3.append(l)
        while sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted(
                list(set(L1).union(set(L2)))) == sorted(L3):
            COLO0 = random.randint(2, 4)
            COLO1 = random.randint(2, 4)
            # size0=4
            # size1=4

            L1 = random.sample(range(0, 4), COLO0)
            L2 = random.sample(range(0, 4), COLO1)
            L3 = []
            L = L1 + L2
            for l in L:
                if L.count(l) == 1:
                    L3.append(l)
        COLO.append(L1)
        COLO.append(L2)
        COLO.append(L3)

    list0 = []
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    while sorted(L6) == sorted(L3) or sorted(L4) == sorted(L3) or sorted(L5) == sorted(L3):
        L4 = []
        L5 = []
        a = random.randint(4, 8)
        L1 = random.sample(range(1, 10), a)
        L2 = random.sample(range(1, 10), a)
        L3 = random.sample(range(1, 10), a)
        L = L1 + L2
        L6 = list(set(L))
        for l in L:
            if L.count(l) == 1:
                L4.append(l)
            if L.count(l) == 2:
                L5.append(l)
    list0.append(L1)
    list0.append(L2)
    list0.append(L3)
    # img_huidu = read_image(path='./huidu/')
    count = 0
    picture=random.randint(0, len(img_huidu)-1)
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    for l in list0:
        b = 0
        for el in l:
            plt.subplot(3, 3, el)
            d = COLO[count][b]
            img = img_huidu[picture]
            img = color(img, d)
            if b >= len(COLO[count]) - 1:
                b = random.randint(0, len(COLO[count]) - 1)
            else:
                b = b + 1
            plt.imshow(img)
            plt.axis('off')
            # img = img_huidu[picture]
            # plt.imshow(img)
            # plt.axis('off')
        if count == 0:
            name0 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count == 1:
            name1 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count == 2:
            name2 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'color'+'-xor'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def q10(path,json_data_list,back=True):

    all_num = len(json_data_list)
    COLO = [[], [], []]
    while len(COLO[2]) == 0:
        COLO = []
        COLO0 = random.randint(2, 4)
        COLO1 = random.randint(2, 4)
        L1 = random.sample(range(0, 4), COLO0)
        L2 = random.sample(range(0, 4), COLO1)
        L = L1 + L2
        L3 = set(L)
        L3 = list(L3)
        while sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted(
                list(set(list(set(L1).union(set(L2)))).difference(set(list(set(L1).intersection(set(L2))))))) == sorted(
                L3):
            COLO0 = random.randint(2, 4)
            COLO1 = random.randint(2, 4)
            L1 = random.sample(range(0, 4), COLO0)
            L2 = random.sample(range(0, 4), COLO1)
            L = L1 + L2
            L3 = set(L)
            L3 = list(L3)
        COLO.append(L1)
        COLO.append(L2)
        COLO.append(L3)

    list0 = []
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    while sorted(L6) == sorted(L3) or sorted(L4) == sorted(L3) or sorted(L5) == sorted(L3):
        L4 = []
        L5 = []
        a = random.randint(4, 8)
        L1 = random.sample(range(1, 10), a)
        L2 = random.sample(range(1, 10), a)
        L3 = random.sample(range(1, 10), a)
        L = L1 + L2
        L6 = list(set(L))
        for l in L:
            if L.count(l) == 1:
                L4.append(l)
            if L.count(l) == 2:
                L5.append(l)
    list0.append(L1)
    list0.append(L2)
    list0.append(L3)
    # img_huidu = read_image(path='./huidu/')
    count = 0
    picture=random.randint(0, len(img_huidu)-1)
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    for l in list0:
        b = 0
        for el in l:
            plt.subplot(3, 3, el)
            d = COLO[count][b]
            img = img_huidu[picture]
            img = color(img, d)
            if b >= len(COLO[count]) - 1:
                b = random.randint(0, len(COLO[count]) - 1)
            else:
                b = b + 1
            plt.imshow(img)
            plt.axis('off')
            # img = img_huidu[picture]
            # plt.imshow(img)
            # plt.axis('off')
        if count == 0:
            name0 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count == 1:
            name1 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count == 2:
            name2 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'color'+'-or'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def q11(path,json_data_list,back=True):

    all_num = len(json_data_list)

    COLO = [[],[],[]]
    while len(COLO[2])==0:
        COLO = []
        COLO0 = random.randint(2, 4)
        COLO1 = random.randint(2, 4)
        L1 = random.sample(range(0, 4), COLO0)
        L2 = random.sample(range(0, 4), COLO1)
        L3 = []
        L = L1 + L2
        for l in L:
            if L.count(l) == 2:
                L3.append(l)
        L3 = set(L3)
        L3 = list(L3)
        while sorted(list(set(L1).union(set(L2)))) == sorted(L3) or sorted(
                list(set(list(set(L1).union(set(L2)))).difference(set(list(set(L1).intersection(set(L2))))))) == sorted(
            L3):
            COLO0 = random.randint(2, 4)
            COLO1 = random.randint(2, 4)
            L1 = random.sample(range(0, 4), COLO0)
            L2 = random.sample(range(0, 4), COLO1)
            L3 = []
            L = L1 + L2
            for l in L:
                if L.count(l) == 2:
                    L3.append(l)
            L3 = set(L3)
            L3 = list(L3)
        COLO.append(L1)
        COLO.append(L2)
        COLO.append(L3)

    list0 = []
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    while sorted(L6) == sorted(L3) or sorted(L4) == sorted(L3) or sorted(L5) == sorted(L3):
        L4 = []
        L5 = []
        a = random.randint(4, 8)
        L1 = random.sample(range(1, 10), a)
        L2 = random.sample(range(1, 10), a)
        L3 = random.sample(range(1, 10), a)
        L = L1 + L2
        L6 = list(set(L))
        for l in L:
            if L.count(l) == 1:
                L4.append(l)
            if L.count(l) == 2:
                L5.append(l)
    list0.append(L1)
    list0.append(L2)
    list0.append(L3)
    # img_huidu = read_image(path='./huidu/')
    count = 0
    picture=random.randint(0, len(img_huidu)-1)
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    for l in list0:
        b = 0

        for el in l:
            plt.subplot(3, 3, el)
            d = COLO[count][b]
            img = img_huidu[picture]
            img = color(img, d)
            if b >= len(COLO[count]) - 1:
                b = random.randint(0, len(COLO[count]) - 1)
            else:
                b = b + 1
            plt.imshow(img)
            plt.axis('off')
            # img = img_huidu[picture]
            # plt.imshow(img)
            # plt.axis('off')
        if count == 0:
            name0 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count == 1:
            name1 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count == 2:
            name2 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'color'+'-and'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def q12(path,json_data_list,back=True):

    all_num = len(json_data_list)
    list0 = []
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    while sorted(L6) == sorted(L3) or sorted(L4) == sorted(L3) or sorted(L5) == sorted(L3):
        L4 = []
        L5 = []
        a = random.randint(1, 8)
        L1 = random.sample(range(1, 10), a)
        L2 = random.sample(range(1, 10), a)
        L3 = random.sample(range(1, 10), a)
        L = L1 + L2
        L6 = list(set(L))
        for l in L:
            if L.count(l) == 1:
                L4.append(l)
            if L.count(l) == 2:
                L5.append(l)
    list0.append(L1)
    list0.append(L2)
    list0.append(L3)

    # img_huidu = read_image(path='./huidu/')
    count = 0
    picture=random.sample(range(0, len(img_huidu)),3)
    PIC=sorted(picture)
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]

    for l in list0:
        for el in l:
            plt.subplot(3, 3, el)
            img = img_huidu[PIC[count]]
            plt.imshow(img)
            plt.axis('off')
            # img = img_huidu[picture]
            # plt.imshow(img)
            # plt.axis('off')
        if count == 0:
            name0 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count == 1:
            name1 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count == 2:
            name2 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'type'+'-progression'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def q13(path,json_data_list,back=True):

    all_num = len(json_data_list)


    # img_huidu = read_image(path='./huidu/')
    PIC = [[],[],[]]
    while len(PIC[2]) == 0:
        PIC = []
        a1 = random.randint(2, 7)
        a2 = random.randint(2, 7)
        L1 = random.sample(range(0, len(img_huidu)), a1)
        L2 = random.sample(range(0, len(img_huidu)), a2)
        L3 = []
        L = L2 + L1
        for l in L:
            if L.count(l) == 1:
                L3.append(l)
        while len(L3)>=9 or sorted(list(set(L1).intersection(set(L2))))==sorted(L3) or sorted(list(set(L1).union(set(L2))))==sorted(L3):
            PIC = []
            a1 = random.randint(2, 7)
            a2 = random.randint(2, 7)
            L1 = random.sample(range(0, len(img_huidu)), a1)
            L2 = random.sample(range(0, len(img_huidu)), a2)
            L3 = []
            L = L2 + L1
            for l in L:
                if L.count(l) == 1:
                    L3.append(l)
        PIC.append(L1)
        PIC.append(L2)
        PIC.append(L3)

    list0 = []
    b=max(a1,a2)
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    while sorted(L6) == sorted(L3) or sorted(L4) == sorted(L3) or sorted(L5) == sorted(L3):
        L4 = []
        L5 = []
        a = random.randint(b, 8)
        L1 = random.sample(range(1, 10), a)
        L2 = random.sample(range(1, 10), a)
        L3 = random.sample(range(1, 10), a)
        L = L1 + L2
        L6 = list(set(L))
        for l in L:
            if L.count(l) == 1:
                L4.append(l)
            if L.count(l) == 2:
                L5.append(l)
    list0.append(L1)
    list0.append(L2)
    list0.append(L3)
    count = 0
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    for l in list0:
        b = 0

        for el in l:
            plt.subplot(3, 3, el)
            img = img_huidu[PIC[count][b]]
            if b >= len(PIC[count]) - 1:
                b = random.randint(0, len(PIC[count]) - 1)
            else:
                b = b + 1
            plt.imshow(img)

            # img = img_huidu[picture]
            # plt.imshow(img)
            plt.axis('off')
        if count == 0:
            name0 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count == 1:
            name1 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count == 2:
            name2 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'type'+'-xor'
    data_simple = {'img_name': name0 + name1+ name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def q14(path,json_data_list,back=True):

    all_num = len(json_data_list)


    # img_huidu = read_image(path='./huidu/')
    PIC = [[], [], []]
    while len(PIC[2]) == 0 :
        PIC=[]
        a1 = random.randint(2, 7)
        a2 = random.randint(2, 7)
        L1 = random.sample(range(0, len(img_huidu)), a1)
        L2 = random.sample(range(0, len(img_huidu)), a2)
        L3 = L1 + L2
        L3 = set(L3)
        L3 = list(L3)
        while len(L3)>8 or sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted(list(set(list(set(L1).union(set(L2)))).difference(set(list(set(L1).intersection(set(L2))))))) == sorted(L3):
            a1 = random.randint(2, 7)
            a2 = random.randint(2, 7)
            L1 = random.sample(range(0, len(img_huidu)), a1)
            L2 = random.sample(range(0, len(img_huidu)), a2)
            L3 = L1 + L2
            L3 = set(L3)
            L3 = list(L3)
        PIC.append(L1)
        PIC.append(L2)
        PIC.append(L3)

    a=max(len(L3),a1,a2)
    list0 = []
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    while sorted(L6) == sorted(L3) or sorted(L4) == sorted(L3) or sorted(L5) == sorted(L3):
        L4 = []
        L5 = []
        L1 = random.sample(range(1, 10), a)
        L2 = random.sample(range(1, 10), a)
        L3 = random.sample(range(1, 10), a)
        L = L1 + L2
        L6 = list(set(L))
        for l in L:
            if L.count(l) == 1:
                L4.append(l)
            if L.count(l) == 2:
                L5.append(l)
    list0.append(L1)
    list0.append(L2)
    list0.append(L3)
    count = 0
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    for l in list0:
        b = 0

        for el in l:
            plt.subplot(3, 3, el)
            img = img_huidu[PIC[count][b]]
            if b >= len(PIC[count]) - 1:
                b = random.randint(0, len(PIC[count]) - 1)
            else:
                b = b + 1
            plt.imshow(img)
            plt.axis('off')
                # img = img_huidu[picture]
                # plt.imshow(img)
                # plt.axis('off')
        if count == 0:
            name0 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count == 1:
            name1 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count == 2:
            name2 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'type'+'-or'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def q15(path,json_data_list,back=True):

    all_num = len(json_data_list)


    # img_huidu = read_image(path='./huidu/')
    PIC = [[], [], []]
    while len(PIC[2]) == 0:
        PIC=[]
        a1 = random.randint(2, 7)
        a2 = random.randint(2, 7)
        L1 = random.sample(range(0, len(img_huidu)), a1)
        L2 = random.sample(range(0, len(img_huidu)), a2)
        L3 = []
        L = L2 + L1
        for l in L:
            if L.count(l) == 2:
                L3.append(l)
        L3 = set(L3)
        L3 = list(L3)
        while sorted(list(set(L1).union(set(L2)))) == sorted(L3) or sorted(
                list(set(list(set(L1).union(set(L2)))).difference(set(list(set(L1).intersection(set(L2))))))) == sorted(
                L3):
            a1 = random.randint(2, 7)
            a2 = random.randint(2, 7)
            L1 = random.sample(range(0, len(img_huidu)), a1)
            L2 = random.sample(range(0, len(img_huidu)), a2)
            L3 = []
            L = L2 + L1
            for l in L:
                if L.count(l) == 2:
                    L3.append(l)
            L3 = set(L3)
            L3 = list(L3)
        PIC.append(L1)
        PIC.append(L2)
        PIC.append(L3)

    b=max(a1,a2)
    list0 = []
    L3 = []
    L4 = []
    L5 = []
    L6 = []
    while sorted(L6) == sorted(L3) or sorted(L4) == sorted(L3) or sorted(L5) == sorted(L3):
        L4 = []
        L5 = []
        a = random.randint(b, 8)
        L1 = random.sample(range(1, 10), a)
        L2 = random.sample(range(1, 10), a)
        L3 = random.sample(range(1, 10), a)
        L = L1 + L2
        L6 = list(set(L))
        for l in L:
            if L.count(l) == 1:
                L4.append(l)
            if L.count(l) == 2:
                L5.append(l)
    list0.append(L1)
    list0.append(L2)
    list0.append(L3)
    count = 0
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    for l in list0:
        b = 0
        for el in l:
            plt.subplot(3, 3, el)
            img = img_huidu[PIC[count][b]]
            if b >= len(PIC[count]) - 1:
                b = random.randint(0, len(PIC[count]) - 1)
            else:
                b = b + 1
            plt.imshow(img)
            plt.axis('off')
            # img = img_huidu[picture]
            # plt.imshow(img)
            # plt.axis('off')
        if count == 0:
            name0 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        elif count == 1:
            name1 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        elif count == 2:
            name2 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf() # 清图
            if back == True:
                blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'
        count = count + 1
    structure_str = 'type'+'-and'
    data_simple = {'img_name': name0 + name1+name2, 'Text': '', 'Out': structure_str}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def type_to(path,json_data_list,mode=1,back=True):
    # p = 'double-type-'
    all_num = len(json_data_list)
    str0 = ['type-progression', 'type-xor', 'type-or', 'type-and', ]
    str1 = ['color-progression', 'color-xor', 'color-or', 'color-and', 'number-progression', 'position-xor', 'position-or', 'position-and']
    first_rule_num = len(str0)
    second_rule_num = len(str1)
    for type in range(first_rule_num):
        for j in range(second_rule_num):
            if j==4:
                # all_num = len(json_data_list)
                list0 = []
                L = []
                L3 = []
                L4 = []
                while L == sorted(L3) or sorted(L4) == sorted(L3):
                    a = random.sample(range(4, 10), 3)
                    a = sorted(a)
                    L1 = random.sample(range(1, 10), a[0])
                    L2 = random.sample(range(1, 10), a[1])
                    L = L1 + L2
                    L4 = []
                    for l in L:
                        if L.count(l) == 1:
                            L4.append(l)
                    L = set(L)
                    L = list(L)
                    L = sorted(L)
                    L3 = random.sample(range(1, 10), a[2])
                list0.append(L1)
                list0.append(L2)
                list0.append(L3)
            elif j==5:
                # all_num = len(json_data_list)
                list0 = [[], [], []]
                while len(list0[2]) == 0:
                    list0=[]
                    L1 = []
                    L2 = []
                    L3 = []
                    L4 = []
                    L5 = []
                    while len(L3)<4 or sorted(L5) == sorted(L3) or sorted(L4) == sorted(L3) or (
                            len(L3) > len(L2) and len(L2) > len(L1)):
                        a = random.randint(4, 9)
                        b = random.randint(4, 9)
                        L1 = random.sample(range(1, 10), a)
                        L2 = random.sample(range(1, 10), b)
                        L3 = []
                        L5 = []
                        L = L1 + L2
                        L4 = set(L1 + L2)
                        L4 = list(L4)
                        for l in L:
                            if L.count(l) == 1:
                                L3.append(l)
                            if L.count(l) == 2:
                                L5.append(l)
                        L5 = list(set(L5))

                    list0.append(L1)
                    list0.append(L2)
                    list0.append(L3)
            elif j==6:
                list0 = [[], [], []]
                while len(list0[2]) == 0:
                    list0 = []
                    L1 = []
                    L2 = []
                    L3 = []
                    L4 = []
                    L5 = []
                    while len(L3)<4 or sorted(L5) == sorted(L3) or sorted(L4) == sorted(L3) or (
                            len(L3) > len(L2) and len(L2) > len(L1)):
                        a = random.randint(4, 9)
                        b = random.randint(4, 9)
                        L1 = random.sample(range(1, 10), a)
                        L2 = random.sample(range(1, 10), b)
                        L = L1 + L2
                        L3 = set(L)
                        L3 = list(L3)
                        L4 = []
                        L5 = []
                        for l in L:
                            if L.count(l) == 1:
                                L4.append(l)
                            if L.count(l) == 2:
                                L5.append(l)
                        L5 = list(set(L5))

                    list0.append(L1)
                    list0.append(L2)
                    list0.append(L3)
            elif j==7:
                list0 = [[], [], []]
                while len(list0[2]) == 0:
                    list0 = []
                    L1 = []
                    L2 = []
                    L3 = []
                    L4 = []
                    L5 = []
                    while len(L3)<4 or sorted(L5) == sorted(L3) or sorted(L4) == sorted(L3) or (
                            len(L3) > len(L2) and len(L2) > len(L1)):
                        a = random.randint(4, 9)
                        b = random.randint(4, 9)
                        L1 = random.sample(range(1, 10), a)
                        L2 = random.sample(range(1, 10), b)
                        L3 = []
                        L4 = []
                        L = L1 + L2
                        L5 = list(set(L))
                        for l in L:
                            if L.count(l) == 2:
                                L3.append(l)
                            if L.count(l) == 1:
                                L4.append(l)
                        L3 = set(L3)
                        L3 = list(L3)

                    list0.append(L1)
                    list0.append(L2)
                    list0.append(L3)

            else:
                list0 = []
                L3 = []
                L4 = []
                L5 = []
                L6 = []
                while sorted(L6) == sorted(L3) or sorted(L4) == sorted(L3) or sorted(L5) == sorted(L3):
                    L4 = []
                    L5 = []
                    a = random.randint(4, 9)
                    L1 = random.sample(range(1, 10), a)
                    L2 = random.sample(range(1, 10), a)
                    L3 = random.sample(range(1, 10), a)
                    L = L1 + L2
                    L6 = list(set(L))
                    for l in L:
                        if L.count(l) == 1:
                            L4.append(l)
                        if L.count(l) == 2:
                            L5.append(l)
                list0.append(L1)
                list0.append(L2)
                list0.append(L3)


            # img_huidu = read_image(path='./huidu/')
            if type==0:
                if mode==1:
                    PIC = random.sample(range(0, len(img_huidu)//9*8),3)
                if mode==2:
                    PIC = random.sample(range(len(img_huidu) // 9 * 8, len(img_huidu)), 3)


            if type==1:
                PIC = []
                L3=[]
                while len(L3)==0:
                    if mode == 1:
                        L1 = random.sample(range(0, len(img_huidu) // 9 * 8), 2)
                        L2 = random.sample(range(0, len(img_huidu) // 9 * 8), 2)
                    if mode == 2:
                        L1 = random.sample(range(len(img_huidu) // 9 * 8, len(img_huidu)), 2)
                        L2 = random.sample(range(len(img_huidu) // 9 * 8, len(img_huidu)), 2)
                    L = L2 + L1
                    L3 = []
                    for l in L:
                        if L.count(l) == 1:
                            L3.append(l)
                    while sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted(
                        list(set(L1).union(set(L2)))) == sorted(L3):
                        if mode==1:
                            L1 = random.sample(range(0, len(img_huidu)//9*8), 2)
                            L2 = random.sample(range(0, len(img_huidu)//9*8), 2)
                        if mode==2:
                            L1 = random.sample(range( len(img_huidu) // 9 * 8, len(img_huidu)), 2)
                            L2 = random.sample(range(len(img_huidu) // 9 * 8, len(img_huidu)), 2)

                        L = L2 + L1
                        L3 = []
                        for l in L:
                            if L.count(l) == 1:
                                L3.append(l)

                PIC.append(L1)
                PIC.append(L2)
                PIC.append(L3)

            if type==2:
                PIC = []
                L3= []
                while len(L3) == 0:
                    if mode == 1:
                        L1 = random.sample(range(0, len(img_huidu) // 9 * 8), 2)
                        L2 = random.sample(range(0, len(img_huidu) // 9 * 8), 2)
                    if mode == 2:
                        L1 = random.sample(range(len(img_huidu) // 9 * 8, len(img_huidu)), 2)
                        L2 = random.sample(range(len(img_huidu) // 9 * 8, len(img_huidu)), 2)
                    L3 = L1 + L2
                    L3 = set(L3)
                    L3 = list(L3)
                    while len(L3) == 9 or sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted\
                                (list(set(list(set(L1).union(set(L2)))).difference(set(list(set(L1).intersection(set(L2))))))) == sorted(L3):
                        if mode == 1:
                            L1 = random.sample(range(0, len(img_huidu) // 9 * 8), 2)
                            L2 = random.sample(range(0, len(img_huidu) // 9 * 8), 2)
                        if mode == 2:
                            L1 = random.sample(range(len(img_huidu) // 9 * 8, len(img_huidu)), 2)
                            L2 = random.sample(range(len(img_huidu) // 9 * 8, len(img_huidu)), 2)
                        L3 = L1 + L2
                        L3 = set(L3)
                        L3 = list(L3)
                PIC.append(L1)
                PIC.append(L2)
                PIC.append(L3)

            if type==3:
                PIC = []
                L3 = []
                while len(L3) == 0:
                    if mode == 1:
                        L1 = random.sample(range(0, len(img_huidu) // 9 * 8), 2)
                        L2 = random.sample(range(0, len(img_huidu) // 9 * 8), 2)
                    if mode == 2:
                        L1 = random.sample(range(len(img_huidu) // 9 * 8, len(img_huidu)), 2)
                        L2 = random.sample(range(len(img_huidu) // 9 * 8, len(img_huidu)), 2)
                    L = L2 + L1
                    L3 = []
                    for l in L:
                        if L.count(l) == 2:
                            L3.append(l)
                    L3=set(L3)
                    L3=list(L3)
                    while sorted(list(set(L1).union(set(L2)))) == sorted(L3) or sorted\
                                (list(set(list(set(L1).union(set(L2)))).difference(set(list(set(L1).intersection(set(L2))))))) == sorted(L3):
                        if mode == 1:
                            L1 = random.sample(range(0, len(img_huidu) // 9 * 8), 2)
                            L2 = random.sample(range(0, len(img_huidu) // 9 * 8), 2)
                        if mode == 2:
                            L1 = random.sample(range(len(img_huidu) // 9 * 8, len(img_huidu)), 2)
                            L2 = random.sample(range(len(img_huidu) // 9 * 8, len(img_huidu)), 2)
                        L = L2 + L1
                        L3 = []
                        for l in L:
                            if L.count(l) == 2:
                                L3.append(l)
                        L3 = set(L3)
                        L3 = list(L3)
                PIC.append(L1)
                PIC.append(L2)
                PIC.append(L3)




            if j==0 :
                colo=random.sample(range(0, 4), 3)
                colo=sorted(colo)
            elif j==1 :
                COLO = []
                L3 = []
                while len(L3)==0:
                    COLO0 = random.randint(2, 4)
                    COLO1 = random.randint(2, 4)
                    L1 = random.sample(range(0, 4), COLO0)
                    L2 = random.sample(range(0, 4), COLO1)
                    L = L1 + L2
                    L3 = []
                    for l in L:
                        if L.count(l) == 1:
                            L3.append(l)
                    while sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted(
                            list(set(L1).union(set(L2)))) == sorted(L3):
                        COLO0 = random.randint(2, 4)
                        COLO1 = random.randint(2, 4)
                        L1 = random.sample(range(0, 4), COLO0)
                        L2 = random.sample(range(0, 4), COLO1)
                        L3 = []
                        L = L1 + L2
                        for l in L:
                            if L.count(l) == 1:
                                L3.append(l)

                COLO.append(L1)
                COLO.append(L2)
                COLO.append(L3)
            elif j==2 :
                COLO = []
                COLO0 = random.randint(2, 4)
                COLO1 = random.randint(2, 4)
                L1 = random.sample(range(0, 4), COLO0)
                L2 = random.sample(range(0, 4), COLO1)
                L = L1 + L2
                L3 = set(L)
                L3 = list(L3)
                while sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted(
                        list(set(list(set(L1).union(set(L2)))).difference(
                            set(list(set(L1).intersection(set(L2))))))) == sorted(L3):
                    COLO0 = random.randint(2, 4)
                    COLO1 = random.randint(2, 4)
                    L1 = random.sample(range(0, 4), COLO0)
                    L2 = random.sample(range(0, 4), COLO1)
                    L = L1 + L2
                    L3 = set(L)
                    L3 = list(L3)
                COLO.append(L1)
                COLO.append(L2)
                COLO.append(L3)
                COLO.append(L1)
                COLO.append(L2)
                COLO.append(L3)
            elif j==3 :
                COLO = []
                L3 = []
                while len(L3)==0:
                    COLO0 = random.randint(2, 4)
                    COLO1 = random.randint(2, 4)
                    L1 = random.sample(range(0, 4), COLO0)
                    L2 = random.sample(range(0, 4), COLO1)
                    L3 = []
                    L=L1+L2
                    for l in L:
                        if L.count(l) == 2:
                            L3.append(l)
                    L3 = set(L3)
                    L3 = list(L3)
                    while sorted(list(set(L1).union(set(L2)))) == sorted(L3) or sorted(
                            list(set(list(set(L1).union(set(L2)))).difference(
                                set(list(set(L1).intersection(set(L2))))))) == sorted(
                        L3):
                        COLO0 = random.randint(2, 4)
                        COLO1 = random.randint(2, 4)
                        L1 = random.sample(range(0, 4), COLO0)
                        L2 = random.sample(range(0, 4), COLO1)
                        L3 = []
                        L = L1 + L2
                        for l in L:
                            if L.count(l) == 2:
                                L3.append(l)
                        L3 = set(L3)
                        L3 = list(L3)
                COLO.append(L1)
                COLO.append(L2)
                COLO.append(L3)
            count=0
            ba = random.randint(0, len(img_back) - 1)
            backpic = img_back[ba]
            for l in list0:
                b=0
                e=0
                for el in l:
                    plt.subplot(3, 3, el)
                    if type==0:
                        img = img_huidu[PIC[count]]
                    else:
                        img = img_huidu[PIC[count][e]]
                        if e >= len(PIC[count]) - 1:
                            e = random.randint(0, len(PIC[count]) - 1)
                        else:
                            e = e + 1

                    if j==0:
                        img = color(img,colo[count])
                    if j==1 or j==2 or j==3:
                        d=COLO[count][b]
                        img = color(img, d)
                        if b >= len(COLO[count]) - 1:
                            b = random.randint(0, len(COLO[count]) - 1)
                        else:
                            b = b + 1
                    plt.imshow(img)
                    plt.axis('off')
                    # img = img_huidu[picture]
                    # plt.imshow(img)
                    # plt.axis('off')
                if count == 0:
                    name0 = str(j + type * second_rule_num + all_num) + '-' + str(count) + '.jpg'
                    path_name = os.path.join(path, name0)
                    plt.savefig(path_name)
                    # plt.show()
                    plt.clf() # 清图
                    if back == True:
                        blend_two_images(image=path_name, background=backpic)
                    name0 = name0 + ';'
                elif count == 1:
                    name1 = str(j + type * second_rule_num + all_num) + '-' + str(count) + '.jpg'
                    path_name = os.path.join(path, name1)
                    plt.savefig(path_name)
                    # plt.show()
                    plt.clf() # 清图
                    if back == True:
                        blend_two_images(image=path_name, background=backpic)
                    name1 = name1 + ';'
                elif count == 2:
                    name2 =str(j + type * second_rule_num + all_num) + '-' + str(count) + '.jpg'
                    path_name = os.path.join(path, name2)
                    plt.savefig(path_name)
                    # plt.show()
                    plt.clf() # 清图
                    if back == True:
                        blend_two_images(image=path_name, background=backpic)
                    name2 = name2 + ';'
                count = count + 1

            structure_str =[str0[type],str1[j]]
            data_simple = {'img_name': name0 + name1 + name2, 'Text': '', 'Out': structure_str}
            print(j + type * second_rule_num + all_num)
            json_data_list[str(j + type * second_rule_num + all_num)]= data_simple
    return json_data_list

def color_to(path,json_data_list,mode=1,back=True):
    all_num = len(json_data_list)
    first_rule_num = 4
    second_rule_num = 8
    for type in range (first_rule_num):
        for j in range (second_rule_num):
            str0 = ['color-progression', 'color-xor', 'color-or', 'color-and' ]
            str1 = [ 'number-progression', 'position-xor', 'position-or', 'position-and','size-progression', 'size-xor',
                    'size-or', 'size-and']
            list0 = []
            if type== 0 :
                colo = random.sample(range(0, 4), 3)
                colo = sorted(colo)
            if type == 1 :
                COLO = []
                L3 = []
                while len(L3) == 0:
                    L3 = []
                    COLO0 = random.randint(2, 4)
                    COLO1 = random.randint(2, 4)

                    L1 = random.sample(range(0, 4), COLO0)
                    L2 = random.sample(range(0, 4), COLO1)
                    L = L1 + L2
                    for l in L:
                        if L.count(l) == 1:
                            L3.append(l)
                    while sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted(
                            list(set(L1).union(set(L2)))) == sorted(L3):
                        COLO0 = random.randint(2, 4)
                        COLO1 = random.randint(2, 4)
                        L1 = random.sample(range(0, 4), COLO0)
                        L2 = random.sample(range(0, 4), COLO1)
                        L3 = []
                        L = L1 + L2
                        for l in L:
                            if L.count(l) == 1:
                                L3.append(l)
                COLO.append(L1)
                COLO.append(L2)
                COLO.append(L3)
            if  type == 2 :
                COLO = []
                COLO0 = random.randint(2, 4)
                COLO1 = random.randint(2, 4)
                L1 = random.sample(range(0, 4), COLO0)
                L2 = random.sample(range(0, 4), COLO1)
                L = L1 + L2
                L3 = set(L)
                L3 = list(L3)
                while sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted(
                        list(set(list(set(L1).union(set(L2)))).difference(
                            set(list(set(L1).intersection(set(L2))))))) == sorted(
                    L3):
                    COLO0 = random.randint(2, 4)
                    COLO1 = random.randint(2, 4)
                    L1 = random.sample(range(0, 4), COLO0)
                    L2 = random.sample(range(0, 4), COLO1)
                    L = L1 + L2
                    L3 = set(L)
                    L3 = list(L3)
                COLO.append(L1)
                COLO.append(L2)
                COLO.append(L3)
            if  type == 3 :
                COLO = []
                L3 = []
                while len(L3) == 0:
                    COLO0 = random.randint(2, 4)
                    COLO1 = random.randint(2, 4)
                    L1 = random.sample(range(0, 4), COLO0)
                    L2 = random.sample(range(0, 4), COLO1)
                    L3 = []
                    L = L1 + L2
                    for l in L:
                        if L.count(l) == 2:
                            L3.append(l)
                    L3 = set(L3)
                    L3 = list(L3)
                    while sorted(list(set(L1).union(set(L2)))) == sorted(L3) or sorted(
                            list(set(list(set(L1).union(set(L2)))).difference(
                                set(list(set(L1).intersection(set(L2))))))) == sorted(
                        L3):
                        COLO0 = random.randint(2, 4)
                        COLO1 = random.randint(2, 4)
                        L1 = random.sample(range(0, 4), COLO0)
                        L2 = random.sample(range(0, 4), COLO1)
                        L3 = []
                        L = L1 + L2
                        for l in L:
                            if L.count(l) == 2:
                                L3.append(l)
                        L3 = set(L3)
                        L3 = list(L3)
                COLO.append(L1)
                COLO.append(L2)
                COLO.append(L3)
            if j == 0:
                L = []
                L3 = []
                L4 = []
                # all_num = len(json_data_list)
                while L == sorted(L3) or sorted(L4) == sorted(L3):
                    a = random.sample(range(4, 10), 3)
                    a = sorted(a)
                    L1 = random.sample(range(1, 10), a[0])
                    L2 = random.sample(range(1, 10), a[1])
                    L = L1 + L2
                    L4 = []
                    for l in L:
                        if L.count(l) == 1:
                            L4.append(l)
                    L = set(L)
                    L = list(L)
                    L = sorted(L)
                    L3 = random.sample(range(1, 10), a[2])
                list0.append(L1)
                list0.append(L2)
                list0.append(L3)
            elif j == 1:
                list0 = [[], [], []]
                while len(list0[2]) == 0:
                    list0 = []
                    L1 = []
                    L2 = []
                    L3 = []
                    L4 = []
                    L5 = []
                    while len(L3)<4 or sorted(L5) == sorted(L3) or sorted(L4) == sorted(L3) or (
                            len(L3) > len(L2) and len(L2) > len(L1)):
                        a = random.randint(4, 9)
                        b = random.randint(4, 9)
                        L1 = random.sample(range(1, 10), a)
                        L2 = random.sample(range(1, 10), b)
                        L3 = []
                        L5 = []
                        L = L1 + L2
                        L4 = set(L1 + L2)
                        L4 = list(L4)
                        for l in L:
                            if L.count(l) == 1:
                                L3.append(l)
                            if L.count(l) == 2:
                                L5.append(l)
                        L5 = list(set(L5))

                    list0.append(L1)
                    list0.append(L2)
                    list0.append(L3)
            elif j == 2:
                list0 = [[], [], []]
                while len(list0[2]) == 0:
                    list0 = []
                    L1 = []
                    L2 = []
                    L3 = []
                    L4 = []
                    L5 = []
                    while len(L3)<4 or sorted(L5) == sorted(L3) or sorted(L4) == sorted(L3) or (
                            len(L3) > len(L2) and len(L2) > len(L1)):
                        a = random.randint(4, 9)
                        b = random.randint(4, 9)
                        L1 = random.sample(range(1, 10), a)
                        L2 = random.sample(range(1, 10), b)
                        L = L1 + L2
                        L3 = set(L)
                        L3 = list(L3)
                        L4 = []
                        L5 = []
                        for l in L:
                            if L.count(l) == 1:
                                L4.append(l)
                            if L.count(l) == 2:
                                L5.append(l)
                        L5 = list(set(L5))

                    list0.append(L1)
                    list0.append(L2)
                    list0.append(L3)
            elif j == 3:
                list0 = [[], [], []]
                while len(list0[2]) == 0:
                    list0 = []
                    L1 = []
                    L2 = []
                    L3 = []
                    L4 = []
                    L5 = []
                    while len(L3)<4 or sorted(L5) == sorted(L3) or sorted(L4) == sorted(L3) or (
                            len(L3) > len(L2) and len(L2) > len(L1)):
                        a = random.randint(4, 7)
                        b = random.randint(4, 7)
                        L1 = random.sample(range(1, 10), a)
                        L2 = random.sample(range(1, 10), b)
                        L3 = []
                        L4 = []
                        L = L1 + L2
                        L5 = list(set(L))
                        for l in L:
                            if L.count(l) == 2:
                                L3.append(l)
                            if L.count(l) == 1:
                                L4.append(l)
                        L3 = set(L3)
                        L3 = list(L3)

                    list0.append(L1)
                    list0.append(L2)
                    list0.append(L3)

            else:
                list0 = []
                L3 = []
                L4 = []
                L5 = []
                L6 = []
                while sorted(L6) == sorted(L3) or sorted(L4) == sorted(L3) or sorted(L5) == sorted(L3):
                    L4 = []
                    L5 = []
                    a = random.randint(4, 8)
                    L1 = random.sample(range(1, 10), a)
                    L2 = random.sample(range(1, 10), a)
                    L3 = random.sample(range(1, 10), a)
                    L = L1 + L2
                    L6 = list(set(L))
                    for l in L:
                        if L.count(l) == 1:
                            L4.append(l)
                        if L.count(l) == 2:
                            L5.append(l)
                list0.append(L1)
                list0.append(L2)
                list0.append(L3)

            if j== 4 :
                size = random.sample(range(0, 4), 3)
                size = sorted(size)
            if j == 5 :
                SIZE = [[], [], []]
                while len(SIZE[2]) == 0:
                    SIZE = []
                    size0 = random.randint(2, 4)
                    size1 = random.randint(2, 4)

                    L1 = random.sample(range(0, 4), size0)
                    L2 = random.sample(range(0, 4), size1)
                    L3 = []
                    L = L1 + L2
                    for l in L:
                        if L.count(l) == 1:
                            L3.append(l)
                    while sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted(
                            list(set(L1).union(set(L2)))) == sorted(L3):
                        size0 = random.randint(2, 4)
                        size1 = random.randint(2, 4)
                        # size0=4
                        # size1=4

                        L1 = random.sample(range(0, 4), size0)
                        L2 = random.sample(range(0, 4), size1)
                        L3 = []
                        L = L1 + L2
                        for l in L:
                            if L.count(l) == 1:
                                L3.append(l)
                    SIZE.append(L1)
                    SIZE.append(L2)
                    SIZE.append(L3)
            if  j == 6 :
                SIZE = [[], [], []]
                while len(SIZE[2]) == 0:
                    SIZE = []
                    size0 = random.randint(2, 4)
                    size1 = random.randint(2, 4)
                    L1 = random.sample(range(0, 4), size0)
                    L2 = random.sample(range(0, 4), size1)
                    L = L1 + L2
                    L3 = set(L)
                    L3 = list(L3)
                    while sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted(
                            list(set(list(set(L1).union(set(L2)))).difference(
                                set(list(set(L1).intersection(set(L2))))))) == sorted(
                        L3):
                        size0 = random.randint(2, 4)
                        size1 = random.randint(2, 4)
                        L1 = random.sample(range(0, 4), size0)
                        L2 = random.sample(range(0, 4), size1)
                        L = L1 + L2
                        L3 = set(L)
                        L3 = list(L3)
                    SIZE.append(L1)
                    SIZE.append(L2)
                    SIZE.append(L3)
            if  j == 7:
                SIZE = [[], [], []]
                while len(SIZE[2]) == 0:
                    SIZE = []
                    size0 = random.randint(2, 4)
                    size1 = random.randint(2, 4)
                    L1 = random.sample(range(0, 4), size0)
                    L2 = random.sample(range(0, 4), size1)
                    L3 = []
                    L = L1 + L2
                    for l in L:
                        if L.count(l) == 2:
                            L3.append(l)
                    L3 = set(L3)
                    L3 = list(L3)
                    while sorted(list(set(L1).union(set(L2)))) == sorted(L3) or \
                            sorted(list(
                                set(list(set(L1).union(set(L2)))).difference(set(list(set(L1).intersection(set(L2))))))) \
                            == sorted(L3):
                        size0 = random.randint(2, 4)
                        size1 = random.randint(2, 4)
                        L1 = random.sample(range(0, 4), size0)
                        L2 = random.sample(range(0, 4), size1)
                        L3 = []
                        L = L1 + L2
                        for l in L:
                            if L.count(l) == 2:
                                L3.append(l)
                        L3 = set(L3)
                        L3 = list(L3)
                    SIZE.append(L1)
                    SIZE.append(L2)
                    SIZE.append(L3)
        # img_huidu = read_image(path='./huidu/')
            count = 0
            if mode==1:
                picture = random.randint(0, len(img_huidu)//9*8 - 1)
            if mode==2:
                picture = random.randint(len(img_huidu) // 9 * 8, len(img_huidu) - 1)
            ba = random.randint(0, len(img_back) - 1)
            backpic = img_back[ba]
            for l in list0:
                b=0
                e=0
                for el in l:
                    plt.subplot(3, 3, el)
                    img = img_huidu[picture]
                    if type==0:
                        img = color(img,colo[count])
                    if type==1 or type==2 or type==3:
                        d=COLO[count][b]
                        img = color(img, d)
                        if b >= len(COLO[count]) - 1:
                            b = random.randint(0, len(COLO[count]) - 1)
                        else:
                            b = b + 1
                    if j==4:
                        img = resize(img, size[count])
                    elif j==5 or j==6 or j==7:
                        m= SIZE[count][e]
                        img = resize(img, m)
                        if e >= len(SIZE[count]) - 1:
                            e = random.randint(0, len(SIZE[count]) - 1)
                        else:
                            e = e + 1


                    plt.imshow(img)
                    plt.axis('off')
                if count == 0:
                    name0 = str(j + type * second_rule_num + all_num) + '-' + str(count) + '.jpg'
                    path_name = os.path.join(path, name0)
                    plt.savefig(path_name)
                    # plt.show()
                    plt.clf() # 清图
                    if back == True:
                        blend_two_images(image=path_name, background=backpic)
                    name0 = name0 + ';'
                elif count == 1:
                    name1 = str(j + type * second_rule_num + all_num) + '-' + str(count) + '.jpg'
                    path_name = os.path.join(path, name1)
                    plt.savefig(path_name)
                    # plt.show()
                    plt.clf() # 清图
                    if back == True:
                        blend_two_images(image=path_name, background=backpic)
                    name1 = name1 + ';'
                elif count == 2:
                    name2 = str(j + type * second_rule_num + all_num) + '-' + str(count) + '.jpg'
                    path_name = os.path.join(path, name2)
                    plt.savefig(path_name)
                    # plt.show()
                    plt.clf() # 清图
                    if back == True:
                        blend_two_images(image=path_name, background=backpic)
                    name2 = name2 + ';'
                count = count + 1
            structure_str =[str0[type],str1[j]]
            data_simple = {'img_name': name0 + name1 + name2, 'Text': '', 'Out': structure_str}
            print(j + type * second_rule_num + all_num)
            json_data_list[str(j + type * second_rule_num + all_num)] = data_simple
    return json_data_list


def size_to(path,json_data_list,mode=1,back=True):

    all_num = len(json_data_list)
    first_rule_num = 4
    second_rule_num = 4
    for type in range (first_rule_num):
        for j in range (second_rule_num):
            str0 = ['size-progression', 'size-xor', 'size-or', 'size-and', ]
            str1 = [ 'number-progression', 'position-xor', 'position-or', 'position-and']
            list0 = []
            if type== 0 :
                size = random.sample(range(0, 4), 3)
                size = sorted(size)
            if type == 1 :
                SIZE = [[], [], []]
                while len(SIZE[2]) == 0:
                    SIZE = []
                    size0 = random.randint(2, 4)
                    size1 = random.randint(2, 4)

                    L1 = random.sample(range(0, 4), size0)
                    L2 = random.sample(range(0, 4), size1)
                    L3 = []
                    L = L1 + L2
                    for l in L:
                        if L.count(l) == 1:
                            L3.append(l)
                    while sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted(
                            list(set(L1).union(set(L2)))) == sorted(L3):
                        size0 = random.randint(2, 4)
                        size1 = random.randint(2, 4)
                        # size0=4
                        # size1=4

                        L1 = random.sample(range(0, 4), size0)
                        L2 = random.sample(range(0, 4), size1)
                        L3 = []
                        L = L1 + L2
                        for l in L:
                            if L.count(l) == 1:
                                L3.append(l)
                    SIZE.append(L1)
                    SIZE.append(L2)
                    SIZE.append(L3)
            if  type == 2 :
                SIZE = [[], [], []]
                while len(SIZE[2]) == 0:
                    SIZE = []
                    size0 = random.randint(2, 4)
                    size1 = random.randint(2, 4)
                    L1 = random.sample(range(0, 4), size0)
                    L2 = random.sample(range(0, 4), size1)
                    L = L1 + L2
                    L3 = set(L)
                    L3 = list(L3)
                    while sorted(list(set(L1).intersection(set(L2)))) == sorted(L3) or sorted(
                            list(set(list(set(L1).union(set(L2)))).difference(
                                set(list(set(L1).intersection(set(L2))))))) == sorted(
                        L3):
                        size0 = random.randint(2, 4)
                        size1 = random.randint(2, 4)
                        L1 = random.sample(range(0, 4), size0)
                        L2 = random.sample(range(0, 4), size1)
                        L = L1 + L2
                        L3 = set(L)
                        L3 = list(L3)
                    SIZE.append(L1)
                    SIZE.append(L2)
                    SIZE.append(L3)
            if  type == 3 :
                SIZE = [[], [], []]
                while len(SIZE[2]) == 0:
                    SIZE = []
                    size0 = random.randint(2, 4)
                    size1 = random.randint(2, 4)
                    L1 = random.sample(range(0, 4), size0)
                    L2 = random.sample(range(0, 4), size1)
                    L3 = []
                    L = L1 + L2
                    for l in L:
                        if L.count(l) == 2:
                            L3.append(l)
                    L3 = set(L3)
                    L3 = list(L3)
                    while sorted(list(set(L1).union(set(L2)))) == sorted(L3) or \
                            sorted(list(
                                set(list(set(L1).union(set(L2)))).difference(set(list(set(L1).intersection(set(L2))))))) \
                            == sorted(L3):
                        size0 = random.randint(2, 4)
                        size1 = random.randint(2, 4)
                        L1 = random.sample(range(0, 4), size0)
                        L2 = random.sample(range(0, 4), size1)
                        L3 = []
                        L = L1 + L2
                        for l in L:
                            if L.count(l) == 2:
                                L3.append(l)
                        L3 = set(L3)
                        L3 = list(L3)
                    SIZE.append(L1)
                    SIZE.append(L2)
                    SIZE.append(L3)
            if j == 0:
                list0 = []
                L = []
                L3 = []
                L4 = []
                while L == sorted(L3) or sorted(L4) == sorted(L3):
                    a = random.sample(range(4, 10), 3)
                    a = sorted(a)
                    L1 = random.sample(range(1, 10), a[0])
                    L2 = random.sample(range(1, 10), a[1])
                    L = L1 + L2
                    L4 = []
                    for l in L:
                        if L.count(l) == 1:
                            L4.append(l)
                    L = set(L)
                    L = list(L)
                    L = sorted(L)
                    L3 = random.sample(range(1, 10), a[2])
                list0.append(L1)
                list0.append(L2)
                list0.append(L3)
            if j == 1:
                list0 = [[], [], []]
                while len(list0[2]) == 0:
                    list0 = []
                    L1 = []
                    L2 = []
                    L3 = []
                    L4 = []
                    L5 = []
                    while len(L3)<4 or sorted(L5) == sorted(L3) or sorted(L4) == sorted(L3) or (
                            len(L3) > len(L2) and len(L2) > len(L1)):
                        a = random.randint(4, 9)
                        b = random.randint(4, 9)
                        L1 = random.sample(range(1, 10), a)
                        L2 = random.sample(range(1, 10), b)
                        L3 = []
                        L5 = []
                        L = L1 + L2
                        L4 = set(L1 + L2)
                        L4 = list(L4)
                        for l in L:
                            if L.count(l) == 1:
                                L3.append(l)
                            if L.count(l) == 2:
                                L5.append(l)
                        L5 = list(set(L5))

                    list0.append(L1)
                    list0.append(L2)
                    list0.append(L3)
            if j == 2:
                list0 = [[], [], []]
                while len(list0[2]) == 0:
                    list0 = []
                    L1 = []
                    L2 = []
                    L3 = []
                    L4 = []
                    L5 = []
                    while len(L3)<4 or sorted(L5) == sorted(L3) or sorted(L4) == sorted(L3) or (
                            len(L3) > len(L2) and len(L2) > len(L1)):
                        a = random.randint(4, 9)
                        b = random.randint(4, 9)
                        L1 = random.sample(range(1, 10), a)
                        L2 = random.sample(range(1, 10), b)
                        L = L1 + L2
                        L3 = set(L)
                        L3 = list(L3)
                        L4 = []
                        L5 = []
                        for l in L:
                            if L.count(l) == 1:
                                L4.append(l)
                            if L.count(l) == 2:
                                L5.append(l)
                        L5 = list(set(L5))

                    list0.append(L1)
                    list0.append(L2)
                    list0.append(L3)
            if j == 3:
                list0 = [[], [], []]
                while len(list0[2]) == 0:
                    list0 = []
                    L1 = []
                    L2 = []
                    L3 = []
                    L4 = []
                    L5 = []
                    while  len(L3)<4 or sorted(L5) == sorted(L3) or sorted(L4) == sorted(L3) or (len(L3) > len(L2) and len(L2) > len(L1)):
                        a = random.randint(4, 9)
                        b = random.randint(4, 9)
                        L1 = random.sample(range(1, 10), a)
                        L2 = random.sample(range(1, 10), b)
                        L3 = []
                        L4 = []
                        L = L1 + L2
                        L5 = list(set(L))
                        for l in L:
                            if L.count(l) == 2:
                                L3.append(l)
                            if L.count(l) == 1:
                                L4.append(l)
                        L3 = set(L3)
                        L3 = list(L3)

                    list0.append(L1)
                    list0.append(L2)
                    list0.append(L3)

            # img_huidu = read_image(path='./huidu/')
            count = 0
            if mode == 1:
                picture = random.randint(0, len(img_huidu) // 9 * 8 - 1)
            if mode == 2:
                picture = random.randint(len(img_huidu) // 9 * 8, len(img_huidu) - 1)
            ba = random.randint(0, len(img_back) - 1)
            backpic = img_back[ba]
            for l in list0:
                b=0
                for el in l:
                    plt.subplot(3, 3, el)
                    img = img_huidu[picture]
                    if type==0:
                        img = resize(img,size[count])
                    if type==1 or type==2 or type==3:
                        d=SIZE[count][b]
                        img = resize(img, d)
                        if b >= len(SIZE[count]) - 1:
                            b = random.randint(0, len(SIZE[count]) - 1)
                        else:
                            b = b + 1

                    plt.imshow(img)
                    plt.axis('off')
                if count == 0:
                    name0 = str(j + type * second_rule_num+ all_num) + '-' + str(count) + '.jpg'
                    path_name = os.path.join(path, name0)
                    plt.savefig(path_name)
                    # plt.show()
                    plt.clf() # 清图
                    if back == True:
                        blend_two_images(image=path_name, background=backpic)
                    name0 = name0 + ';'
                elif count == 1:
                    name1 = str(j + type * second_rule_num+ all_num) + '-' + str(count) + '.jpg'
                    path_name = os.path.join(path, name1)
                    plt.savefig(path_name)
                    # plt.show()
                    plt.clf()
                    if back == True:
                        blend_two_images(image=path_name, background=backpic)
                    name1 = name1 + ';'
                elif count == 2:
                    name2 = str(j + type * second_rule_num+ all_num) + '-' + str(count) + '.jpg'
                    path_name = os.path.join(path, name2)
                    plt.savefig(path_name)
                    # plt.show()
                    plt.clf() # 清图
                    if back == True:
                        blend_two_images(image=path_name, background=backpic)
                    name2 = name2 + ';'
                count = count + 1
            structure_str =[str0[type],str1[j]]
            data_simple = {'img_name': name0 + name1 + name2, 'Text': '', 'Out': structure_str}
            print(j + type * second_rule_num + all_num)
            json_data_list[str(j + type * second_rule_num+ all_num)] = data_simple
    return json_data_list

def type_find(path,json_data_list,back=True):
    all_num = len(json_data_list)
    s=random.randint(3,9)
    p=random.sample(range(1,10),s)

    ba = random.randint(0, len(img_back)-1)
    backpic=img_back[ba]
    picture = random.sample(range(0, len(img_huidu)), 2)
    count = 0
    for i in p:
        plt.subplot(3, 3, i)
        if count==0:
            img = img_huidu[picture[0]]
        else:
            img = img_huidu[picture[1]]
        plt.imshow(img)
        plt.axis('off')
        count =count+1
    name0= str(all_num) + '-A' + '.jpg'
    path_name = os.path.join(path, name0)
    plt.savefig(path_name)
    # plt.show()
    plt.clf()  # if back==True:清图
    if back==True:
        blend_two_images(image=path_name, background=backpic)
    name0 = name0 + ';'
    label=random.randint(1,2)
    if label==1:
        plt.subplot(3, 3, 1)
        img = img_huidu[picture[0]]
        plt.imshow(img)
        plt.axis('off')
        plt.subplot(3, 3, 2)
        img = img_huidu[picture[1]]
        plt.imshow(img)
        plt.axis('off')
    else:
        plt.subplot(3, 3, 1)
        img = img_huidu[picture[1]]
        plt.imshow(img)
        plt.axis('off')
        plt.subplot(3, 3, 2)
        img = img_huidu[picture[0]]
        plt.imshow(img)
        plt.axis('off')
    name1 = str(all_num) + '-B' + '.jpg'
    path_name = os.path.join(path, name1)
    plt.savefig(path_name)
    plt.clf()  # 清图
    if back == True:
        blend_two_images(image=path_name, background=backpic)
    name1 = name1 + ';'

    data_simple = {'img_name': name0 + name1, 'Text': '', 'Out': label}

    json_data_list[str(all_num)] = data_simple
    print(all_num)
    return json_data_list


def color_find(path, json_data_list,back=True):
    all_num = len(json_data_list)
    s = random.randint(3, 9)
    p = random.sample(range(1, 10), s)
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]

    pic = random.randint(0, len(img_huidu) - 1)
    pic = img_huidu[pic]
    co = random.sample(range(0, 4), 2)
    picture1 = color(pic, co[0])
    picture2 = color(pic, co[1])
    picture = []
    picture.append(picture1)
    picture.append(picture2)
    count = 0
    for i in p:
        plt.subplot(3, 3, i)
        if count == 0:
            img =picture[0]
        else:
            img = picture[1]
        plt.imshow(img)
        plt.axis('off')
        count = count + 1
    name0 = str(all_num) + '-A' + '.jpg'
    path_name = os.path.join(path, name0)
    plt.savefig(path_name)
    # plt.show()
    plt.clf()  # 清图
    if back == True:
        blend_two_images(image=path_name, background=backpic)
    name0 = name0 + ';'
    label = random.randint(1, 2)
    if label == 1:
        plt.subplot(3, 3, 1)
        img = picture[0]
        plt.imshow(img)
        plt.axis('off')
        plt.subplot(3, 3, 2)
        img = picture[1]
        plt.imshow(img)
        plt.axis('off')
    else:
        plt.subplot(3, 3, 1)
        img = picture[1]
        plt.imshow(img)
        plt.axis('off')
        plt.subplot(3, 3, 2)
        img = picture[0]
        plt.imshow(img)
        plt.axis('off')
    name1 = str(all_num) + '-B' + '.jpg'
    path_name = os.path.join(path, name1)
    plt.savefig(path_name)
    # plt.show()
    plt.clf()  # 清图
    if back == True:
        blend_two_images(image=path_name, background=backpic)
    name1 = name1 + ';'

    data_simple = {'img_name': name0 + name1, 'Text': '', 'Out': label}

    # json_data_list.append({str(p0): data_simple})
    json_data_list[str(all_num)] = data_simple
    print(all_num)
    return json_data_list

def size_find(path, json_data_list,back=True):
    all_num = len(json_data_list)
    s=random.randint(3,9)
    p=random.sample(range(1,10),s)
    count = 0
    pic = random.randint(0, len(img_huidu)-1)
    pic = img_huidu[pic]
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    co=random.sample(range(0, 4),2)
    picture1=resize(pic,co[0])
    picture2=resize(pic,co[1])
    picture=[]
    picture.append(picture1)
    picture.append(picture2)
    for i in p:
        plt.subplot(3, 3, i)
        if count==0:
            img = picture[0]
        else:
            img = picture[1]
        plt.imshow(img)
        plt.axis('off')
        count=count+1
    name0= str(all_num) + '-A' + '.jpg'
    path_name = os.path.join(path, name0)
    plt.savefig(path_name)
    plt.clf()  # 清图
    if back==True:
        blend_two_images(image=path_name, background=backpic)
    name0 = name0 + ';'
    label=random.randint(1,2)
    if label==1:
        plt.subplot(3, 3, 1)
        img = picture[0]
        plt.imshow(img)
        plt.axis('off')
        plt.subplot(3, 3, 2)
        img = picture[1]
        plt.imshow(img)
        plt.axis('off')
    else:
        plt.subplot(3, 3, 1)
        img = picture[1]
        plt.imshow(img)
        plt.axis('off')
        plt.subplot(3, 3, 2)
        img = picture[0]
        plt.imshow(img)
        plt.axis('off')
    name1 = str(all_num) + '-B' + '.jpg'
    path_name = os.path.join(path, name1)
    plt.savefig(path_name)
    plt.clf()  # 清图
    if back == True:
        blend_two_images(image=path_name, background=backpic)
    name1 = name1 + ';'
    data_simple = {'img_name': name0 + name1, 'Text': '', 'Out': label}
    json_data_list[str(all_num)] = data_simple
    print(all_num)
    return json_data_list

def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")

def get_filename(path,filetype):
    name =[]
    final_name = []
    for root,dirs,files in os.walk(path):
        for i in files:
            if filetype in i:
                name.append(i.replace(filetype,''))#生成不带‘.csv’后缀的文件名组成的列表
    final_name = [item +filetype for item in name]#生成‘.csv’后缀的文件名组成的列表
    return final_name #输出由有‘.csv’后缀的文件名组成的列表

if __name__ == '__main__':
    pass