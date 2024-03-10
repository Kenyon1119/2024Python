students=[{'國文': 55, '數學': 92, '英文': 66},
          {'國文': 90, '數學': 52, '英文': 74},
          {'國文': 62, '數學': 66, '英文': 73},
          {'國文': 82, '數學': 97, '英文': 77},
          {'國文': 90, '數學': 59, '英文': 91},
          {'國文': 65, '數學': 50, '英文': 64},
          {'國文': 55, '數學': 88, '英文': 65},
          {'國文': 100, '數學': 55, '英文': 94},
          {'國文': 56, '數學': 55, '英文': 84},
          {'國文': 76, '數學': 76, '英文': 81},
          {'國文': 73, '數學': 61, '英文': 97},
          {'國文': 61, '數學': 80, '英文': 50},
          {'國文': 75, '數學': 100, '英文': 84}]

#open()，file物件實體使用open內建function
#csv module 建立實體(初始化initializer)

import csv

#建立file實體，這個實體會自動關閉close()->with...as
fieldname = input('請輸入檔案名稱:')
csvname = f'{fieldname}.csv'
with open(csvname,mode='w',encoding='utf-8',newline='') as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=['國文','數學','英文'])
    writer.writeheader()
    writer.writerows(students)

print(f'{csvname}.csv存檔完成')    
##class csv.DictWriter()
##整合式終端機執行
