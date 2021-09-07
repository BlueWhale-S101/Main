print('列表操作12法')
print('1、列表定义')
liebiao = ['Ctrl','Shift','Alt','Backspace','Esc']
print('原列表')
print(liebiao)

print('2、列表索引')
print(liebiao[0])
print(liebiao[1])
print(liebiao[-1])
print(liebiao[-2])

print('3、列表取值')
print(liebiao[2])

print('4、修改列表中的元素')
liebiao[4] = 'Tab'
print(liebiao)

print('5、向列表中追加元素')
liebiao.append('Backspace')
print(liebiao)

print('6、删除列表中的元素')
liebiao.remove('Alt')
print(liebiao)

print('7、向列表的指定位置添加元素')
liebiao.insert(2,'Esc')
print(liebiao)

print('8、查询列表中指定元素的位置')
print(liebiao)
print(liebiao.index('Backspace'))

print('9、反转列表')
print(liebiao)
liebiao.reverse()
print(liebiao)

print('10、列表切片')
print(liebiao[0:2])
print(liebiao[-4:-2])
print(liebiao[-4:3])
print(liebiao[3:])
print(liebiao[:3])
print(liebiao[:])

print('11、遍历列表')
for n in liebiao:
    print(n)

print('12、清空列表')
liebiao.clear()
print(liebiao)