import json
import os
import random
import matplotlib.pyplot as plt
import util
import shutil
import matplotlib
matplotlib.use('Agg')
random.seed(2021)

img_huidu =util.read_image(path='./svg-png-gray/')
img_back = util.read_image(path='./background/')
def numb(n,back=True):
    path= './data/not_in_memory_train'
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)
    for th in range(n*2):
        a = random.randint(1, 8)
        if a==1:
            # L1 = random.sample(range(30, len(img_huidu) ), 1)
            L1 = random.sample(range(0, len(img_huidu) - 200), 1)
        else:
            # L1 = random.sample(range(0, 30), 1)
            L1 = random.sample(range(0, len(img_huidu) - 200), 1)
            L2 = random.sample(range(0, len(img_huidu) -1), a-1)
            while L1==L2:
                L2 = random.sample(range(0, len(img_huidu) - 1), a - 1)
            for i in L2:
                L1.append(i)

        ba = random.randint(0, len(img_back) - 1)
        backpic = img_back[ba]
        b = random.randint(a, 9)
        L2 = random.sample(range(1, 10), b)
        count = 0
        for l in L2:
            plt.subplot(3, 3, l)
            img = img_huidu[L1[count]]
            if count >= len(L1) - 1:
                count = random.randint(0, len(L1) - 1)
            else:
                count = count + 1
            plt.imshow(img)
            plt.axis('off')
        name = str(th) + '.jpg'
        path_name = os.path.join(path, name)
        plt.savefig(path_name)
        plt.clf()
        if back == True:
            util.blend_two_images(image=path_name, background=backpic)
        print(th)
n =8000
numb(n,back=False)


memory_path = './data/memory_dataset/'
img_huidu0 = util.get_filename(path=memory_path,filetype = '.jpg')
not_memory_path = './data/not_in_memory_train/'
img_huidu1 =util.get_filename(path=not_memory_path, filetype = '.jpg')

def context(path,json_data_list):

    all_num = len(json_data_list)

    L1 = random.randint(0, len(img_huidu0)-1)
    L2 = random.randint(0, len(img_huidu1)-1)
    L3 = random.randint(0, len(img_huidu1)-1)
    l=random.randint(1, 3)
    if l==1:
        img0 = img_huidu0[L1]
        img1 = img_huidu1[L2]
        img2 = img_huidu1[L3]


        name0 = str(all_num) + '-' + str(1) + '.jpg'
        path_name = os.path.join(path, name0)
        shutil.copy(os.path.join(memory_path,img0), path_name)
        name0 = name0 + ';'

        name1 = str(all_num) + '-' + str(2) + '.jpg'
        path_name = os.path.join(path, name1)
        shutil.copy(os.path.join(not_memory_path,img1), path_name)
        name1 = name1 + ';'

        name2 = str(all_num) + '-' + str(3) + '.jpg'
        path_name = os.path.join(path, name2)
        shutil.copy(os.path.join(not_memory_path, img2), path_name)
        name2 = name2 + ';'

        out='F1'

    if l==2:
        img0 = img_huidu1[L2]
        img1 = img_huidu0[L1]
        img2 = img_huidu1[L3]

        name0 = str(all_num) + '-' + str(1) + '.jpg'
        path_name = os.path.join(path, name0)
        shutil.copy(os.path.join(not_memory_path, img0), path_name)
        name0 = name0 + ';'

        name1 = str(all_num) + '-' + str(2) + '.jpg'
        path_name = os.path.join(path, name1)
        shutil.copy(os.path.join(memory_path, img1), path_name)
        name1 = name1 + ';'

        name2 = str(all_num) + '-' + str(3) + '.jpg'
        path_name = os.path.join(path, name2)
        shutil.copy(os.path.join(not_memory_path, img2), path_name)
        name2 = name2 + ';'

        out='F2'
    if l==3:
        img0 = img_huidu1[L2]
        img1 = img_huidu1[L3]
        img2 = img_huidu0[L1]

        name0 = str(all_num) + '-' + str(1) + '.jpg'
        path_name = os.path.join(path, name0)
        shutil.copy(os.path.join(not_memory_path, img0), path_name)
        name0 = name0 + ';'

        name1 = str(all_num) + '-' + str(2) + '.jpg'
        path_name = os.path.join(path, name1)
        shutil.copy(os.path.join(not_memory_path, img1), path_name)
        name1 = name1 + ';'

        name2 = str(all_num) + '-' + str(3) + '.jpg'
        path_name = os.path.join(path, name2)
        shutil.copy(os.path.join(memory_path, img2), path_name)
        name2 = name2 + ';'

        out='F3'




    data_simple = {'img_name': name0+name1+name2, 'Text': '', 'Out': out}

    json_data_list[str(all_num)] = data_simple

    return json_data_list

def main():
    IST = 'Context Recalling'
    json_data_list = {}

    path='./data/'
    if not os.path.exists(path):
        os.mkdir(path)

    path=path + 'context_recall_memory_train/'
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)


    for i in range(n):
        json_data_list=context(path,json_data_list)
        print(i)

    json_data_dict = {IST: json_data_list}

    json_path = path + 'label.json'
    with open(json_path, "w") as f:
        json.dump(json_data_dict, f)
    print("加载入文件完成...")

if __name__ == '__main__':
    main()