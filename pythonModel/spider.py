import urllib
import os
from urllib import request
from lxml import etree
import re


def StringListSave(save_path, filename, slist):
    #if not os.path.exists(save_path):
        #os.makedirs(save_path)
    path = save_path+"/"+filename+".txt"
    for s in slist:print("%s\t\t%s" % (s[0].encode("utf-8"), s[1].encode("utf8")))
    #with open(path, "w+") as fp:
       # for s in slist:
           #fp.write("%s\t\t%s\n" % (s[0].encode("utf8"), s[1].encode("utf8")))


def Page_Info(myPage):
    mypage_Info = re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', myPage, re.S)
    return mypage_Info

def New_Page_Info(new_page):
    dom = etree.HTML(new_page)

    new_items = dom.xpath('//tr/td/a/text()')
    new_urls = dom.xpath('//tr/td/a/@href')
    assert(len(new_items) == len(new_urls))
    return zip(new_items, new_urls)



def Spider(url):
    i = 0
    print("downloading%s"%url)
    myPage = request.urlopen(url)

    decode=(myPage.headers['Content-Type'].split(';')[1]).split('=')[1]
    data = myPage.read().decode(decode.lower())
    myPageResults = Page_Info(data)

    save_path = u"网易新闻抓取"
    filename = str(i) + "_" + u"新闻排行榜"
    #StringListSave(save_path, filename, myPageResults)

    i += 1
    for item, url in myPageResults:
        print("downloading%s"%url)
        new_page =  request.urlopen(url).read()
        newPageResults = New_Page_Info(new_page)
        for np in newPageResults:
            print(np)
        #filename = str(i) + "_" + item
        #StringListSave(save_path, filename, newPageResults)
        i += 1


def Pageinfotest(myPage):
    mypage_Info = re.findall(r'<td[^>]+>(.*?)</td>', myPage, re.S)
    return mypage_Info


def spidertest(url):
    i = 0
    print("downloading%s"%url)
    myPage = request.urlopen(url)
    decode='gb2312'
    data = myPage.read().decode(decode.lower())
    
    

    
def opentxt():
    p=r'D:\Desktop\222.txt'
    pw=r'D:\Desktop\3.txt'
    f=open(p,'r')
    fw=open(pw,'w')
    for l in f.readlines():
        res=re.findall(r'<td .*?>(.*?)</td>', l, re.S)
        if len(res)>0:
            for r in res:
                if 'strong' in r:
                    fw.write(r+'\n')
                elif 'ohhovvwc' in r:
                    ht=re.findall(r'<a .*? ohhovvwc="(.*)" .*?>.*?</a>',r,re.S)
                    for h in ht:
                        fw.write(h+'\n')
                else:
                    ht=re.findall(r'<a href="(.*?)" .*?>.*?</a>',r,re.S)
                    for h in ht:
                        fw.write(h+'\n')



if __name__ == '__main__':
    opentxt()
    print("end")
