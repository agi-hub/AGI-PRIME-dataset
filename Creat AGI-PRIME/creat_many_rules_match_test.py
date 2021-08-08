import os
import json
import util
import shutil
import random
random.seed(2021)

def main():
    IST = 'FINDMULTRULE'
    json_data_list = {}

    path = './data/'
    if not os.path.exists(path):
        os.mkdir(path)
    path = path + 'many_rule_match_test/'

    if not os.path.exists(path):
        os.mkdir(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)
    n = 1000 // 80 + 1
    for i in range(n):
        json_data_list = util.type_to(path, json_data_list,mode=2,back=False)
        json_data_list = util.color_to(path, json_data_list,mode=2,back=False)
        json_data_list = util.size_to(path, json_data_list,mode=2,back=False)
    json_data_list = {k: v for (k, v) in json_data_list.items() if int(k) < 1000}
    json_data_dict = {IST: json_data_list}
    json_path = path + 'label.json'
    with open(json_path, "w") as f:
        json.dump(json_data_dict, f)
    print("加载入文件完成...")


if __name__ == '__main__':
    main()