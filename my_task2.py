import re

file = open('task2.html','r',encoding="utf-8")
file = file.readlines()

style = []
weight = []

for line in file:
    res1 = re.findall(r"font-style: (\w+);", line)
    res2 = re.findall(r"size: (\d+)px",line)
    
    for element in res1:
        style.append(element)
    for element in res2:
        weight.append(element)

print(f"Used styles: {list(set(style))}")
print(f"Used sizes(px): {list(set(weight))}")