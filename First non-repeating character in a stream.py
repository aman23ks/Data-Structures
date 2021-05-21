def FirstNonRepeating(A):
    # Code here
    hashmap = {}
    queue = []
    output = ""
    # A = list(A)

    for i in range(len(A)):
        ele = A[i]
        if ele not in hashmap:
            hashmap[ele] = 1
        else:
            hashmap[ele] += 1

        if hashmap[ele] == 1:
            queue.append(ele)

        while queue:
            if hashmap[queue[0]] == 1:
                output += queue[0]
                break
            else:
                queue.pop(0)

        if queue == []:
            output += "#"

    return output


print(FirstNonRepeating("aabccdba"))
