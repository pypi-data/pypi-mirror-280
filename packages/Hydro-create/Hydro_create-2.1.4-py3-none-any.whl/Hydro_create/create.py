from pandas import DataFrame as df 
from xpinyin import Pinyin
import pandas as pd
import os
p = Pinyin()
name = ""

try:
    os.makedirs("excel")
    print("初始化成功")
except:
    print("excel目录已存在")
try:
    open("name.in","r").close()
except:
    open("name.in","w").close()
    print("name.in 文件已存在")

def get(data,code,x):
    if "电话" in data:
        return data["电话"][x]
    else:
        return data["用户名"][x]+code

def transform(data):
    global p
    data["用户名"] = []
    data["密码"] = []
    data["账号导入"] = []
    scode = ""
    suffix = input("请输入后缀:")
    code = input("请输入密码后缀: ")
    school = ""
    if suffix!="":
        suffix = "_"+suffix
    #scode = get(data)
    siz = len(data["姓名"])
    lst = []
    
    if "学校" not in data:
        school = input("请输入学校:")
        if school !="":
            data["学校"] = ["" for i in range(siz)]
    data["用户名"] = ["" for i in range(siz)]
    data["密码"] = ["" for i in range(siz)]
    data["账号导入"] = ["" for i in range(siz)]
    for i in range(siz):
        name = data["姓名"][i]
        pinyin = p.get_pinyin(name)
        pinyin = "".join(pinyin.split("-"))
        # 1.用户名
        user = pinyin
        data["用户名"][i] = user
        
        #  2.密码 获取用户名+后缀 或者 手机号
        _code = get(data,code,i)
        data["密码"][i] = _code
        user = user+suffix
        data["用户名"][i] = user
        
        # 3. 学校
        _school = ""
        if school!="":
            data["学校"][i] = school
        if "学校" in data:
            _school = r',{"school":"%s"}'%(data["学校"][i])
        s = "%s@qq.com,%s,%s,%s%s"%(user,user,_code,data["姓名"][i],_school)
        data["账号导入"][i] = s
        lst.append(s)
    name = open("账号导入1","w",encoding='utf-8')
    name.write("\n".join(lst))
    name.write("\n")
    name.close()
    return data



def run():
    data = {"姓名":[]}
    name = open("name.in","r",encoding = 'utf-8')
    lst = name.readlines()
    for i in range(len(lst)):
        if lst[i][-1]=="\n":
            lst[i] = lst[i][:-1]
        data["姓名"].append(lst[i])
    data = transform(data)
    df(data).to_excel("excel/用户信息.xlsx",index=False,sheet_name="学生信息")
    print("创建成功")
def readexc(Name = True,sheet=0):
    global name

    name = input("请输入文件名")
    file = pd.read_excel(r'excel/%s.xlsx'%(name),sheet)
    data = {}
    for i in file.loc[0].index:
        data[i] = []
    for i in data:
        data[i] = list(file[i])
    try:
        data["姓名"]
    except:
        print("不存在姓名字段")
        if Name:
            return False
    return data
def run1():
    data = readexc()
    data = transform(data)
    global name
    #name = "用户信息"
    pd.DataFrame(data).to_excel("excel/%s账号.xlsx"%(name),index = False,sheet_name="学生信息")
    print("excel/%s账号.xlsx 创建成功"%(name))

def Course1(sheet = None):
    Id = input("请输入题号标签(比如在表格内题号在open栏则输入open learn则输入learn)")
    if sheet == None:
        sheet = input("请输入表名")
    data = readexc(False,sheet = sheet)
    for i in data:
        if Id == i:
            print(i)
    lst = []
    title = {}
    tot = 1
    for i in range(len(data["章节"])):
        y = data["章节"][i]
        if type(y)!=str:
            y = lst[-1]
            print(y)
            data["章节"][i] = y
        else:
            #print("name",y)
            title[y] = {}
            title[y]["_id"] = tot
            title[y]["title"] = y
            lst.append(y)
            title[y]["lecture"] = "本章讲义"
            title[y]["pids"] = []
    for i in range(len(data["章节"])):
        x = data[Id][i]
        head = data["章节"][i]
        if pd.isna(head) or pd.isna(x):
            continue;
        title[head]["pids"].append(int(x))
    Lst = []
    for i in lst:
        if len(title[i]["pids"])==0:
            del title[i]
            continue
        title[i]["_id"]=tot
        tot+=1
        Lst.append(str(title[i]))
    a = open("out.out","w",encoding = 'utf-8')
    x = ",\n".join(Lst).replace("\'","\"")
    print(x)
    a.write("[%s]"%(x))
    a.close()
    return title



def Course2(sheet = None ):
    Id = input("请输入是open还是learn")
    if Id!="open" and Id !="learn":
        print("输入错误程序结束")
        return False
        
    data = readexc(False,sheet = "New P3")
    for i in data:
        if Id == i:
            print(i)
    lst = []
    title = {}
    tot = 1
    for i in range(len(data["章节"])):
        y = data["章节"][i]
        if type(y)!=str:
            y = lst[-1]
            print(y)
            data["章节"][i] = y
        else:
            #print("name",y)
            title[y] = {}
            title[y]["_id"] = tot
            tot+=1
            title[y]["title"] = y
            lst.append(y)
            title[y]["lecture"] = "本章讲义"
            title[y]["pids"] = []
    for i in range(len(data["章节"])):
        if ch=="课例题":
            if data["题目类型"][i]!="课例题":
                continue
        else:
            if data["题目类型"][i]=="课例题":
                continue
        x = data[Id][i]
        head = data["章节"][i]
        if pd.isna(head) or pd.isna(x):
            continue;
        title[head]["pids"].append(int(x))
    Lst = []
    for i in lst:
        if len(title[i]["pids"])==0:
            continue
        Lst.append(str(title[i]))
    a = open("out.out","w",encoding = 'utf-8')
    x = ",\n".join(Lst).replace("\'","\"")
    print(x)
    a.write("[%s]"%(x))
    a.close()
    return title