T = 'CATATCGGCATA'
P = 'ATA'

n = len(T)  # length of the given text
m = len(P)  # length of the pattern needed to be found in the text


# Funtion for hashing the characters
def hash(s, m):
    d = 0
    i = 1
    while i <= m:  # Taking 101 as the base case, base case can be any value
        d += 101**(m-i) * ord(s[i-1])
        i += 1

    return d

# Function for rolling hash


def rollHash(oldhash, remChar, insChar, m):
    oldhash = oldhash - (101**(m-1) * ord(remChar))
    oldhash *= 101
    oldhash += ord(insChar) * 101**(0)
    return oldhash


pHashed = hash(P, m)
tHashed = hash(T[0:m], m)

i = 0
found = False

while i < n-m+1:
    if pHashed == tHashed and P == T[i:i+m]:
        found = True
        print("Match found at position", i)
    if i < n-m:
        tHashed = rollHash(tHashed, T[i], T[i+m], m)
    i += 1

if not found:
    print("No matches found")
