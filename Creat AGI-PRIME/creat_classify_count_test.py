import os
import json
import random
import shutil
import util
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
random.seed(2021)

def main(back=True):
    IST = 'COUNTBYCATEGORY'
    json_data_list = {}

    path='./data/'
    if not os.path.exists(path):
        os.mkdir(path)

    path=path + 'classify_count_test/'
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)


    img_huidu = util.read_image(path='./svg-png-gray/')

    img_back = util.read_image(path='./background/')


    pictures_numbers=1000

    list=[]
    for ps in range (pictures_numbers):
        s=random.randint(1,9)
        c = random.sample(range(1,10),s)
        list.append(c)
    p0=0
    for l in list:
        picture = random.sample(range(len(img_huidu) // 9 * 8, len(img_huidu)), 9)
        LIST = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # data_simple = []
        count = 0
        ba = random.randint(0, len(img_back) - 1)
        backpic = img_back[ba]
        for i in l:
            plt.subplot(3, 3, i)
            g= random.randint(0,8)
            img = img_huidu[picture[g]]
            LIST[g]=LIST[g]+1
            plt.imshow(img)
            plt.axis('off')
            count = count + 1
        name0 = str(p0) + '-A' + '.jpg'
        path_name = os.path.join(path, name0)
        plt.savefig(path_name)
        # plt.show()
        plt.clf()  # 清图
        if back == True:
            util.blend_two_images(image=path_name, background=backpic)
        name0 = name0 + ';'
        sign=0
        cl=1
        for i in LIST:
            if i!=0:
                plt.subplot(3, 3,cl)
                img = img_huidu[picture[sign]]
                cl=cl+1
            sign=sign+1
            plt.imshow(img)
            plt.axis('off')
        name1 = str(p0) + '-B' + '.jpg'
        path_name = os.path.join(path, name1)
        plt.savefig(path_name)
        # plt.show()
        plt.clf()  # 清图
        if back == True:
            util.blend_two_images(image=path_name, background=backpic)
        name1 = name1 + ';'

        LIST=[i for i in LIST if i != 0]

        data_simple = {'img_name': name0 + name1, 'Text': '', 'Out':LIST}

        # json_data_list.append({str(p0): data_simple})
        json_data_list[str(p0)] = data_simple
        print(p0)
        p0 = p0 + 1

    json_data_dict = {IST: json_data_list}
    json_path = path + 'label.json'
    with open(json_path, "w") as f:
        json.dump(json_data_dict, f)
    print("加载入文件完成...")


if __name__ == '__main__':
    main(back=False)