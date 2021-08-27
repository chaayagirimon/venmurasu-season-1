import pandas as pd
import csv

"""
combining all CSV
df1 = pd.read_csv("chapter1.csv")
df1 = df1.T
df2 = pd.read_csv("chapter2.csv")
df2 = df2.T
df3 = pd.read_csv("chapter3.csv")
df3 = df3.T
df4 = pd.read_csv("chapter4.csv")
df4 = df4.T
df5 = pd.read_csv("chapter5.csv")
df5 = df5.T
dfTot = df1 + df2 + df3 + df4 + df5
print(dfTot.shape)
dfTot.to_csv("Combined.csv")
"""



"""
def completeClean(value):
    value = value.replace("." , "")
    value = value.replace("1" , "")
    value = value.replace("2" , "")
    value = value.replace("3" , "")
    value = value.replace("4" , "")
    value = value.replace("5" , "")
    value = value.replace("6" , "")
    value = value.replace("7" , "")
    value = value.replace("8" , "")
    value = value.replace("9" , "")
    value = value.replace("0" , "")
    return value


def containsNumber(value):
    if True in [char.isdigit() for char in value]:
        return True
    return False

data = open("mltramaxcleaned.txt" , "w+" , encoding="utf-8")
final = pd.DataFrame
clean = open("cleaned.txt" , "r+" ,encoding="utf-8")
no_of_lines = 0
no_of_words = 0
point = "."
for line in clean:
    if point in line:
        no_of_lines +=1

    if containsNumber(line):
        no_of_lines -= 1

    line = completeClean(line)
    no_of_words +=1
    
    data.write(line)
print(no_of_lines)
print(no_of_words)

"""