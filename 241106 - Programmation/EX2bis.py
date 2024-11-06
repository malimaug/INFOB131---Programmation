def how_many_currency(amount: int):
    currency_sizes = {500 :0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}


    for bill_size in currency_sizes:
        rest = amount % bill_size
        bill_amount = (amount - rest) / bill_size
        amount = rest
        currency_sizes[bill_size] += int(bill_amount)

    return currency_sizes

amount = 250
print(how_many_currency(amount))