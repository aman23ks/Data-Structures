A = 'abcde'
B = 'cdeab'
if A == B:
            print(True)
else:
            for i in range(len(A)):
                val = A[0]
                A = A + val
                A = A[1:]
                if A == B:
                     print(True)  
            print(False)
