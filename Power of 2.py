def isPowerofTwo(n):
    # Your code here
    if n == 0:
        return False
    if n != 1:
        if n % 2 != 0:
            return False
        n = n//2
    return True


print(isPowerofTwo(80))
