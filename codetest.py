#!/usr/bin/env python
'''
An exampler of reading and writing Unicode string:Writes
a Unicode string to a file in utf-8 and reads itback in
'''
CODEC='utf-8'
FILE='unicode.txt'

hello_out=u'Hello world\n'
bytes_out=hello_out.encode(CODEC)
f=open(FILE,'w')
f.write(str(bytes_out,encoding='utf-8'))
f.close()

f=open(FILE,'r')
bytes_in=f.read()
f.close()
hello_in=bytes(bytes_in,encoding='utf-8')
print(hello_in)
