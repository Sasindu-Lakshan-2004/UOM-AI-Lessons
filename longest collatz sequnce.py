max_count = 0
num_with_max_count = 0
memo = {}

for number in range(1, 1000000):
    num = number
    count = 0
    while num != 1:
        if num in memo:
            count += memo[num]
            break
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
        count += 1
    memo[number] = count
    if count > max_count:
        max_count = count
        num_with_max_count = number

print(f"Maximum steps: {max_count}, Number: {num_with_max_count}")

