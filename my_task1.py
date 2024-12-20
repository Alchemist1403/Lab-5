import re

file = open('task1-en.txt','r',encoding="utf-8")
file = file.readlines()


words_of_4_letters = []
fig_structured_words = []

for line in file:
    res1 = re.findall(r"\b[a-z][a-z][a-z][a-z]\b", line)
    res2 = re.findall(r"Fig[.]+ \d",line)
    res3 = re.findall(r"Fig[.]+ \d[(]+\w[)]+",line)

    for element in res1:
        words_of_4_letters.append(element)
    for element in res2:
        fig_structured_words.append(element)
    for element in res3:
        fig_structured_words.append(element)



print(sorted(list(set(fig_structured_words))))
print(sorted(list(set(words_of_4_letters))))
