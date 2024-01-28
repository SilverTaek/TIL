N = [1,0,1,1,1,0,0,1,1,0]

sum=0
cnt=0
for x in N:
    if x==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0


        