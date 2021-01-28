s = "abccba"

while s.count("abc"):
    s = s.replace("abc", "")
if s == "":
    print(True)
else:
    print(False)
