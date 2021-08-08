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

def creat_memory(path,json_data_list,listsign,back=True):
    all_num = len(json_data_list)
    a = random.randint(1, 8)
    L1 = random.sample(range(len(img_huidu)-200, len(img_huidu)), a)
    # L1 = random.sample(range(0, 30), a)
    listsign=listsign+L1
    b = random.randint(a, 9)
    L2 = random.sample(range(1, 10), b)
    count = 0
    ba = random.randint(0, len(img_back) - 1)
    backpic = img_back[ba]
    for l in L2:
        plt.subplot(3, 3, l)
        img = img_huidu[L1[count]]
        if count >= len(L1) - 1:
            count = random.randint(0, len(L1) - 1)
        else:
            count = count + 1
        plt.imshow(img)
        plt.axis('off')
    name = str(all_num) + '.jpg'
    path_name = os.path.join(path, name)
    plt.savefig(path_name)
    plt.clf()
    if back == True:
        util.blend_two_images(image=path_name, background=backpic)
    name = name + ';'
    structure_str = 'memory_dataset'
    data_simple = {'img_name': name, 'Text': '', 'Out': structure_str}
    print(all_num)
    json_data_list[str(all_num)] = data_simple
    return json_data_list,listsign


def main():
    IST = 'MEMORY-DATASET'
    json_data_list = {}

    path='./data/'
    if not os.path.exists(path):
        os.mkdir(path)

    path=path + 'memory_dataset/'
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)
    listsign=[]
    n=100
    for i in range(n):
        json_data_list,listsign=creat_memory(path,json_data_list,listsign,back=False)


    json_data_dict = {IST: json_data_list}
    json_path = path + 'label.json'
    with open(json_path, "w") as f:
        json.dump(json_data_dict, f)
    print("加载入文件完成...")

    result_json_data_dict = {'result': listsign}
    result_json_path = path + 'listsign.json'
    with open(result_json_path, "w") as f:
        json.dump(result_json_data_dict, f)

if __name__ == '__main__':
    main()


