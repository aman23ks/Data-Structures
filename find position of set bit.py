def findPosition(self, N):
    # code here
    # Time complexity O(N) and space complexity O(1). time complexity can be reduced to O(logN).
    count = 0
    val = 0

    while N > 0:
        val += 1
        if N & 1:
            count += 1
        N = N >> 1

    if count != 1:
        return -1
    else:
        return val
