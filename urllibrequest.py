import re
from urllib import request
from lxml import etree
import threadpool
import threading
import gzip
import io

testurl="http://news.163.com/rank/"
htmlcode='gbk'
threadlock=threading.Lock()
#news=[]
def test1():
    with request.urlopen(testurl) as f:
        print('Status:', f.status, f.reason)
        #网页的编码格式只取一次，默认所有的编码方式都是这个
        decode=(f.headers['Content-Type'].split(';')[1]).split('=')[1]
        data = f.read().decode(decode.lower())
        infos = re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', data, re.S)
        #for i in range(len(infos)):
            #print('%s-%s'%(i,infos[i][0]))
        #print('选择新闻类型')
        #k=input()
        k='0'
        if k.isdigit()and int(k)<len(infos):
            newpage=(request.urlopen(infos[int(k)][1]).read()).decode(decode.lower())
            dom=etree.HTML(newpage)
            items=dom.xpath('//tr/td/a/text()')
            urls=dom.xpath('//tr/td/a/@href')
            assert (len(items)==len(urls))
            urlss=urls[:50]
            print(len(items))
            for i in range(len(urlss)):
                new=(request.urlopen(urlss[i]).read()).decode(decode.lower())
                #ncs=re.findall(r'<div id="endText" class="end-text">.*?</div>',data,re.S)
                newdom=etree.HTML(new)
                newitems=newdom.xpath("//div[@id='endText'and @class='post_text']/p/text()")
                newcontent=''
                for n in newitems:
                    newcontent=newcontent+n
                news.append(newcontent)
                #print('=======================输入y继续')
                #if 'y'==input():continue
                #else:break;
        print('ok')



        
def test2():
    with request.urlopen(testurl) as f:
        htmlcode=(f.headers['Content-Type'].split(';')[1]).split('=')[1]
        data = f.read().decode(htmlcode.lower())
        infos = re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', data, re.S)
        newpage=(request.urlopen(infos[0][1]).read()).decode(htmlcode.lower())
        dom=etree.HTML(newpage)
        items=dom.xpath('//tr/td/a/text()')
        urls=dom.xpath('//tr/td/a/@href')
        assert (len(items)==len(urls))
        urlss=urls[:50]
        print(len(items))
        news=[]
        args=[]
        [args.append(([i,news],None)) for i in urlss]
        pool=threadpool.ThreadPool(8)
        ress=threadpool.makeRequests(GetNewpage,args)
        [pool.putRequest(req) for req in ress]
        print("start=====%s"%len(urlss))
        pool.wait()
        print("end==========")
        print(len(news))
        print(news[0])
        while(True):
            k=input()
            if not k.isdigit()or int(k)>=len(news):break
            print(news[int(k)])

            
def GetNewpage(url,news):
    try:
        new=(request.urlopen(url).read()).decode(htmlcode.lower())
        newdom=etree.HTML(new)
        newitems=newdom.xpath("//div[@id='endText'and @class='post_text']/p/text()")
        newcontent=""
        for n in newitems:
            newcontent=newcontent+n
        threadlock.acquire()
        news.append(newcontent)
        threadlock.release()
    except Exception:
        print('%s------------------error'%url)


def pooltest():
    a=[1,2,3,4,5,6,7,8,9,10,111]
    b=[]
    args=[]
    [args.append(([i,b],None)) for i in a]
    pool=threadpool.ThreadPool(5)
    ress=threadpool.makeRequests(lambda x,y:y.append(x),args,lambda x,y:print(x.requestID))
    [pool.putRequest(req) for req in ress]
    pool.wait()
    
