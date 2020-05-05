"""from collections import defaultdict, deque
from itertools import permutations
from sys import stdin,stdout
from bisect import bisect_left, bisect_right
from copy import deepcopy
from random import randint,randrange,choice

int_input=lambda : int(stdin.readline())
string_input=lambda : stdin.readline()
multi_int_input =lambda : map(int, stdin.readline().split())
multi_input = lambda : stdin.readline().split()
list_input=lambda : list(map(int,stdin.readline().split()))
string_list_input=lambda: list(string_input())
MOD = pow(10,9)+7

lists=[1399,1400,1599,1600,1799,1800,1999,2000,2199,2200,2499,2500]
import os,sys"""
import sys,os
print(os.path.join(sys.path[0],"input.in"))
sys.stdout = open(os.path.join(sys.path[0],"input.in"),'w+')
from random import randint,randrange,choice
test=10000
print(test)
for i in range(test):
    if(i<=7000):
        l=randint(0,10000001)
        r=randint(l,10000001)
        print(l,r)
    elif(i>7000 and i<=7200):
        l=randint(0,100001)
        r=randint(l+1,100001)
        if(r%59==0):
            print(l,r)
        else:
            while(r%59!=0):
                r=randint(l+1,100001)
            print(l,r)
    elif(i>7200 and i<7500):
        l=randint(0,100001)
        r=randint(0,l+1)
        print(l,r)
    else:
        l=randint(0,59)
        r=randint(l,59)
        print(l,r)
