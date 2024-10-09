prix = 250000
fraisEnregistrement = prix*0.125
honoraire = prix*0.01
admin = 1500
tva = (1500 + honoraire)*0.21
total = prix + fraisEnregistrement + honoraire + tva + admin
print("La maison coutera", total)