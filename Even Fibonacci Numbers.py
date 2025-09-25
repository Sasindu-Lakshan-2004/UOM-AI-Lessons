maximum_number=4000000
n1=1
n2=1
n3=0
total=0
while n3<=maximum_number:
    n3=n1+n2
    if n3%2 == 0:
        total+=n3
    n1,n2=n2,n3
print(total) 