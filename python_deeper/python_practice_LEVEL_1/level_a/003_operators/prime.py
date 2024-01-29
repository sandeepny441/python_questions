def is_prime(given_num):
    for num in range(2, int(given_num**0.5) +1):
        if given_num % num == 0:
            return 'Not Prime' 
    return "Prime" 

for num in range(3,100):
    print(num, '--> ', is_prime(num))


