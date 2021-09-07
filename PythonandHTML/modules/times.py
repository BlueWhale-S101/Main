from modules import lists
import time

def timer(sec=int,min=int):
    if type(min)!=type(1) or type(sec)!=type(1):
        raise ValueError('Must be int,cannot be others.')
    if sec>=60:
        raise ValueError('"sec" Cannot >= 60.')
    if min>0:
        min = min*60
    a = min+sec
    for i in range(min+sec):
        print('',end='')
        print('\rRemaining '+str(a)+' seconds.',end='')
        time.sleep(1)
        a = a-1
    print('\rTimer ends. Remaining 0 second.')

def now_time(choice=0):
    a = time.asctime()
    b = []
    for i in a:
        b.append(i)
    day = {'Mon':'Monday','Tue':'Tuesday','Wed':'Wednesday','Thu':'Thursday','Fri':'Friday','Sat':'Saturday','Sun':'Sunday'}
    day2 = lists.list_merge(b[:3])
    date_day = day[day2]
    if choice==0:
        date = date_day +',' + lists.list_merge(b[-21:-14]) + ', ' + lists.list_merge(b[-4:]) + '  ' + lists.list_merge(b[-13:-5])
    elif choice==1:
        date = date_day + ',' + lists.list_merge(b[-21:-14]) + ', ' + lists.list_merge(b[-4:])
    elif choice==2:
        date = lists.list_merge(b[-13:-5])
    else:
        raise ValueError('Choice must be 0,1 or 2(type="int"),cannot be others.')
    return date