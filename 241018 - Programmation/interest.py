import math
yearly_interest =  1.06
weekly_interest = yearly_interest ** (1/52)
money1 = 1000
money2 = 1000

for year_id in range(1, 12063):
    for week_id in range(1, 54):
        money1 *= weekly_interest

    money2 *=  yearly_interest

print(money1)
print(money2)

