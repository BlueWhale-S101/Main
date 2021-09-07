import openpyxl as exl
import csv

def write_CSVlist(name,list):
    if type(name)!=type(''):
        raise ValueError('The file name must be "str",cannot be others.')
    if type(list)!=type([]):
        raise ValueError('Write content must be "list",cannot be others.')
    c = []
    for i in name:
        c.append(i)
    if c[-4:] != ['.','c','s','v']:
        print(c[-4:])
        raise ValueError('The file format must be  .csv file,cannot be other types of files.')
    with open(name,'a',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(list)

def read_CSVlist(name):
    if type(name)!=type(''):
        raise ValueError('The file name must be "str",cannot be others.')
    c = []
    for i in name:
        c.append(i)
    if c[-4:] != ['.', 'c', 's', 'v']:
        print(c[-4:])
        raise ValueError('The file format must be  .csv file,cannot be other types of files.')
    with open(name, newline='', encoding='utf-8') as f:
        reads = csv.reader(f)
        value = []
        for a in reads:
                value.append(a)
    return value


def write_XLSXlist(name,list,sheetname=None,renamesheet=None,renamelist=None):
    if type(name)!=type(''):
        raise ValueError('The file name must be "str",cannot be others.')
    if type(list)!=type([]):
        raise ValueError('Write content must be "list",cannot be others.')
    if type(sheetname)!=type('') and type(sheetname)!=type(None):
        raise ValueError('Sheet name must be a strange or None(use activity table),cannot be others.')
    if type(renamesheet)!=type('') and type(renamesheet)!=type(None):
        raise ValueError('New sheet name must be a strange or None(do not rename),cannot be others.')
    if type(renamelist)!=type('') and type(renamelist)!=type(None):
        raise ValueError('New list name must be a strange or None(do not rename),cannot be others.')
    c = []
    for i in name:
        c.append(i)
    if c[-5:] != ['.', 'x', 'l', 's','x']:
        print(c[-5:])
        raise ValueError('The file format must be  .xlsx file,cannot be other types of files.')
    wb = exl.load_workbook(name)
    if sheetname is None:
        sht = wb.active
    else:
        sht = wb[sheetname]
    if renamesheet is not None:
        sht.title = '1st'
    if type(list[0])!=type([]):
        if list[0]==None:
            sht[list[1]]=list[2]
        else:
            sht.append(list)
    else:
        for i in list:
            sht.append(i)
    if renamelist is None:
        wb.save(name)
    else:
        wb.save(renamelist)

def read_XLSXlist(name,cell,sheetname=None):
    if type(name)!=type(''):
        raise ValueError('The file name must be "str",cannot be others.')
    if type(sheetname)!=type('') and type(sheetname)!=type(None):
        raise ValueError('Sheet name must be a strange or None(use activity table),cannot be others.')
    if type(cell)!=type(''):
        raise ValueError('The cell name must be "str",cannot be others.')
    c = []
    for i in name:
        c.append(i)
    if c[-5:] != ['.', 'x', 'l', 's', 'x']:
        print(c[-5:])
        raise ValueError('The file format must be  .xlsx file,cannot be other types of files.')
    wb = exl.load_workbook(name)
    if sheetname is None:
        sht = wb.active
    else:
        sht = wb[sheetname]
    out = sht[cell].value
    wb.save(name)
    return out