import csv

fl = open('1.csv','w',newline='',encoding='utf-8')
# 创建“csv”文件，定义模式、编码方式及空行
wrt = csv.writer(fl)  # 创建“writer”（写入）对象
wrt.writerow(['1'])
wrt.writerow(['2','3'])
wrt.writerow(['4','5'])  # 写入一行数据（单层表格）
fl.close()  # 保存

fl = open('1.csv','r',newline='',encoding='utf-8')
# 打开“csv”文件
rd = csv.reader(fl)  # 创建“reader"（读取）对象
for i in rd:
    print(i)  # 读取每一行的数据（单层表格）并输出