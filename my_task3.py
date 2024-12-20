import re


file = open('task3.txt','r',encoding="utf-8")
file = file.readlines()

for line in file:
    res1 = re.findall(r"[^\s]*@[^\s]* ", line) # электронный аддресс
    res2 = re.findall(r"[A-Z][a-z]* ", line) # фамилия
    res3 = re.findall(r"http[^\s]* ", line) # сайт
    res4 = re.findall(r"[\d]*-[\d]*-[\d]*", line) # дата

f = open("task.csv",'w',encoding="utf-8")

for id_of_person in range(len(res1)+1):
    if id_of_person == 0:
        f.write("ID;Surname;Address;Date;Site")
    f.write(f"{id_of_person};{res2[id_of_person-1]};{res1[id_of_person-1]};{res4[id_of_person-1]};{res3[id_of_person-1]}\n")
    
f.close()