from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element:%s,attrs:%s'%(name,str(attrs)))

    def end_element(self,name):
        print('sax:end_element:%s'%name)

    def char_data(self,text):
        print('sax:char_data:%s'%text)

xml=r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

for i in range(10):
    print(i)
handler=DefaultSaxHandler()
parser=ParserCreate()
parser.StartElementHandler=handler.start_element
parser.EndElementHandler=handler.end_element
parser.CharacterDataHandler=handler.char_data
parser.Parse(xml)


from xml.sax.handler import ContentHandler
from xml.sax import parse
import os


class Dispatcher:
    def dispatch(self,prefix,name,attrs=None):
        mname=prefix+name.capitalize()
        dname='default'+prefix.capitalize()
        method=getattr(self,mname,None)
        if callable(method):args=()
        else:
            method=getattr(self,dname,None)
            args=name,
        if prefix=='start':args+=attrs,
        if callable(method):method(*args)

    def startElement(self,name,attrs):
        self.dispatch('start',name,attrs)

    def endElement(self,name):
        self.dispatch('end',name)


class WebsiteConstructor(Dispatcher, ContentHandler):
    paathrough=False

    def __init__(self,directory):
        self.directory=[directory]:
