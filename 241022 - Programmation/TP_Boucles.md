# 1. différence
## a.
```
e = 0
while e < 10:
    print(e+1)
    print(e)
    e += 1
```

## b.
pas possible de faire une boucle infinie avec un for

# 2. Triple boucle
ça affichera:
```
0 0 0
0 0 1
0 0 2
0 1 0
0 1 1
0 1 2
0 2 0
0 2 1
0 2 2
1 0 0
1 0 1
1 0 2
1 1 0
1 1 1
1 1 2
1 2 0
1 2 1
1 2 2
2 0 0
2 0 1
2 0 2
2 1 0
2 1 1
2 1 2
2 2 0
2 2 1
2 2 2
```

# 3. Somme liste
```
sum_number = 0

for number in [2, 4, 6, 8, 10]:
    sum_number += number

print(sum_number)
```

# 4. Product list
```
mult_number = 1

for number in [1, 2, 3, 4, 5]:
    mult_number *= number

print(mult_number)
```

# 5. Factorielle
```
total = 1

for fact in range(2, 5 + 1)
    total *= fact
    
print(total)
```

# 6. Somme chiffre d'un nombre
```
number = 12345
str_number = str(number)

result = 0

iterator = 0

while iterator < len(str_number):
    result += int(str_number[iterator])
    iterator += 1

print(result)
```

# 7. Dividers of number

```
number = 12
divider_list = []

for div in range(1, 12 + 1):
    if number % div == 0:
        divider_list.append(div)

print(len(divider_list))
```

# 8. display mult

```
start_number = 2
end_number = 5

for front_number in range(start_number, end_number + 1):
    for multiplier in range(1, 11):
        multiplication = front_number * multiplier
        print("%d * %d = %d" % (front_number, multiplier, multiplication))
```

# 9. generate odd
```
for number in range(1, 20, 2):
    print(number)
```

# 10. multiples sum

```
total_sum = 0
for number in range(1, 1000):
    if number % 3 == 0 or number % 5 == 0:
        total_sum += number
        
print(total_sum)
```