import os
import json
import random
import util
import shutil
random.seed(2021)

def main():
    IST = 'SINGLERULEMATCH'
    json_data_list = {}

    path='./data/'
    if not os.path.exists(path):
        os.mkdir(path)

    path=path + 'single_rule_match_train/'
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

    n=8000//12+1

    for i in range(n):
        json_data_list = util.q0(path, json_data_list,back=False)
        json_data_list = util.q1(path, json_data_list,back=False)
        json_data_list = util.q2(path, json_data_list,back=False)
        json_data_list = util.q5(path, json_data_list,back=False)
        json_data_list = util.q6(path, json_data_list,back=False)
        json_data_list = util.q7(path, json_data_list,back=False)

        json_data_list = util.q8(path, json_data_list,back=False)
        json_data_list = util.q10(path, json_data_list,back=False)
        json_data_list = util.q11(path, json_data_list,back=False)
        json_data_list = util.q12(path, json_data_list,back=False)
        json_data_list = util.q13(path, json_data_list,back=False)
        json_data_list = util.q15(path, json_data_list,back=False)
        # json_data_list = util.q3(path, json_data_list, back=False)
        # json_data_list = util.q4(path, json_data_list, back=False)
        # json_data_list = util.q10(path, json_data_list, back=False)
        # json_data_list = util.q15(path, json_data_list, back=False)
        print(len(json_data_list))


    json_data_list = {k:v for (k,v) in json_data_list.items() if int(k)<8000}
    print(len(json_data_list))
    json_data_dict = {IST: json_data_list}


    json_path = path + 'label.json'
    with open(json_path, "w") as f:
        json.dump(json_data_dict, f)
    print("加载入文件完成...")

if __name__ == '__main__':
    main()