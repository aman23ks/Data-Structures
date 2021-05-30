def minFlips(S):
    # Code here
    c1 = 0
    c2 = 0
    for i in range(len(S)):
        if (i+1) % 2 == 0 and S[i] == "1":
            continue
        elif (i+1) % 2 == 0 and S[i] != "1":
            c1 += 1
        if (i+1) % 2 != 0 and S[i] == "0":
            continue
        elif (i+1) % 2 != 0 and S[i] != "0":
            c1 += 1
    for i in range(len(S)):
        if (i+1) % 2 == 0 and S[i] == "0":
            continue
        elif (i+1) % 2 == 0 and S[i] != "0":
            c2 += 1
        if (i+1) % 2 != 0 and S[i] == "1":
            continue
        elif (i+1) % 2 != 0 and S[i] != "1":
            c2 += 1

    return min(c1, c2)


S = "001"
print(minFlips(S))
