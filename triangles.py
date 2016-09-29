def triangles():
    n=1;
    while True:
        yield t(n)
        n=n+1
    
    
    
def t(n):
    l=[]
    if n==1:
        return [x for x in range(1,2)]
    l1=t(n-1)
    l.append(1)
    for i in range(1,len(l1)):
        l.append(l1[i-1]+l1[i])
    l.append(1)
    return l

def triangles1():
    lst = [1]
    while True:
        yield lst
        lst.append(0)     # 先占位，然后修改相应位置上的数值
        lst = [lst[i-1] + lst[i] for i in range(len(lst))]
        

def test():
    n=0
    for t in triangles1():
        print(t)
        n=n+1
        if n==10:
            break

        
if __name__=="__main__":
    test()
