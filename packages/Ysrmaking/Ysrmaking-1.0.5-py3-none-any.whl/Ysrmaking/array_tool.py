import random as ran
import copy
def Array(a=0,b=1):
   return list(range(a,b+1)) 
def choosen(lst):
   ran.shuffle(lst)
   return lst

def choosen_arr(lst,n):
   Lst = copy.deepcopy(lst)
   a = []
   choosen(a)
   for i in range(n):
      if (i%(n//1000+1))==0:
          choosen(a)
          #print("has choosen")
      a.append(Lst.pop())
   return a

def make_matrix(n,m,order = True):
    if order:
        lst = list(range(1,n*m+1))
    else:
        lst = list(range(1,n*m*2))
        lst = choosen_arr(lst,n*m)
    choosen(lst)
    return get_arr(lst,m)
def get_arr(Arr,n):
    arr = copy.deepcopy(Arr)
    size = len(arr)
    lst = []
    l = []
    for i in range(size):
        choosen(arr)
        l.append(arr.pop())
        if i%n==n-1:
            lst.append(l)
            l = []
    return lst