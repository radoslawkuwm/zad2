import math
import sys as system

def zad():
    sporty=['koszykowka','reczna','siatkowka','hokerj','curling']
    sporty.reverse()
    sporty.extend(['zumba','joga'])
    print(sporty)

def zad2():
    slownik = {'itp':'i tym podobne','itd':'i tak dalej','jw':'jak wyzej'}

def zad3():
    gry = {'ets':'Euro truck simulatro','cs':'Counter strike','aoe':'Age of empires'}
    print(len(gry))

def zad4():
    zdanie = input()
    print(zdanie.count('a'))

def zad5():
    a = system.stdin.readline()
    b = system.stdin.readline()
    c = system.stdin.readline()
    system.stdout.write(str(math.pow(float(a),float(b))+float(c)))

def zad6():
    a = input()
    b = input()
    c = input()

    if(a>b):
        if(a>c):
            print(a)
        else:
            print(c)
    else:
        if(b>c):
            print(b)
        else:
            print(c)

def zad7():
    lista = [2,4,6,3.5,5.5,7.5]
    for x in lista:
        print(x*x)

def zad8():
    lista = []
    i=0
    while(i<10):
        x = float(input())
        if(x%2 == 0):
            lista.append(x)
        i+=1
    print(lista)

def zad9():
    try:
        print(math.sqrt(float(input())))
    except ValueError:
        print('podano liczbe ujemna')