'''
Host: sp1.baidu.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
Referer: https://www.baidu.com/
Cookie: BAIDUID=167C88351DCB85B1BE54615AC628B987:FG=1;\
BIDUPSID=1A859D128A56BD31E67D8AD597A24104;\
PSTM=1493984301;\
BDUSS=V2WDhlZ1ZDbndrU0NWbDBrRFpPdXFUOTRQN0VSNHRsdWl0RVJJTHhnZEU4VE5aSVFBQUFBJCQAAAAAAAAAAAEAAAC3TocYaHVhc2hpMTk4OTAxMDMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAERkDFlEZAxZOV;\
BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1455_21095_20698_22157; BDSFRCVID=n48sJeCCxG3Gh67ZL1SI_dVAASeXdBsqo1vQ3J;\
H_BDCLCKID_SF=tRk8oDK5JIvjHt_k-4rM-JL3hgT22-us32LJQhcH0b61sUndhRuhWx7L-RJJJUj0bKTiotjdQUb1D-nF-qrfQ-QQyH3ZQfJgyjbBQh5Tt\
UJMeCnTDMRhqt4bQGoyKMnitIv9-pPKJxt0hC-CDj0-DjPW5ptX54rKMDOXsJO8fbuMb-O_bfbT2MbyQUAqthTrtG7AMbbC0lj6efngLRbahT_B0HbZqtJHKbDtoDKatM5;\
PSINO=3
Connection: keep-alive
'''

cookie=' BAIDUID=167C88351DCB85B1BE54615AC628B987:FG=1;\
BIDUPSID=1A859D128A56BD31E67D8AD597A24104;\
PSTM=1493984301;\
BDUSS=V2WDhlZ1ZDbndrU0NWbDBrRFpPdXFUOTRQN0VSNHRsdWl0RVJJTHhnZEU4VE5aSVFBQUFBJCQAAAAAAAAAAAEAAAC3TocYaHVhc2hpMTk4OTAxMDMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAERkDFlEZAxZOV;\
BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1455_21095_20698_22157; BDSFRCVID=n48sJeCCxG3Gh67ZL1SI_dVAASeXdBsqo1vQ3J;\
H_BDCLCKID_SF=tRk8oDK5JIvjHt_k-4rM-JL3hgT22-us32LJQhcH0b61sUndhRuhWx7L-RJJJUj0bKTiotjdQUb1D-nF-qrfQ-QQyH3ZQfJgyjbBQh5Tt\
UJMeCnTDMRhqt4bQGoyKMnitIv9-pPKJxt0hC-CDj0-DjPW5ptX54rKMDOXsJO8fbuMb-O_bfbT2MbyQUAqthTrtG7AMbbC0lj6efngLRbahT_B0HbZqtJHKbDtoDKatM5;\
PSINO=3'
cookiedouban='ll="118254"; bid=SQm-UB52Ypw; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1494557917%2C%22https%3A%2F%2Fwww.baidu.com%2F%22%5D; \
_pk_id.100001.8cb4=962a96140f511561.1494202557.14.1494557917.1494553896.;\
__utma=30149280.578057176.1494202561.1494491184.1494553690.13; \
__utmz=30149280.1494553690.13.10.utmcsr=baidu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; \
push_noty_num=0; push_doumail_num=0; __utmv=30149280.4782; __yadk_uid=NDT5EVayoCEOfep58X2BctlFfDET9C4V; \
_vwo_uuid_v2=C6F51F6A66780168E4D5090D3529933E|678f0eac19877ea8f58479b04ec88d01; ps=y; ue="huachengming@126.com"; \
ct=y; __utmc=30149280; dbcl2="47824012:S0EuqaOSyLA"; ck=gwi9; _pk_ses.100001.8cb4=*'


def cookietest():
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
             'Accept':'*/*',
             'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
             'Accept-Encoding':'gzip, deflate, br',
             'Referer':'https://www.douban.com/',
             'Cookie':cookiedouban,
             'Connection':'keep-alive'}
    
    req=request.Request('https://www.douban.com',headers=headers)
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        bs=f.read();
        bi = io.BytesIO(bs)
        gf = gzip.GzipFile(fileobj=bi, mode="rb")
        print(gf.read().decode('utf-8'))




if __name__=="__main__":
    '''
    import profile
    profile.run('test2()','prores')
    import pstats
    p=pstats.Stats('prores')
    p.strip_dirs().sort_stats("cumulative").print_stats(0)
    '''
    cookietest()
    #test2()
    #pooltest()
    '''
    while(True):
        k=input()
        if not k.isdigit()or int(k)>=len(news):break
        print(news[int(k)])
    '''
