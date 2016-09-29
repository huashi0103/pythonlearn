
def msort(a):
        i=len(a)
        while(i>1):
                j=0
                while(j<i-1):
                        if(a[j+1]<a[j]):
                             t=a[j]
                             a[j]=a[j+1]
                             a[j+1]=t
                        j=j+1
                i=i-1

def isort(a):
        for i in range(1,len(a)):
                t=a[i]
                j=i-1
                while(t<a[j] and j>=0):
                        a[j+1]=a[j]
                        j=j-1
                a[j+1]=t

def qsort(a,left,right):
        if right-left<2:return
        x=a[left]
        i=left
        j=right
        while(i<j):
                while(x<=a[j] and i<j):
                        j=j-1
                a[i]=a[j]
                while(x>=a[i] and i<j):
                        i=i+1
                a[j]=a[i]
        a[i]=x
        qsort(a,left,i-1)
        qsort(a,i+1,right)
        
def ssort(a,start):
        if start>=len(a):return
        index=start
        for i in range(start,len(a)):
                if(a[index]>a[i]):
                        index=i
        t=a[index]
        a[index]=a[start]
        a[start]=t
        ssort(a,start+1)
def init():
        return [12,11,21,25,114,2254,11,11,1,2,3,54]

def test():
	a=init()
	print(a)
	isort(a)
	print(a)
	a=init()
	msort(a)
	print(a)
	a=init()
	qsort(a,0,len(a)-1)
	print(a)
	a=init()
	ssort(a,0)
	print(a)
	

if __name__ == '__main__':
    test()
