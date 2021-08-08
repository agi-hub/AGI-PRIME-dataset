import os
import json
import random
import util
import shutil
random.seed(2021)
def main():
    IST = 'Single-rule Learning'
    json_data_list = {}

    path='./data/'
    if not os.path.exists(path):
        os.mkdir(path)

    path=path + 'single_rule_match_test/'
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)
    rules = ['number-progression','type-progression','size-progression','color-progression',
            'type-xor','size-xor','color-xor','position-xor',
            'type-or','size-or','color-or','position-or',
            'type-and','size-and','color-and','position-and']
    rules=set(rules)
    rules=sorted(rules)


    util.text_save(os.path.join(path,'rule.txt'), rules)

    for i in range(250):
        json_data_list = util.q3(path, json_data_list,back=False)
        json_data_list = util.q4(path, json_data_list,back=False)
        json_data_list = util.q10(path, json_data_list,back=False)
        json_data_list = util.q15(path, json_data_list,back=False)
        print(len(json_data_list))

    json_data_dict = {IST: json_data_list}
    json_path = path + 'label.json'
    with open(json_path, "w") as f:
        json.dump(json_data_dict, f)
    print("加载入文件完成...")

if __name__ == '__main__':
    main()