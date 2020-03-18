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
import bisect
count=0
li=[1400,1600,1800,2000,2200,2500]
f=open("final_input.in","r+")
files=open("final_output.in","w")
for i in f:
    if(4000>=int(i)>=0):
        val=str(bisect.bisect_right(li,int(i))+1)
        files.write(str(val)+"\n")
    if(int(i)<0):
        files.write("PLAGIARIZE"+"\n")
files.close()
f.close()


          
"""o=os.path.join(sys.path[0],"input.in")
f=open(o,"r")
import bisect
li=[1400,1600,1800,2000,2200,2500]
sys.stdout = open(os.path.join(sys.path[0],"output2.in"),'w+')
print(bisect.bisect_right(li,f.readline()+1)"""

