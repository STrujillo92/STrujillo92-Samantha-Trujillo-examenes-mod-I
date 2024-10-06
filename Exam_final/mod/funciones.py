import random

l=[]
l2=[]
l3=[]
l4=[]
l5=[]


def func01():
    for i in range(10):
        x=random.randint(0,20)
        l.append(x)
    print(l)


def func02(a):
    conj=set(a)
    for i in conj:
        l2.append(i)
    print(l2)


def func03(a):
    a.sort()
    for i in a:
        l3.append(i)
    print(l3)
    a.sort(reverse=True)
    for i in a:
        l4.append(i)
    print(l4)


def func04(a):
    for i in a:
        if i%2==0:
            l5.append(i)
    l5.sort()
    print(l5[-1])


func01()
func02(l)
func03(l2)
func04(l2)