
def how_many_currency(amount: int) -> list :
    currency_sizes = (500, 200, 100, 50, 20, 10, 5, 2, 1)
    used_currency_amount = []

    currency_index = 0

    while amount > 0:
        rest = amount % currency_sizes[currency_index]
        one_currency_amount = (amount - rest) / currency_sizes[currency_index]
        amount = rest
        currency_index += 1
        used_currency_amount.append(int(one_currency_amount))

    return used_currency_amount

def print_currency(list: list):
    currency_sizes = (500, 200, 100, 50, 20, 10, 5, 2, 1)
    currency_index = 0
    for currency_amount in list:
        if currency_amount == 1 and currency_index in [7,8]:
            print("Give %d piece of %d" % (currency_amount, currency_sizes[currency_index]))

        elif currency_amount > 1 and currency_index in [7,8]:
            print("Give %d pieces of %d" % (currency_amount, currency_sizes[currency_index]))

        elif currency_amount == 1 and not (currency_index in [7,8]):
            print("Give %d bill of %d" % (currency_amount, currency_sizes[currency_index]))

        elif currency_amount > 1 and not (currency_index in [7,8]):
            print("Give %d bills of %d" % (currency_amount, currency_sizes[currency_index]))

        currency_index += 1


amount = 7483
currency_amount = how_many_currency(amount)
print_currency(currency_amount)



