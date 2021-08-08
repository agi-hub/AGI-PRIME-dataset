import os
import sys
rootPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(rootPath)[0]
sys.path.append(rootPath)
import json
import random
import util
import shutil
import matplotlib
matplotlib.use('Agg')
random.seed(2021)

def main(back=True):
    IST = 'FINDDIFFERENCE'
    json_data_list = {}

    path='./data/'
    if not os.path.exists(path):
        os.mkdir(path)

    path=path + 'find_differents_test/'
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)
    pictures_numbers=1000

    for i in range(pictures_numbers):
        json_data_list = util.size_find(path, json_data_list, back=False)

    json_data_dict = {IST: json_data_list}
    json_path = path + 'label.json'
    with open(json_path, "w") as f:
        json.dump(json_data_dict, f)
    print("加载入文件完成...")



if __name__ == '__main__':
    main(back=False)