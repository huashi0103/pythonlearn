import json
import os
import subprocess
import time,random
import threading

from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue


class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

        
def sudent2dict(std):
    return{
        'name':std.name,
        'age':std.age,
        'score':std.score
        }

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])
# linux  mac
def test():
    print('Process(%s)start..'%os.getpid())
    pid=os.fork()
    if pid==0:
        print('child id (%s)  parent id(%s)'%(os.getpid(),os.getppid()))
    else:
        print('(%s)create child id(%s)'%(os.getpid(),pid))



def run_proc(name):
    print('run child process %s (%s)..'%(name,os.getpid()))


def log_time_task(name):
    print('run task %s(%s)..'%(name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('task %s runs %0.f seconds.'%(name,(end-start)))




def write(q):
    print('process to write:%s'%os.getpid())
    for value in['A','B','C']:
        print('put %s to queue..'%value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('process to read：%s'%os.getpid())
    while True:
        value=q.get(True)
        print('get %s from queue:'%value)

def loop():
    print('thread %s is running,,,'%threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s>>>%s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended'%threading.current_thread().name)
    
balance=0
lock=threading.Lock()

def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n

def run_thread(n):
    for i in range(10000):
        change_it(n)
        '''
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
            
            '''
local_school=threading.local()

def process_student():
    std=local_school.student
    print('hello,%s(in %s)\n'%(std,threading.current_thread().name))
    

def process_thread(name):
    local_school.student=name
    process_student()


if __name__=="__main__":
    '''
    s=Student('Bob',20,86)
    print(json.dumps(s,default=sudent2dict))
    print("..................")
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print(json.loads(json_str, object_hook=dict2student))
    '''
    #test()
    '''
    print('parent process %s'%os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('child process will start')
    p.start()
    p.join()
    print('child process end')
    '''
    '''
    print('parent process %s'%os.getpid())
    p=Pool(9)
    for i in range(9):
        p.apply_async(log_time_task,args=(i,))
    print("wait for all subprocess done..")
    p.close()
    p.join()
    print('all subprocess done')
    '''
    '''
    print('$ nslookuyp www.python.org')
    r=subprocess.call(['nslookup','www.python.org'])
    print('exit code',r)
    '''
    '''
    print('$nslookup')
    p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output)
    print('excit code:',p.returncode)
    '''
    '''
    q=Queue()
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
    '''
    '''
    print('thread %s is running..'%threading.current_thread().name)
    t=threading.Thread(target=loop,name='loopthread')
    t.start()
    t.join()
    print('thread %s ended'%threading.current_thread().name)


    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
    '''
    t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
