import importlib as Import
import threading as thread
import random as ran
from cyaron import *
import copy
import subprocess as sub
import zipfile,os

_pre = 0
prename = ""
file = ""
def per(id,tot):
    global _pre
    return int((id-_pre)/(tot-_pre)*100)
def Rename(origin,new):
     os.rename(origin,new)
def rename(origin,new,num=10):
    src = r'test/'
    origin = src+origin
    new = src+new
    for i in range(num+1):
        try:
            orgin_in = r'%s%d.in'%(origin,i)
            orgin_out = r'%s%d.out'%(origin,i) 
            new_in = r'%s%d.in'%(new,i)
            new_out = r'%s%d.out'%(new,i)
        except:
            1
        try:
            
            orgin_in = r'%s0%d.in'%(origin,i)
            orgin_out = r'%s0%d.out'%(origin,i) 
            new_in = r'%s%d.in'%(new,i)
            new_out = r'%s%d.out'%(new,i)
        except:
            1
            
def check(file):
    x = file.readlines()
    for i in x:
        p = i.split(" ")
        for j in p:
            try:
                if float(j)<0:
                    return True
            except:
                1
    return False
def exzip(filename):
    global prename
    zip_ref = zipfile.ZipFile(r'test/%s.zip'%(filename),'r')
    zip_ref.extractall('test/')
    zip_ref.close()
def delzip(filename):
    try:
        sub.check_call(r'rm test/%s.zip'%(filename),shell = True,stdout=None)
    except:
        1
        

def zip_rename(N,Pre=0,newname = ""):
    global prename,file
    zipname = input("请输入压缩包文件名（不带.zip）")
    filename = input("请输入测点文件前缀名")
    exzip(zipname)
    file = filename
    prename = zipname
    rename(filename,"",num=N)
    prename = newname
    try:
        delzip(zipname)
    except:
        print("压缩包删除失败")
    try:
        delzip("rename")
    except:
        print("之前压缩包删除失败")
    
    mkzip(pre = Pre,n=N+1,name = "rename")
    print("重命名成功")
def Mkzip(zip_file,origin,target):
    zip_file.write(origin,compress_type=zipfile.ZIP_DEFLATED,arcname=target)
def mkzip(n = 16,pre = 0,name = "new"):
    global prename
    zip_file = zipfile.ZipFile(r'test/%s.zip'%(name),'w')
    # 把zfile整个目录下所有内容，压缩为new.zip文件
    # zip_file.write('c.txt',compress_type=zipfile.ZIP_DEFLATED)
    print(prename)
    for i in range(pre+1,n+1):
        try:
            os.rename(r'test/%d.in'%(i),r'test/%s%d.in'%(prename,i))
            os.rename(r'test/%d.out'%(i),r'test/%s%d.out'%(prename,i))
        except:
            try:
                os.rename(r'test/0%d.in'%(i),r'test/%s%d.in'%(prename,i))
                os.rename(r'test/0%d.out'%(i),r'test/%s%d.out'%(prename,i))
            except:
                print("%d输入输出文件不存在"%(i))
    for i in range(pre+1,n):
                
        try:
            a = open(r'test/%s%d.out'%(prename,i),"r")
            #print("check is ",check(a))
            if check(a):
                print(r'test/%d.out has a negative value'%(i))
            a.close()
            
            
            origin = r'test/%s%d.in'%(prename,i)
            target = r'%s%d.in'%(prename,i)
            Mkzip(orgin,target)
            
            origin = r'test/%s%d.out'%(prename,i)
            target = r'%s%d.out'%(prename,i)
            Mkzip(orgin,target)
            
        except:
            print("test%d不存在"%(i))
        sub.check_call(r'rm test/%s%d.in'%(prename,i),shell = True,stdout=None)
        sub.check_call(r'rm test/%s%d.out'%(prename,i),shell = True,stdout=None)
    zip_file.close()     
    print("finish")
