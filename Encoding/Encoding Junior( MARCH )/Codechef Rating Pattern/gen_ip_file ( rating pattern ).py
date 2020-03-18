from collections import defaultdict, deque
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

import os,sys
print(os.path.join(sys.path[0],"final_input.in"))
sys.stdout = open(os.path.join(sys.path[0],"final_input.in"),'w+')

test=100000

print(test)

for i in range(test):
    if(i<=5000):
        rating=randint(-4000,0)
        print(rating)
    elif(i<=50000):
        rating=randint(0,4000)
        if(rating not in lists):
            print(rating)
        else:
            while(rating in lists):
                rating=randint(0,4000)
            print(rating)
    else:
        rating=randint(0,4000)
        if(rating in lists):
            print(rating)
        else:
            if(rating in lists):
                print(rating)
            while(rating not in lists):
                rating=randint(0,4000)
            print(rating)
