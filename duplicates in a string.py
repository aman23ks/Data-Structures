s = 'yhkoryenollwpjwqquwigwnebvypnigmpsdjtjylu'

letter_counter = {}
value = []

for i in s:
    if i in letter_counter:
        letter_counter[i] += 1
    else:
        letter_counter[i] = 1

for key, values in letter_counter.items():
    if values > 1:
        value.append(key)

if value == []:
    print(-1)
else:
    print(value[0])
