maximum_number=20
needed_numbers=[2]

for i in range(3, maximum_number+1):
    divisible = False
    for j in needed_numbers:
        if i % j == 0:
            divisible = True
            break
    if not divisible:
        needed_numbers.append(i)

evenly_div_num=1
for i in needed_numbers:
    evenly_div_num *= i

print(needed_numbers)
print(evenly_div_num)
