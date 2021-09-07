import time,random,keyboard
a = []
a.insert(0,'|')
a.insert(0,'|')
a.insert(2,'[')
for z in range(34):
    times = random.randint(1,4)
    if times==1:
        a.append('[')
    else:
        a.append('|')
print('\r_________________________________________________________________________________')
print('''\r欢迎挑战超坑眼力+反应测试游戏！下面是游戏介绍：
游戏开始后，注意看好了：代表你的符号“//>”前(刻度0）如果是“|”，请不要按键；如果是“[”，按下
ctrl就行啦!按错失败哟~
为了保证页面的整体效果，操作区为全英文~
还有刻度可以让你预测什么时候要按，每0.5秒符号向前移动一次（详细操作时看）~
写着“The specified key pressed?”的刻度是表示在上次系统是否感应到ctrl+space两键是否都已
按下~
“Keep time”刻度表示你坚持的时间秒数~

下面，请选择难度~ 1代表较难难，2代表简单~
''')
hard = 0
while hard!=1 and hard!=2:
    hard = int(input('请在这输入>>>'))

time.sleep(1)
print('\r_________________________________________________________________________________')
print('\ryou|0        |10       |20       |30   |end |The specified key pressed?|Keep time')
print('\r   0 2 4 6 8 0 2 4 6 8 0 2 4 6 8 0 2 4 6    |                          |')
print('\r//>Ready?',end='')
time.sleep(1)
print('\r//>Go!',end='')
time.sleep(0.2)
e = '|'
timer = 0
while True:
    if hard==1:
        time.sleep(0.35)
    else:
        time.sleep(0.5)
    d = ''
    for i in a:
        d+=i
    psd = str(keyboard.is_pressed('ctrl'))
    if (e=='[' and psd=='True') or (e=='|' and psd=='False'):
        if psd=='True':
            psd+=' '
        print('\r'+'//>'+d+'    '+psd+'                      '+str(timer)+'sec',end='')
        u = d
    else:
        if psd=='True':
            psd+=' '
        print('\r//>'+u+'    '+psd+'                      '+str(timer)+'sec')
        print('\r_________________________________________________________________________________')
        print('\r//>'+e+'    The specified key pressed='+psd)
        print('\rYou made a mistake after keeping it for '+str(timer)+' seconds.')
        print('\r_________________________________________________________________________________')
        break
    if hard==1:
        timer+=0.35
    else:
        timer+=0.5
    e = a[0]
    a = a[1:]
    c = random.randint(1,4)
    if c == 1:
        b = '['
    else:
        b = '|'
    a.insert(-1,b)