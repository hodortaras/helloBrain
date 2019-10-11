import sys
import argparse

parser = argparse.ArgumentParser(description='Diagram parametrs')
parser.add_argument('metod', type = str, help = 'Задайте номер решаемого задания "m1....m5"')
args = parser.parse_args()

def task1 (num, num2):
    s0=num+num2
    s1=num-num2
    s2=num*num2
    s=[s0,s1,s2]
    return s

def square(storona):
    return ((storona**2)*3**0.5)/4

def square1(ugol):
    return (ugol/2)*13.7**2

def stepen(num):
    b =[]
    b.append(num**5)
    b.append(num**13)
    return b

def zamena(qq,ww):
    pr1=(qq+ww)*0.5
    pr2=2*qq*ww
    if qq<ww:
        qq=pr1
        ww=pr2
    else:
        qq=pr2
        ww=pr1
    return qq,ww
if __name__=='__main__':
    if args.metod == 'm1':
        a = float(input('Веведите первое действительное число: '))
        b = float(input('Веведите второе действительное число: '))
        l=task1 (a,b)
        print('Сумма чисел {}, разность чисел {}, произведение чисел {}'.format(l[0],l[1],l[2]))
    elif args.metod == 'm2':
        rebro = float(input('Введите размер стороны равностороннего треугольника: '))
        print ('Площадь равностороннего треугольника ' + str(square(rebro)))
    elif args.metod == 'm3':
        ang=float(input('Радиус сектора 13.7. Введите угол сектора в радианах: '))
        print('Площадь данного сектора: '+str(square1(ang)))
    elif args.metod == 'm4':
        a = int(input('Веведите действительное число для возведения в степень: '))
        st = stepen(a)
        print('Число'+str(a)+'в степени 5='+str(st[0]))
        print('Число'+str(a)+'в степени 13='+str(st[1]))
    elif args.metod == 'm5':
        w1 = int(input('Веведите первое действительное число: '))
        w2 = int(input('Веведите второе действительное число: '))
        print('Числа заменены на' +str(zamena(w1,w2)))
