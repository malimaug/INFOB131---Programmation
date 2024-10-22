import time
import math


def is_prime_number(number: int):
    for div in range(3, math.floor(math.sqrt(number)) +1, 2):
        if number % div == 0:
            return False

    return True


amount_of_primes = 1000000



# variante générale
start_time = time.time()

number_basic = 3
found_primes_basic = 1
list_primes_2 = [2]

while amount_of_primes > found_primes_basic:
    if is_prime_number(number_basic):
        found_primes_basic += 1
        list_primes_2.append(number_basic)
    number_basic += 2


print("--- %s seconds ---" % (time.time() - start_time))

print(number_basic, "is the", amount_of_primes, "prime number")

