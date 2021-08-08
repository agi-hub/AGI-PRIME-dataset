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


def obre(path,p,json_data_list,back=False):

    result_json_path = './data/memory_dataset/listsign.json'
    with open(result_json_path, "r") as f:
        load_dict = json.load(f)
    listsign = load_dict['result']
    listsign=list(set(listsign))
    out=[0,0,0,0,0,0,0,0,0]
    all_num = len(json_data_list)
    a = random.randint(1, 8)
    L1 = random.sample(range(0, len(img_huidu)), a)
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    b = random.randint(a, 9)
    L2 = random.sample(range(1, 10), b)
    count = 0
    for l in L2:
        plt.subplot(3, 3, l)
        img = img_huidu[L1[count]]
        if L1[count] in listsign:
            out[l - 1] = 1
        if count >= len(L1) - 1:
            count = random.randint(0, len(L1) - 1)
        else:
            count = count + 1
        plt.imshow(img)
        plt.axis('off')
    name = str(p) + '.jpg'
    path_name = os.path.join(path, name)
    plt.savefig(path_name)
    plt.clf()
    if back==True:
        util.blend_two_images(image=path_name, background=backpic)
    name = name + ';'
    data_simple = {'img_name': name, 'Text': '', 'Out': out}
    json_data_list[str(all_num)] = data_simple
    return json_data_list

def main():
    IST = 'Objects Recalling'
    json_data_list = {}

    path='./data/'
    if not os.path.exists(path):
        os.mkdir(path)

    path=path + 'object_memory_train/'
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)
    n=8000
    for i in range(n):
        json_data_list=obre(path,i,json_data_list,back=False)

    json_data_dict = {IST: json_data_list}
    json_path = path + 'label.json'
    with open(json_path, "w") as f:
        json.dump(json_data_dict, f)
    print("加载入文件完成...")

if __name__ == '__main__':
    main()