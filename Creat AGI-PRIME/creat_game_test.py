import os
import json
import random
import util
import shutil
import matplotlib
matplotlib.use('Agg')
random.seed(2021)
import matplotlib.pyplot as plt
import numpy as np

img_huidu=util.read_image(path='./svg-png-gray/')
img_back = util.read_image(path='./background/')
def game(path,json_data_list,back=False):
    out=[0,0,0,0,0,0,0,0,0]
    out1=[1,2,3,4,5,6,7,8,9]
    all_num = len(json_data_list)
    a=random.randint(3, 9)
    picture1=random.sample(range(len(img_huidu) // 9 * 8 - 1,len(img_huidu)-1), a)
    picture2 = random.sample(picture1, a)
    picture3 = random.sample(picture1, a)
    knowledge = sorted(range(len(picture3)), key=lambda k: picture3[k])
    l1 = (np.array(knowledge) + 1).tolist()
    text = '<'.join(str(i) for i in l1)

    v = list(map(lambda x: x[0] - x[1], zip(picture1, picture2)))
    L = []
    L1 = random.sample(range(1, 10), a)
    L4 = out1[0:a]
    L.append(L1)
    L.append(L1)
    L.append(L4)
    o = 0
    for l in v:
        if l > 0:
            out[L1[o]-1] = 1
        o = o + 1

    count = 0
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    for l in L:
        b = 0
        for lm in l:
            plt.subplot(3, 3, lm)
            if count == 0:
                img = img_huidu[picture1[b]]
            elif count == 1:
                img = img_huidu[picture2[b]]
            else:
                img = img_huidu[picture3[b]]
            b = b + 1
            plt.imshow(img)
            plt.axis('off')
        if count == 0:
            name0 =str(all_num)+'-'+str(count) + '.jpg'
            path_name = os.path.join(path, name0)
            plt.savefig(path_name)
            # plt.show()
            plt.clf()  # 清图
            if back==True:
                util.blend_two_images(image=path_name, background=backpic)
            name0 = name0 + ';'
        if count == 1:
            name1 = str(all_num)+'-'+str(count)  + '.jpg'
            path_name = os.path.join(path, name1)
            plt.savefig(path_name)
            # plt.show()
            plt.clf()  # 清图
            if back==True:
                util.blend_two_images(image=path_name, background=backpic)
            name1 = name1 + ';'
        if count == 2:
            name2 = str(all_num) + '-' + str(count) + '.jpg'
            path_name = os.path.join(path, name2)
            plt.savefig(path_name)
            # plt.show()
            plt.clf()  # 清图
            if back==True:
                util.blend_two_images(image=path_name, background=backpic)
            name2 = name2 + ';'

        count=count+1
    data_simple = {'img_name': name0+name1+name2, 'Text': text, 'Out': out}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def main():
    IST = 'GAMESTONE'
    json_data_list = {}

    path='./data/'
    if not os.path.exists(path):
        os.mkdir(path)

    path=path + 'game_test/'
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)

    for i in range(1000):
        json_data_list = game(path, json_data_list,back=False)
        print(i)
    json_data_dict = {IST: json_data_list}
    json_path = path + 'label.json'
    with open(json_path, "w") as f:
        json.dump(json_data_dict, f)
    print("加载入文件完成...")

if __name__ == '__main__':
    main()