s = "{([])}"
list_val = []
val = {")": "(", "]": "[", "}": "{"}
for i in s:
    if i in val.values():
        list_val.append(i)
    elif i in val.keys() and len(list_val) != 0:
        if val[i] == list_val[-1]:
            list_val.pop()
        elif val[i] != list_val[-1]:
            print(False)
    else:
        print(False)
print(len(list_val) == 0)
