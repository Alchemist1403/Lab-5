import re


file = open('task_add.txt','r',encoding="utf-8")
file = file.readlines()

hidden_sites = []
hidden_dates = []
hidden_addresses = []
for line in file:
    res1 = re.findall(r" [\w]*@[\w]+\.\w\w\w", line) # Почты
    res2 = re.findall(r"http[s]*://[a-z]*.[a-z]*", line) # Сайты
    res3 = re.findall(r"[\d]+\.[\d]+\.[\d]+", line) # Даты (точки)
    res4 = re.findall(r"[\d]+-[\d]+-[\d]{2}", line) # Даты (тире + другой формат)
    res5 = re.findall(r"[\d]+-[\d]+-[\d]{4}", line) # Даты (тире)

    if len(res1) > 0:
        hidden_addresses.append(res1)
    if len(res2) > 0:
        hidden_sites.append(res2)
    if len(res3) > 0:
        hidden_dates.append(res3)
    if len(res4) > 0:
        hidden_dates.append(res4)
    if len(res5) > 0:
        hidden_dates.append(res5)
    

print(f"Спрятанные:\nПочты:{hidden_addresses}\nСайты:{hidden_sites}\nДаты:{hidden_dates}")
print("Примечание: в доменах почт и адресов могут быть лишние буквы или символы.")
print("Ненужные буквы можно легко вычеркнуть после нахождения основной части адреса или почты.")
