from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

COMMENT_CHARS='#:'
#http://www.swpc.noaa.gov/ftpdir/weekly/Predict.txt
file=open("D:\Desktop\commandflags.txt")
drawing=Drawing(400,200)
data=[]

for line in file.readlines():
    if not line.isspace():
        data.append([float(n) for n in line.split()])

pred=[row[2]for row in data]
high=[row[3]for row in data]
low=[row[4]for row in data]
times=[row[0]+row[1]/12.0 for row in data]
lp=LinePlot()
lp.x=50
lp.y=50
lp.height=125
lp.width=300
lp.data=[zip(times,pred),zip(times,high),zip(times,low)]
lp.lines[0].strokeColor=colors.blue
lp.lines[1].strokeColor=colors.red
lp.lines[2].strokeColor=colors.green


