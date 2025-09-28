def fact(x):
    if x==0 or x==1:
        return 1
    else:
        return x*fact(x-1)  


n=str(fact(100))
sum=0
for i in range(len(n)):
    sum+=int(n[i])    
print(sum )    
