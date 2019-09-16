S=input()
list=[]
sum=0
N=[int(m) for m in S]
if(int(S) <= 10000000000):
    for i in N:
        if(i%2!=0):
            list.append(i)
    for i in list:
        sum=sum+i
    if(sum%2==0):
        print("E")
    else:
        print("O")
