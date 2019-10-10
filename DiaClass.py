from turtle import *
import argparse
import sys
from numpy import *


parser = argparse.ArgumentParser(description='Diagram parametrs')
parser.add_argument('typedia', type = str, help = 'Выбор типа диаграмы(cir - Круговая диаграма, gis - Гистаграмма)')
parser.add_argument('javascript', type = float, default = 0, help = 'Доля рынка языка программирования JavaScript')
parser.add_argument('c', type = float, default = 0, help = 'Доля рынка языка программирования C')
parser.add_argument('python', type = float, default = 0, help = 'Доля рынка языка программирования Python')
parser.add_argument('java', type = float, default = 0, help = 'Доля рынка языка программирования Java')
parser.add_argument('php', type = float, default = 0, help = 'Доля рынка языка программирования Php')
args = parser.parse_args()


#print(args.lan5 + ' '+ str(args.lan5des))

onepercent=round(360/(args.javascript+args.c+args.python+args.java+args.php),2)
colors=('yellow','blue','green','black','white')
ang=[i for i in range(5)]
ang[0] = onepercent*args.javascript
ang[1] = onepercent*args.c
ang[2] = onepercent*args.python
ang[3] = onepercent*args.java
ang[4] = 360 - (ang[0]+ang[1]+ang[2]+ang[3])

title = ['JavaScript','C','Python','Java','Php']

class Draw ():
    def __init__(self,size,title, colors):
        self.title = title
        self.size = size
        self.colors = colors
    def CircleDiagram(self):
        for x in range(5):
            color('red',self.colors[x])
            begin_fill()
            forward(120)
            left(90)
            circle(120,(self.size[x]/2))
            right(90)
            forward(30)
            write(self.title[x])
            left(180)
            forward(30)
            right(90)
            circle(120,(self.size[x]/2))
            left(90)
            forward(120)
            left(180)
            end_fill()
    def Gistagram(self):
        for x in range(5):
            color('red',self.colors[x])
            begin_fill()
            forward(42)
            left(90)
            forward(self.size[x]*2)
            left(90)
            forward(42)
            left(90)
            forward(self.size[x]*2)
            left(90)
            forward(6)
            write(self.title[x])
            forward(36)
            end_fill()

width(2)
p=Draw(ang,title,colors)
if __name__=='__main__':
    if args.typedia=='cir':
        p.CircleDiagram()
    elif args.typedia=='gis':
        p.Gistagram()
    else:
        print('Unknow format of comand parameters')
done()
