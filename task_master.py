#!/usr/bin/python

#task_master.py

import random,time,queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue=queue.Queue()
#接受结果的队列
result_queue=queue.Queue()

#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

def return_result_queue():
    global result_queue
    return result_queue

def return_task_queue():
    global task_queue
    return task_queue

def startserver():
    #吧两个queue注册到网络上 callable参数管理queue对象
    QueueManager.register('get_task_queue',callable=return_task_queue)
    QueueManager.register('get_result_queue',callable=return_result_queue)
    #锁定端口5000 设置验证码abc
    manager=QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
    #启动queue
    dir(manager)
    manager.start()
    #获取通过网络访问的queue对象
    task=manager.get_task_queue()
    result=manager.get_result_queue()
    #放任务进去
    for i in range(10):
        n=random.randint(0,10000)
        print('put task %d...'%n)
        task.put(n)
    #从result队列读取结果    
    print('try get results')
    for i in range(10):
        r=result.get(timeout=10)
        print('result:%s'%r)
    #关闭
    manager.shutdown()
    print('master exit')


if __name__=='__main__':
    startserver()
    
