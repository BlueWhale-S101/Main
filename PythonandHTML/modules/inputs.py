def input_EH_Value(qustion, classes=0, i_r='Please try again:', rc=None):
    if len(qustion) == 0 or type(qustion) != type(''):
        raise ValueError('"qustion" Must be str,cannot be others.')
    if len(i_r) == 0 or type(i_r) != type(''):
        raise ValueError('"i_r" Must be str,cannot be others.')
    if rc != None and type(rc) != type([]):
        raise ValueError('"rc" Must be list,cannot be others.')
    if rc != None and classes != 3:
        raise ValueError('If you not choose 3,please don\'t write "rc".')
    a = input(qustion)
    while True:
        try:
            if classes == 0:
                b = str(a)
                break
            elif classes == 1:
                b = int(a)
                break
            elif classes == 2:
                b = float(a)
                break
            elif classes == 3:
                if rc == None:
                    raise ValueError('"rc" Cannot be NoneType!')
                elif a in rc:
                    b = a
                    break
                else:
                    pass
            else:
                raise ValueError('"classes" Must be 0,1,2 or 3(type="int"),cannot be others.')
        except ValueError:
            a = input(i_r + qustion)
    return b

def input_psw(dtsp,prompt=None,ir='Please try again: '):
    if prompt is None:
        prompt = ['Username?>>>','Password?>>>']
    if type(dtsp)!=type({}) or len(dtsp)<1:
        raise ValueError('\'dtsp\' Must be dict and it cannot be empty.')
    if type(prompt)!=type([]) or len(prompt)!=2:
        raise ValueError('\'prompt\' Must be list and length must be 2.')
    if type(ir)!=type('') or len(ir)<1:
        raise ValueError('\'ir\' Must be a string and it cannot be empty.')
    n_list = []
    for i in dtsp:
        if type(i)!=type(''):
            raise ValueError('Dtsp\'s key must be strings.')
        n_list.append(i)
    name = input_EH_Value(prompt[0], 0, ir)
    while name not in n_list:
        name = input_EH_Value(ir+prompt[0],0,ir)
    r_psw = dtsp[name]
    if type(r_psw)!=type(''):
        raise ValueError('Dtsp\'s value must be strings.')
    psw = input_EH_Value(prompt[1],0,ir)
    while psw!=r_psw:
        psw = input_EH_Value(ir+prompt[1], 0, ir)
    return name