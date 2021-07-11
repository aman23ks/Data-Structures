price = [10, 7, 19]
k = 45

values = []

total_stocks = 0
total = 0

for i in range(len(price)):
    values.append([price[i], i+1])

values.sort()

for i in range(len(values)):
    stock_cost = values[i][0]
    amount = values[i][1]
    if stock_cost*amount <= k:
        total_stocks += amount
        k -= stock_cost*amount
        total += stock_cost*amount
    else:
        total_stocks += k//stock_cost
        temp = k
        k -= (k//stock_cost)*stock_cost
        total += (temp//stock_cost)*stock_cost

print(total, total_stocks)

print(values)
