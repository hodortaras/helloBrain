
'''
Программа построения диаграммы по входным параметрам

В качестве первого аргумента задаётся тип диаграммы, данный параметр может принимать значение:
cir - круговая диаграмма;
gis - гистаграмма.
Далее программа принимает 10 аргументов в виде 5 пар: название столбца(str),
 значение по которому строится диаграмма(float).
 '''

from turtle import *
import argparse
from numpy import round


parser = argparse.ArgumentParser(description='Diagram parametrs')
parser.add_argument('typedia', type=str, help='Type of diagram (parametr: cir or gis)')
parser.add_argument('lan1', type=str, help='First name of language')
parser.add_argument('lan1des', type=float, help='size the first diagram position')
parser.add_argument('lan2', type=str, help='Second name of language')
parser.add_argument('lan2des', type=float, help='size the second diagram position')
parser.add_argument('lan3', type=str, help='Third name of language')
parser.add_argument('lan3des', type=float, help='size the third diagram position')
parser.add_argument('lan4', type=str, help='Fourth name of language')
parser.add_argument('lan4des', type=float, help='size the fourth diagram position')
parser.add_argument('lan5', type=str, help='Fifth name of language')
parser.add_argument('lan5des', type=float, help='size the fifth  diagram position')
args = parser.parse_args()



onepercent=round(360/(args.lan1des+args.lan2des+args.lan3des+args.lan4des+args.lan5des),2)
colors=('yellow','blue','green','black','white')
ang=[i for i in range(5)]
ang[0] = onepercent*args.lan1des
ang[1] = onepercent*args.lan2des
ang[2] = onepercent*args.lan3des
ang[3] = onepercent*args.lan4des
ang[4] = 360 - (ang[0]+ang[1]+ang[2]+ang[3])

lan=[i for i in range(5)]
lan[0]=args.lan1
lan[1]=args.lan2
lan[2]=args.lan3
lan[3]=args.lan4
lan[4]=args.lan5

def CircleDiagram():
    for x in range(5):
        color('red',colors[x])
        begin_fill()
        forward(120)
        left(90)
        circle(120,(ang[x]/2))
        right(90)
        forward(30)
        write(lan[x])
        left(180)
        forward(30)
        right(90)
        circle(120,(ang[x]/2))
        left(90)
        forward(120)
        left(180)
        end_fill()

def Gistagram():
    for x in range(5):
        color('red',colors[x])
        begin_fill()
        forward(42)
        left(90)
        forward(ang[x]*2)
        left(90)
        forward(42)
        left(90)
        forward(ang[x]*2)
        left(90)
        forward(6)
        write(lan[x])
        forward(36)
        end_fill()

width(2)
if __name__=='__main__':
    if args.typedia=='cir':
        CircleDiagram()
    elif args.typedia=='gis':
        Gistagram()
    else:
        print('Unknow format of comand parameters')
done()
