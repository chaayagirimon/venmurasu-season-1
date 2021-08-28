from bs4 import BeautifulSoup
import lxml.html as lhtml
from lxml import etree, html
import requests
import csv

def startpy(number):
    source  = requests.get("https://venmurasu.in/mutharkanal/chapter-" + str(number)).text

    soup =  BeautifulSoup(source, 'lxml')

    csv_file = open('chapter'+str(number) + '.csv','w')
    csv_writer = csv.writer(csv_file)

    word_list = []

    paragraph = soup.find_all('p')

    
    for para in paragraph:
        word_list.append(para.text.split())
        # print(word)
    finallist = [ item for elem in word_list for item in elem]
    
    csv_writer.writerow(finallist)

# def 

if __name__ == "__main__":
    for num in range(1,6):
        startpy(num)
