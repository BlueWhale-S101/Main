import random
from modules import inputs
import time
fenshu = 0
tx = '输入错误，请重新输入：'

print("来测一下算术正确率吧！")
time.sleep(0.5)
fh = inputs.input_EH_Value("选择一个符号吧~(+,-,*,/)>>>", 3, tx, ['+', '-', '*', '/'])
small = int(inputs.input_EH_Value("输入难度最小值~>>>", 1, tx, ))
big = int(inputs.input_EH_Value('输入难度最大值~>>>', 1, tx))
while big<=small:
    big = int(inputs.input_EH_Value('最大值要大于最小值~输入难度最大值~>>>', 1, tx))
times2 = int(inputs.input_EH_Value('输入作答题目数量~>>>', 1, tx))
while times2<5:
    times2 = int(inputs.input_EH_Value('至少要有五次哦~输入重复次数~>>>', 1, tx))

time.sleep(2)
print('——————————————————————————————————————————————————')
times = 1
start = time.time()
while times < times2+1:
    time.sleep(0.5)
    num1=random.randint(small,big)
    num2=random.randint(small,big)
    print('第 %d/%d 题：' % (times,times2))
    time.sleep(0.5)
    if fh=="+":
        into = inputs.input_EH_Value("%d加%d等于几？>>>" % (num1,num2), 1, tx)
        num1 = int(num1)
        num2 = int(num2)
        daan = num1+num2
    elif fh=="-":
        into = inputs.input_EH_Value("%d减%d等于几？>>>" % (num1,num2), 1, tx)
        num1 = int(num1)
        num2 = int(num2)
        daan = num1-num2
    elif fh=="*":
        into = inputs.input_EH_Value("%d乘%d等于几？>>>" % (num1,num2), 1, tx)
        num1 = int(num1)
        num2 = int(num2)
        daan = num1*num2
    else:
        into = inputs.input_EH_Value("%d除%d等于几？>>>" % (num1,num2), 2, tx)
        int(num1)
        int(num2)
        daan = num1/num2
    time.sleep(1)
    if into == daan:
        print("好厉害，做对了！")
        fenshu = fenshu+(100/times2)
    else:
        print("好可惜，答错了！正确答案是："+str(daan))
    times = times+1
    time.sleep(1.5)
    print('——————————————————————————————————————————————————')

end = time.time()
long = int(end-start)
time.sleep(1)
print('你本次选择测试的符号为：'+fh+' 号；')
print('你本次选择的难度范围：'+str(small)+'~'+str(big)+'；')
print('你本次作答题目数量：'+str(times2)+' 题；')
time.sleep(0.5)
print("你本次作答得分为："+str(fenshu)+' 分；')
print('你本次做对题目数量：'+str(int(fenshu/(100/times2)))+' 题；')
print('你本次做错题目数量：'+str(int((100-fenshu)/(100/times2)))+' 题；')
time.sleep(0.5)
print('你本次作答用时：'+str(long-(3.5*times2))+' 秒；')
print('你本次做答平均每题用时：'+str((long-(3.5*times2))/times2)+' 秒。')