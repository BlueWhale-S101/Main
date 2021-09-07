zidian = {'Rainfall':[100,177,201],'wet':[90,93,98]}
print('字典操作11法')
print('1.定义字典')
print('原字典')
print(zidian)

print('2.取出一个值')
print(zidian['Rainfall'])

print('3.添加元素')
zidian['Temperature'] = [25,27,24]
print(zidian)

print('4.修改对应值')
zidian['Temperature'] = [26,24,29]
print(zidian)

print('5.删除字典中的元素')
zidian.pop('Temperature')
print(zidian)

print('6.遍历字典')
for n in zidian:
    print(n)
    print(zidian[n])

print('7.获取字典中所有的键值对')
obj = zidian.items()
print(obj)
for n in obj:
    print(n)

print('8.获取字典所有的键')
ks = zidian.keys()
for k in ks:
    print(k)

print('9.获取字典所有的值')
vals = zidian.values()
for v in vals:
    print(v)

print('10.获取指定键的值')
Rainfall = zidian.get('Rainfall')
print(Rainfall)
print('')
wet = zidian.get('wet',[90,93,98])
print(wet)

print('11.清空字典')
zidian.clear()
print(zidian)

print('结果展示完毕，程序结束。')