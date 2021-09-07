import random,time

while True:
    print('''————————————————————————————————————————————————————————————
游戏规则：有编号为1～4的4个位置，每个回合里双方分别会随机站在一个位置。
猜对对方所在的位置的编号才能有效攻击对方，连续猜对3次及以上会触发技能，增加攻击力；连续猜对5次及以上可一吸对方10点血。
当有一方的血量小于或等于0时，一局游戏结束，血量小于或等于0的一方输。玩家可选择是否再来一局。''')
    time.sleep(5)
    print('\n敌我战力公告:\n敌方:\n  血量：100\n  普通攻击力：10\n  技能攻击力：20\n我方：\n  血量：120\n  普通攻击力：8\n  技能攻击力：24')
    time.sleep(4)
    print('\n大战即将开始！准备！')
    
    time.sleep(0.5)
    p_l = 120
    e_l = 100
    p_t = 0
    e_t = 0
    time.sleep(1.5)
    while p_l > 0 and e_l > 0:
        p_st = random.randint(1,4)
        e_st = random.randint(1,4)
        while e_st==p_st:
            e_st = random.randint(1,4)
        print('————————————————————————————————————————————————————————————')
        time.sleep(1)
        print('你的位置：%d；\n双方信息：\n  玩家：\n    血量：%d/120，连击：%d；\n  敌人：\n    血量：%d/100，连击：%d。' % (p_st,p_l,p_t,e_l,e_t))
        xzlb = ['1','2','3','4']
        xzlb.remove(str(p_st))

        time.sleep(2)
        cic = input('\n请选择攻击目标位置：'+str(xzlb)+'>>>')
        while True:
            try:
                int(cic)
                if cic not in xzlb:
                    cic = input('输入错误，请选择攻击目标位置：' + str(xzlb) + '>>>')
                else:
                    break
            except ValueError:
                cic = input('输入错误，请选择攻击目标位置：'+str(xzlb)+'>>>')
        print('————————————————————————————————————————————————————————————\n')
        if int(cic)==e_st:
            p_t = p_t+1
            if p_t>=3:
                e_l = e_l-24
                print('玩家已触发技能，【敌人】剩余血量%d！' %e_l)
            else:
                e_l = e_l-8
                print('玩家发起攻击，【敌人】剩余血量%d！' %e_l)
        else:
            p_t = 0
            print('噢，不！你没猜中敌方位置！攻击无效！连击重置！')
        if  e_l <= 0:
            print('')
            break
        if p_t>=5 and p_l<120 and e_l>10:
            e_l-=10
            p_l+=10
            print('玩家触发吸血，【敌人】剩余血量%d，【玩家】剩余血量%d！' % (e_l,p_l))
        time.sleep(1.5)
        
        xzl = ['1','2','3','4']
        xzl.remove(str(e_st))
        e_xz = random.randint(0,1)
        if xzl[e_xz] == str(p_st):
            e_t = e_t+1
            if e_t>=3:
                p_l = p_l-20
                print('敌人已触发技能，【玩家】剩余血量%d！' %p_l)
            else:
                p_l = p_l-10
                print('敌人发起攻击，【玩家】剩余血量%d！' %p_l)
        else:
            e_t = 0
            print('Yes！敌人攻击无效也！')

        if e_t >= 5 and e_l < 100 and p_l > 10:
            p_l -= 10
            e_l += 10
            print('敌人触发吸血，【玩家】剩余血量%d，【敌人】剩余血量%d！')
        print('')
        time.sleep(2)


    print('————————————————————————————————————————————————————————————')
    if p_t == 0:
        print('\n噢，不！你输了！\n')
    elif e_t == 0:
        print('\n耶！敌人输了也！\n')
    print('————————————————————————————————————————————————————————————')
    xz = input('要不要再来一局？要输1，不要输其他信息。>>>')
    if xz != '1':
        print('————————————————————————————————————————————————————————————')
        break
    else:
        print('正在初始化游戏，请稍等。\n')
        time.sleep(2.5)