import pandas as pd

data = open("mltramaxcleaned.txt" , "r+" , encoding="utf-8")

data1 = open("Final_and_analysed1.txt" , "w+" , encoding="utf-8")

lst = []
for line in data:
    lst.append(line)
unique = dict(zip(lst,[lst.count(i) for i in lst]))
print("Unique items: ", len(unique))


unique1 = list(set(lst))
frequency = {}
for item in unique1:
    frequency[item] = lst.count(item)
#print(frequency)
string1 = str(frequency)
data1.write(string1)