import os
import json
import random
import util
import shutil
random.seed(2021)

def main():
    IST = 'Multi-rule Learning'
    json_data_list = {}

    path='./data/'
    if not os.path.exists(path):
        os.mkdir(path)
    path = path + 'many_rule_match_train/'

    if not os.path.exists(path):
        os.mkdir(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)
    n=100
    for i in range(n):
        json_data_list = util.type_to(path,json_data_list,mode=1,back=False)
        json_data_list = util.color_to(path,json_data_list,mode=1,back=False)
        json_data_list = util.size_to(path,json_data_list,mode=1,back=False)
        

    json_data_dict = {IST: json_data_list}
    json_path = path + 'label.json'
    with open(json_path, "w") as f:
        json.dump(json_data_dict, f)
    print("加载入文件完成...")

if __name__ == '__main__':
    main()