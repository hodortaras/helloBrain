import random
import os
import numpy as n
import argparse
import string
from random import choice


parser = argparse.ArgumentParser(description='Diagram parametrs')
parser.add_argument('metod', type = str, help = 'Задайте номер решаемого задания "m1....m10"')
args = parser.parse_args()


symbols1 = 'ABCDEFGHJKLMNPQRSTUVWXYZ'
symbols2 = 'abcdefghijkmnpqrstuvwxyz'
symbols3 = '123456789'
domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l", 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'                ]


def random_domain(domains):
        return domains[random.randint( 0, len(domains)-1)]


def random_name(letters):
    email_name = ""
    for i in range(7):
        email_name = email_name + letters[random.randint(0,len(letters)-1)]
    return email_name


def generate_random_emails():
         one_name = str(random_name(letters))
         one_domain = str(random_domain(domains))
         return (one_name  + "@" + one_domain)

def deinum(x):
    return x.isdigit()

def generate_password(m):
    chars = string.ascii_letters + string.digits
    return ''.join([choice(chars) for i in range(m)])

def f_eval(n):
    return str(eval(n))

def stuped_func(st):
    if args.metod == 'm6':
        return st.replace('!','')
    elif st[:3] == 'abc':
        return st.replace('abc','www')
    else:
        st = st + 'zzz'
        return

def summaslow(st):
    l = st.split(sep = ' ')
    summa = 0
    for i in range(len(l)):
        try:
            x = float(l[i])
            summa += x
        except:
            pass
    return summa

def sortnum(a):
    num = [int(i) for i in a if i.isdigit()]
    return len(num)

def sortstr(st):
    l=st.split(' ')
    l.sort()
    return l


if __name__=='__main__':
    if args.metod == 'm1':
        print('Сгенерирован один рандомный e-mail: ' + generate_random_emails())
    elif args.metod == 'm2':
        a = input('Введите простое математическое выражение для вычислений: ')
        print('Ответ: ' + f_eval(a))
    elif args.metod == 'm3':
        a = input('Введите строку дя проверки являеться ли она действительным числом: ')
        print(deinum(a))
    elif args.metod == 'm4':
        a = int(input('Из скольки символов сгенерировать пароль? '))
        print(generate_password(a))
    elif args.metod == 'm5':
        stroka = input('Введите сстроку для обработки: ')
        print(stuped_func(stroka))
    elif args.metod == 'm6':
        stroka = input('Введите сстроку для обработки: ')
        print('Строка с удалёнными "!": ' + stuped_func(stroka))
    elif args.metod == 'm7':
        stroka = input('Введите сстроку для обработки со словами из цифр: \n ')
        print('Сумма слов состоящих из цифр: ' + str(summaslow(stroka)))
    elif args.metod == 'm8':
        stroka=list()
        for i in range(3):
            stroka.append(input('Введите строку содержащую цыфры: \n '))
        stroka.sort(key=sortnum)
        print(stroka)
    elif args.metod == 'm9':
        stroka = input('Введите сстроку для сортировки слов в алфавитном порядке: \n ')
        print(sortstr(stroka))
    elif args.metod == 'm10':
        stroka = input('Введите сстроку для подсчёта количества слов: \n ')
        print('Кол-во слов: '+ str(len(stroka.split(' '))))



# xs = ['dd1dd','a222','b33b','c4568884cc']
# l=[]
# for x in range(len(xs)):
#     l.append ([int(i) for i in xs[x] if i.isdigit()])
# #xs.sort(key=len)
# s={}
# print(l)
# for x in range(len(xs)):
#     s[len(l[x])]= xs[x]
# print(s)
# num=list(s.keys())
# num.sort()
# print(num)
# l=[]
# for x in range(len(xs)):
#     l.append(s[num[x]])
# print(l)
