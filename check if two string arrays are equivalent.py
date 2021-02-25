word1 = ["abc", "d", "defg"]
word2 = ["abcddefg"]


def combiner(word):
    word_combined = ""
    for i in word:
        word_combined += i
    return word_combined


if combiner(word1) == combiner(word2):
    print(True)
else:
    print(False)
