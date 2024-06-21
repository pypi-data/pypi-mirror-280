'''
make_Big(left,right=0,neg = "")
low_set()
upper_set()
digit_set()
ch_set()
'''
def Ch_set():
    return low_set()+ch_set()+digit_set()+up_set()
def make_Big(left,right=0,neg = ""):
    if right ==0:
        right = left
    if neg:
        neg = '-'
    bit_set = "".join([str(i) for i in range(10)])
    begin = "%s%s"%(bit_set[1:],neg)
    begin = String.random((1),charset = begin)
    if begin !="-":
        left-=1
        left= max(left,0)
        right-=1
        right = max(right,0)
    #sprint(left,right)
    return "%s%s"%(begin,String.random((left,right),charset = bit_set))

def low_set():
    return "".join([chr(ord("a")+i) for i in range(26)])
def up_set():
    return "".join([chr(ord("A")+i) for i in range(26)])
def digit_set():
    return "".join(chr(ord("0")+i) for i in range(10))
def ch_set():
    lst = []
    for i in range(33,48):
        lst.append(chr(i))
    for i in range(58,65):
        lst.append(chr(i))
    for i in range(91,97):
        lst.append(chr(i))
    for i in range(123,127):
        lst.append(chr(i))
    return "".join(lst)

