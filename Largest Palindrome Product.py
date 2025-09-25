digit_count=3
first_num=100
second_bum=100
max_num=0
for i in range(100,1000):
      for j in range(i,1000):
           number=str(i*j)
           mirror=number[::-1]
           if number==mirror and (i*j)>max_num:
                 max_num=i*j
print(max_num)                 