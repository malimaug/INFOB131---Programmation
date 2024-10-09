water_consumption = 15
CVD = 2.16
CVA = 2.35
water_price = 0

redevance = 20 * CVD + 30 * CVA

if water_consumption < 0:
    print("error")
elif water_consumption < 30:
    water_price = 0.5 * water_consumption * CVD
elif water_consumption < 5000:
    water_price = water_consumption * CVD + water_consumption * CVA
else:
    water_price = 0.9 * water_consumption * CVD + water_consumption * CVA


total = redevance + water_price
print(f"ça coutera {total}$")