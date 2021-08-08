import os
import json
import random
import util1
import util
import shutil
random.seed(2021)


def main():
    IST = 'APPLYOPERATOR'
    json_data_list = {}

    path='./data/'
    if not os.path.exists(path):
        os.mkdir(path)

    path=path + 'math_apply_test/'
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)
    rules = ['+','-','*','**','>','<']
    rules=set(rules)
    rules=sorted(rules)


    util.text_save(os.path.join(path,'rule.txt'), rules)
    n=1000//6+1
    for i in range(n):
        json_data_list = util1.math_match(path,json_data_list,mode=2,back=False)
        print(i)
    json_data_list = {k: v for (k, v) in json_data_list.items() if int(k) < 1000}
    json_data_dict = {IST: json_data_list}
    json_path = path + 'label.json'
    with open(json_path, "w") as f:
        json.dump(json_data_dict, f)
    print("加载入文件完成...")

if __name__ == '__main__':
    main()