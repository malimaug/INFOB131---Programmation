import random
line = "---------------------------------------------------------------------------------------------"



# exo1:
print("Hello World!")

print(line)
# exo2:
print(3 + 4)

print(line)
# exo3:
x = 3
y = 4
print (x + y)

print(line)
# exo4:
age = 18
print(f"J'ai {age} ans.")

print(line)
# exo5:
price = 100
discount = 20
reduction_amount = price * (discount * 0.01)
final_price = price - reduction_amount

print(f"Le prix de départ est de {price}€, la réduction est de {discount}% et le prix final est de {final_price}€.")

print(line)
# exo6:
# on définit les diférent prix des différents éléments
minerval = 900
logement = 350
nouriture = 250

# calcul du prix sur 5 ans
price_5years = ((logement + nouriture) * 12 + minerval) * 5

# affichage du prix
print(f"5 ans d'études coute {price_5years}€.")

print(line)
# exo7:
nbr_aleatoire = random.randint(1, 100)

print(nbr_aleatoire)

print(line)
# exo8:
nbr1 = random.randint(1, 100)
nbr2 = random.randint(1,100)

somme =  nbr1 + nbr2

print(somme)

print(line)
# exo9:
a = 42
b = a / 2
a = a + 1
c = a + 1
d = a + b + c

print(a, b, c, d)

a = 2
b = 3
a = 2 * a
a = a + b
c = a + b
a = 2
d = a + b

print(a, b, c, d)