def rebuild(lst):
    arr = []
    for i in lst:
        if type(i)!=list:
            arr.append(i)
        else:
            temp = []
            for j in i:
                if type(j)==list:
                    if temp:
                        arr.append(temp)
                    temp = []
                    arr.append(j)
                else:
                    temp.append(j)
            if temp:
                arr.append(temp)
    return arr
            
class Ysrmaking:
    import subprocess as sub
    example = None
    stderr = None
    stdout = None
    lst = []
    cmd = None
    pre = 0

    def Cmd(self,cmd):
        try:
            print(cmd)
            return self.sub.check_output(cmd,shell="True")
        except:
            print("%s已存在"%(cmd))
    def __init__(self,lst=None,cmd = None):
        if cmd == None:
            cmd = self.Cmd
        #不通过文件则pip安装
        if lst ==None:
            lst = ["mkdir","touch"]
        self.lst = lst
        self.cmd = cmd
        self.cmd(r'%s Std'%(lst[0]))
        self.cmd(r'%s test'%(lst[0]))
        self.cmd(r'%s Std/sample.py'%(lst[1]))
        self.cmd(r'%s Std/std.cpp'%(lst[1]))         
        try:
            self.example = Import.import_module("Std.sample")
        except:
            print("not")
    def Compile(self,remove = True):
        try:
            self.cmd(r'g++ Std/std.cpp -o Std/std')
            if remove:
                try:
                    a = self.sub.check_call(r'rm -rf test',shell = True,stdout=None)
                    print(s)
                except:
                    print("文件不存在")
                self.cmd(r'%s test'%(self.lst[0]))
        except:
            print("标程编译错误")
            return "标程编译错误"
        
    def remake_data(self,n = 16,pre = 0,close =False):
        zip_rename(N=n,newname = "new")
        global _pre,prename,file
        file = "rename"
        filename = file
        prefix = "new"
        _pre = pre
        self.Compile(False)
        prename = prefix
       
        if prefix=="":
            prefix = "temp"
        if filename=="":
            filename = prename
        try:
            exzip(filename)
        except:
            print("不存在压缩包")

        flag = 0

        try:
            rename("",prefix,20)
        except:
            flag = 1
        if flag ==1:
            print("不存在前缀名")
        for id in range(pre+1,n+1):
            next = id
            print("id: ",id)
            io = IO(file_prefix=r'test/', data_id=id)
            a = open(r'test/%s%d.in'%(prename,id),"r")
            lst = a.readlines()
            a.close()
            for i in range(len(lst)):
                lst[i] = [lst[i][:-1]]
            for i in lst:
                io.input_writeln(i)
            try: 
                io.output_gen(r'Std/std')
            except:
                print("标程运行错误")
                io.close()
                return  "标程运行错误"
            io.close()
        print("has end")
        if close:
            return "success"
        zip = thread.Thread(target=mkzip,args=(n+1,pre))
        zip.start()
        zip.join()
        delzip(filename)
        return "success"
        
    def make_data(self,n = 16,pre=0,func=print,close = False,prefix=""):
        name = func.__name__
        global _pre,prename
        _pre = pre
        self.Compile()
        prename = prefix
        print("make_data",prename)
        for id in range(pre+1, n+1):
            if id%5==0:
                print("id: ",id)
            io = IO(file_prefix=r'test/', data_id=id)
            try:
                io = IO(file_prefix=r'test/', data_id=id)
            except:
                #self.makedata(n,func)
                print("运行出错")
                return "运行出错"
            lst = func(id,n)
            lst = rebuild(lst)
            #m = randint(n - 1, MAXM) # DAG 的性质，边数大于等于节点数-1
            #graph = Graph.DAG(n, m) # n 点 m 边的 DAG
            if type(lst[0]) != list:
                lst = [lst]
            for i in lst:
                io.input_writeln(i)
            try:
                io.output_gen(r'Std/std')
            except:
                print("标程运行错误")
                io.close()
                return  "标程运行错误"
            io.close()
        print("has end")
        if close:
            return "success"
        zip = thread.Thread(target=mkzip,args=(n+1,pre))
        zip.start()
        zip.join()
        return "success"