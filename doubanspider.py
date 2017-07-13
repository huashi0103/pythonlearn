#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request

__doc__='douban spider test'
__author__='weisili'


def douban():
        req=request.Request('http://www.douban.com/')
        req.add_header('User-Agent','Mazilla/6.0(iPhone:CPU iPhone OS 8_0 like Mac OSX) AppleWebKit/536.26(KHTML,like Gecko)Version/8.0 Mobile/10A5376e Safari/8536.25')
        with request.urlopen(req) as f:
                print('Status:',f.status,f.reason)
                for k,v in f.getheaders():
                        print('%s;%s'%(k,v))
                print('Data:',f.read().decode('utf-8'))


def doubanspider():
        url="https://api.douban.com/v2/book/2129650"
        with request.urlopen(url) as f:
                data=f.read()
                print('Status:',f.status,f.reason)
                for k,v in f.getheaders():
                        print('%s:%s'%(k,v))
                print('Data',data.decode('utf-8'))


def main():
	end=1
	while end>0:
		test=input('请输入:')
		if test=='q':
            end=0
            print('退出')
		elif test=='a':
                        douban()
		else:
                        print(test)
	s=input('输入任意字符结束..')




if __name__ == '__main__':
    main()
