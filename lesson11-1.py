import pyinputplus as pyip #猴子使用者亂輸入
import random   #內建套件
from pprint import pprint   #呼叫排序輸出pprint
nums=pyip.inputInt(f"請輸入學生數量:")
students:list[dict]=[]  #List
for _ in range(nums): #迴圈 0-49，共50圈
    student:dict[str,int]={}    #形容並建值50組
    for subject in ['國文','英文','數學']:
        student[subject]=random.randint(50,100) 
    students.append(student)
pprint(students)
##執行請在終端機輸入python 路徑及檔案名稱lesson11-1.py
