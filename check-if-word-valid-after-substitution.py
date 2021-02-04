# O(n^2) approach
s = "abccba"

while s.count("abc"):
    s = s.replace("abc", "")
if s == "":
    print(True)
else:
    print(False)

# # O(n) approach
# stack = []
# # for i in s:
# #     if i == 'c':
