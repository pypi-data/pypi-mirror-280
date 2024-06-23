# Introduction
## Install package
```shell
pip install cn_detect
```
##  Example Usage:
```python
from cn_detect.detect import ChineseNameDetect

# Basic
detector = ChineseNameDetect() 
detector.recognize_excel_by_column(excel_file_path='myfile.xlsx', column='Name')

# Use your own family name list, and the family_name_file must be *.txt file
detector = ChineseNameDetect(family_name_file='family_name.txt')
detector.recognize_excel_by_column(excel_file_path='myfile.xlsx', column='Name')
```
