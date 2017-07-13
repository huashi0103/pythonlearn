
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


def medianSlidingWindow(nums, k):
    # write your code here
    le = len(nums)
    res = []
    a = []
    for i in range(le):
        if i + k>le:break;
        if i == 0:
            a = nums[i:i + k]
            for j in range(1, k):
                t = a[j]
                n = j - 1
                while (t < a[n] and n >= 0):
                    a[n + 1] = a[n]
                    n = n - 1
                a[n + 1] = t
        else:
            del a[0]
            t = nums[i + k - 1]
            for i in range(len(a)):
                if t<a[i]:
                    a.insert(i,t)
                    break
            if len(a)!=k:a.append(t)
        if k % 2 == 0:
            res.append((a[k / 2 - 1] + a[k / 2]) / 2)
        else:
            res.append(a[k % 2])
    return res


if __name__ == '__main__':
    a = [1, 2, 7, 8, 5]
    #res = medianSlidingWindow(a, 3)
    qsort(a,0,len(a)-1)
    print(a)
