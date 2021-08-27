#print("தமிழ்")


x =0
data = open("mltramaxcleaned.txt" , "w+" , encoding="utf-8")
data1 = open("ultracleaned.txt" , "r+" , encoding="utf-8")
for line in data1:
    line = line.replace("\n\n" , "\n")
    data.write(line)
print(x)