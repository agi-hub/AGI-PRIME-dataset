# AGI-BABY Dataset


### Configuration requirements
- Python = 3.6.12
- PyTorch = 1.3.1
- mxnet = 1.7.0

### Instructions

#### 1. Deep neural network
#### 1.1 Direct training
1. Using ResNet18+LSTM structure, each task has a separate folder, and the folder path is as follows:
```
agi_baby
├── /baseline/
│  ├── /classify_count/
│  │  └──  main.py
│  │...
```
2. Modify the corresponding task main.py Data set path inside
3. Run the corresponding task main.py file
eg:
```
python main.py
```
#### 1.2 transfer

1. E.g FDT ---> CCT
    Run the corresponding task main file eg 10:
   ```
   python main_10.py
   ```


#### 2. Pre-programmed reasoning logic with vision fea-ture extraction network
#### 2.1 MOCO

1. Using MOCO as feature extraction network, each task is a separate Python file, and the file path is as follows:
```
agi_baby
├── /AGI_BABY_lib_MOCO/
│  ├── find_differents.py
│  │...
```
2. Modify the dataset path in the corresponding task Python
3. Run the python file of the corresponding task
eg:
```
python find_differents.py
```

##### 2.2 our
1. Using our own mxnet network as the feature extraction network, each task is a separate Python file. The file path is as follows:
```
agi_baby
├── /AGI_BABY_lib/
│  ├── find_differents.py
│  │...
```
2. Modify the dataset path in the corresponding task Python
3. Run the python file of the corresponding task
eg:
```
python find_differents.py
```



### License


The project is released under the MIT license. See [LICENSE.txt](./LICENSE) for details.

