count = 0
number = 1
i = 2

while count < 10001:  # loop until we reach the 10001st prime
    # check if i is prime
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
        number = i
    i += 1

print(number)