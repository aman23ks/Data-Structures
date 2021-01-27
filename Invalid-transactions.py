transactions = ["alice,20,1220,mtv", "alice,20,1220,mtv"]

if len(transactions) == 0:
    print([])

invalid_transactions = []

for i in range(len(transactions)):
    first_parts = transactions[i].split(',')

    if int(first_parts[2]) > 1000:
        invalid_transactions.append(transactions[i])

    for j in range(len(transactions)):
        second_parts = transactions[j].split(',')
        if i is not j:
            if first_parts[0] == second_parts[0] and abs(int(first_parts[1]) - int(second_parts[1])) <= 60 and first_parts[3] != second_parts[3]:
                invalid_transactions.append(transactions[i])
                invalid_transactions.append(transactions[j])

print(list(set(invalid_transactions)))
