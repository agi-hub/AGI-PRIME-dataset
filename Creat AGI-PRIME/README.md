# AGI-PRIME Dataset


### Configuration requirements
- Python = 3.6.12
- PyTorch = 1.3.1

### Generation
#### Code structure
The training set and test set of each task are generated separately and saved separately. Take the example of Finding the Differences: when the training set is generated, run:
```
AGI-PRIME-dataset
├── /Creat AGI-PRIME/
│  ├── /creat_find_different.py/
```
when the test set is generated, run:
```
AGI-PRIME-dataset
├── /Creat AGI-PRIME/
│  ├── /creat_find_different_test.py/
```
#### Other details
The basic icons are saved in the svg-png-gray folder in the current directory, and the background pictures are saved in the background folder. The AGI-PRIME dataset is generated without background noise, and only the basic icons are used for generation.



### License


The project is released under the MIT license. See [LICENSE.txt](./LICENSE) for details.

