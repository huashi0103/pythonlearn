
#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
#Definition of Doubly-ListNode
class DoublyListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next


class Solution:
    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        # Write your code here
        l=[]
        if root is None:return
        stack=[]
        current=root
        while len(stack)> 0 or current is not None:
            while current is not None:
                stack.append(current)
                current=current.left
                
            current=stack.pop()
            l.append(current.val)
            current=current.right
        
        dlist=DoublyListNode(l[0])
        current=None
        last=dlist
        for i in range(1,len(l)) :
            current=DoublyListNode(l[i])
            current.prev=last
            last.next=current
            last=current
        
        return dlist

    def medianSlidingWindow(self, nums, k):
        # write your code here
        le = len(nums)
        res = []
        a = []
        def sort(b, first = True):
            if len(b) < 2: return b
            if first:
                return sortq(b)
            else:
                insert = b[len(b) - 1]
                low=0
                high=len(b)-2
                while low <= high:
                    mid=(low+high)//2;
                    if insert>b[mid]:
                        low=mid+1
                    else:
                        high=mid-1
                b.insert(low,insert)
                b.pop()
                return b

        def sortq(b):
            if len(b)<2:
                return b
            else:
                q=b[0]
                less=[i for i in b[1:] if i<=q]
                greator=[i for i in b[1:] if i>q]
                return sortq(less)+[q]+sortq(greator)

        for i in range(le):
            if i + k > le: break
            if i == 0:
                a = nums[i:i + k]
                b = sort(a)
            else:
                n=len(b)
                l = 0
                r = n - 1
                target = nums[i - 1]
                while l <= r:
                    mid = (l + r) // 2
                    if b[mid] > target:
                        r = mid-1
                    elif b[mid]<target:
                        l = mid+1
                    else:
                        b.pop(mid)
                        break
                b.append(nums[i+k-1])
                b=sort(b,first=False)
            l = len(b)
            if l % 2 == 0:
                res.append(b[l // 2] if b[l // 2 - 1] > b[l // 2] else b[l // 2 - 1])
            else:
                res.append(b[l // 2])
        return res

    def addLists2(self, l1, l2):
        # Write your code here
        strl1 = ''
        current = l1
        while current is not None:
            if current.val == None:
                strl1 = strl1+'0'
            else:
                strl1 = strl1+str(current.val)
            current = current.next
        intl1 = int(strl1)
        strl1 = ''
        current = l2
        while current is not None:
            if current.val == None:
                strl1 = strl1+'0'
            else:
                strl1 = strl1 + str(current.val)
            current = current.next
        intl2 = int(strl1)
        val = str(intl1+intl2)
        res = None
        last = None
        for s in val:
            v = int(s) if s != '0' else None
            if res is None:
                res = ListNode(v)
                last=res
            else:
                last.next = ListNode(v)
                last = last.next
        return res

    def expressionExpand(self, s):
        # Write your code here
        nl = []
        sl = []
        sc = ''
        res = ''
        for i in s:
            if i.isdigit():
                sc = sc + i
            else:
                if i == '[':
                    nl.append(int(sc))
                    sl.append('[')
                    sc = ''
                elif i == ']':
                    n = nl.pop()
                    while len(sl)>0:
                        k=sl.pop()
                        if k== '[':break
                        sc=k+sc
                    ts = ''
                    for j in range(n): ts = ts + sc
                    sc = ''
                    if len(nl) > 0:
                        sl.append(ts)
                    else:
                        res = res + ts
                else:
                    if len(nl)>0:
                        sc = sc + i
                    else:
                        res = res + i

        return res

    # @param {string} s a string
    # @param {set[str]} wordDict a set of words
    def wordBreak(self, s, wordDict):
        # Write your code here
        head = []
        for di in wordDict:
            if di !='' and  s.startswith(di):
                head.append(di)
        if len(head) < 1: return []
        cur = s
        res = []
        while len(head) > 0:
            h = head.pop()
            le=len(h.replace(' ',''))
            cur=s[le:]
            if cur == '':
                res.append(h)
                continue
            for di in wordDict:
                if cur.startswith(di):
                    head.append(h + ' ' + di)
        return res

    # @param {int[][]} envelopes a number of envelopes with widths and heights
    # @return {int} the maximum number of envelopes
    def maxEnvelopes(self, envelopes):
        # Write your code here
        import functools
        nums = sorted(envelopes,key= functools.cmp_to_key(lambda x,y:x[0]-y[0] if x[0] != y[0] else y[1] - x[1]))
        print(nums)
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high)//2
                if dp[mid][1] < nums[x][1]:
                    low = mid + 1
                else:
                    high = mid - 1
            if low < len(dp):
                dp[low] = nums[x]
            else:
                dp.append(nums[x])

        print(dp)
        return len(dp)

    def maxEnvelopes2(self, envelopes):
        # Write your code here
        import functools
        nums = sorted(envelopes,key= functools.cmp_to_key(lambda x,y:x[0]-y[0] if x[0] != y[0] else x[1] - y[1]))
        print(nums)
        size = len(nums)
        dp=[1]*size
        maxlen=1
        for i in range(size):
            for j in range(i):
                if nums[i][0]>nums[j][0] and nums[i][1]>nums[j][1]:
                    dp[i]=max(dp[i],dp[j]+1)
            maxlen=max(maxlen,dp[i])
        return maxlen

    def  maxEnvelopes3(self, envelopes):
        import functools
        nums = sorted(envelopes, key=functools.cmp_to_key(lambda x, y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1]))

        maxlen = 0
        h =[0]*len(nums)
        for s in nums:
            i,j = 0,maxlen-1
            while i <=j :
                m = (i+j)//2
                if h[m] < s[1]:
                    i=m+1
                else:
                    j = m-1

            h[i] = s[1]
            if i == maxlen:
                maxlen=maxlen+ 1
        return maxlen

    def largestDivisibleSubset(self, nums):
        n=len(nums)
        nums= sorted(nums)
        res=[]
        for i in range(n):
            cur=[nums[i]]
            last=nums[i]
            for j in range(i+1,n):
                if nums[j] % last ==0 or last% nums[j]==0:
                    cur.append(nums[j])
                    last=nums[j]
            res.append(cur)
        res=sorted(res,key=lambda x:len(x),reverse=True)
        return res[0]

    def canFinish(self, numCourses, prerequisites):
        # Write your code here
        pre = sorted(prerequisites, key=lambda x: x[0])
        dic=dict()
        for p in prerequisites:
            if p[0] in dic.keys():
                dic[p[0]].append(p)
            else:
                dic[p[0]]=[p]

        n=len(pre)
        if n < 2: return True
        res=[]
        cach=[]
        for i in range(n):
            res.append(pre[i])
            cach.append(pre[i])
            while len(cach)>0:
                cur=cach.pop()
                if cur[1] in dic.keys():
                    for j in dic[cur[1]]:
                        if cur[1] == j[0]:
                            for r in res:
                                if r[0] == j[1]: return False
                            cach.append(j)
        return True


if __name__== '__main__':
    solution=Solution()
    sums=[[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]
    sums=[[6,27],[83,9],[10,95],[48,67],[5,71],[18,72],[7,10],[92,4],[68,84],[6,41],[82,41],[18,54],[0,2],[1,2],[8,65],[47,85],[39,51],[13,78],[77,50],[70,56],[5,61],[26,56],[18,19],[35,49],[79,53],[40,22],[8,19],[60,56],[48,50],[20,70],[35,12],[99,85],[12,75],[2,36],[36,22],[21,15],[98,1],[34,94],[25,41],[65,17],[1,56],[43,96],[74,57],[19,62],[62,78],[50,86],[46,22],[10,13],[47,18],[20,66],[83,66],[51,47],[23,66],[87,42],[25,81],[60,81],[25,93],[35,89],[65,92],[87,39],[12,43],[75,73],[28,96],[47,55],[18,11],[29,58],[78,61],[62,75],[60,77],[13,46],[97,92],[4,64],[91,47],[58,66],[72,74],[28,17],[29,98],[53,66],[37,5],[38,12],[44,98],[24,31],[68,23],[86,52],[79,49],[32,25],[90,18],[16,57],[60,74],[81,73],[26,10],[54,26],[57,58],[46,47],[66,54],[52,25],[62,91],[6,72],[81,72],[50,35],[59,87],[21,3],[4,92],[70,12],[48,4],[9,23],[52,55],[43,59],[49,26],[25,90],[52,0],[55,8],[7,23],[97,41],[0,40],[69,47],[73,68],[10,6],[47,9],[64,24],[95,93],[79,66],[77,21],[80,69],[85,5],[24,48],[74,31],[80,76],[81,27],[71,94],[47,82],[3,24],[66,61],[52,13],[18,38],[1,35],[32,78],[7,58],[26,58],[64,47],[60,6],[62,5],[5,22],[60,54],[49,40],[11,56],[19,85],[65,58],[88,44],[86,58]]

    print(solution.canFinish(100,sums))


    # import profile
    # profile.run('solution.maxEnvelopes(sums)','prores')
    # import pstats
    # p=pstats.Stats('prores')
    # p.strip_dirs().sort_stats("cumulative").print_stats(10)#显示前几行，这里设置0 只显示总时间
