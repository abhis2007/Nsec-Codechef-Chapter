import bisect
li=[1400,1600,1800,2000,2200,2500]
for i in range(int(input())):
    v=int(input())
    if(v>=0):
        print(bisect.bisect_right(li,v)+1)
    else:
        print("PLAGIARIZE")
  
