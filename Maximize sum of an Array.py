# Maximize sum(arr[i]*i) of an Array
def Maximize(a, n):
     # Complete the function
        sum = 0
        a.sort()
        for i in range(len(a)):
            sum += a[i]*i

        return int(sum % (pow(10, 9) + 7))


Arr = [5, 3, 2, 4, 1]
n = len(Arr)
print(Maximize(Arr,n))