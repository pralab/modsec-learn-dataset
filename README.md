# HTTP traffic dataset
This is the dataset used in "[Boosting ModSecurity with Machine Learning]()".

## How to cite us

If you use this dataset, please cite us:
```bibtex
```

## Using this dataset

Since GitHub does not allow files larger than 25MB, we divided them into chunks.

To rebuild the whole dataset, you can use the `merge.py` scripts in legitimate and malicious folders.
```bash
:~$ cd legitimates
:~$ python3 merge.py
:~$ cd malicious
:~$ python3 merge.py
```
