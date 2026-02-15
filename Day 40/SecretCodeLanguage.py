"""
Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language.

Rules:
Coding ->
1. If the word contains at least 3 characters, remove the first letter and append it at the end. Now append three random characters at the starting and the end.
2. Else simply reverse the string.

Decoding ->
1. If the word contains less than 3 characters, reverse it.
2. Else remove 3 random characters from start and end. now remove the last letter and append it to the beginning
"""

st = input("Enter Message: ")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding: ")
coding = True if (coding == "1") else False

if (coding):
    nwords = []
    for word in words:
        if (len(word) >= 3):
            r1 = "dsf"
            r2 = "jkr"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if (len(word) >= 3):
            stnew = word[3 : -3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
