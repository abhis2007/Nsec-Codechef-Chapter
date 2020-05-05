MOD=1000000007
def gen(lists,l,r):
    sums=0;diff=r-l
    if(l%60==0):
        round=diff//60
        score=round*280
        i=1
        while(i<=r%60):
            sums+=lists[i]
            i+=1
        val=sums+score
        #print(val%MOD)
        files.write(str(val%MOD)+"\n")
    elif(diff>=59):
        val=l%60
        diff=r-l
        for p in range(val,60):
            sums+=lists[p]
        l=l-(l%60)+60
        round=(r-l)//60
        if(round>=0):
            score=round*280
        k=1
        while(k<=r%60):
            sums+=lists[k]
            k+=1
        val=score+sums;
        #print(val%MOD)
        files.write(str(val%MOD)+"\n")
    else:
        if(r%60>=59):
            j=l%60
            while(j<=59):
                sums+=lists[j]
                j+=1
            r-=59
            m=r%60
            for i in range(1,m+1):
                sums+=lists[i]
            files.write(str(sums%MOD)+"\n")
        else:
            m=l%60
            m2=r%60
            for i in range(m,m2+1):
                sums+=lists[i]
            #print(sums%MOD)
            files.write(str(sums%MOD)+"\n")
def fib(lists,l,r):
    lists[0]=0
    lists[1]=1
    for i in range(2,60):
        lists[i]=(lists[i-1]+lists[i-2])%10
    gen(lists,l,r)
    
f=open("input.in","r+")
files=open("output.in","w")
for i in range(int(f.readline())):
    v=f.readline()
    l,r=map(int,v.split(" "))
    if(l<=r):
        lists=[0]*60
        fib(lists,l,r)
    else:
        files.write("-1"+"\n")
    

