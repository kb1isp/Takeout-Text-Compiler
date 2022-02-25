import fnmatch
import os
import codecs
from bs4 import BeautifulSoup
import csv

html_doc = ""

with open('calls.csv', 'w', newline='') as csvfile:
    fieldnames = ['datetime', 'tel', 'text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for file in os.listdir('/home/kali/calls'): #Had a directory full of the Google Takeout HTML files. Running on a VM, so change this to your directory of choice.
        if fnmatch.fnmatch(file, '*.html'):
            print(file)
            f=codecs.open(file, 'r') 
            html_doc = f.read()
            soup = BeautifulSoup(html_doc, 'html.parser')

            body = soup.body
            divM = body.find('div')
            childDiv = divM.findChildren('div', recursive=False)
            
            for message in childDiv:
                messList = [message.abbr['title'].strip(), message.a['href'].strip(), message.q.text.strip()]
                dictLine = {fieldnames[0]:messList[0],fieldnames[1]:messList[1],fieldnames[2]:messList[2]} #Probably some string comprehension could be done here.
                print(dictLine)
                writer.writerow(dictLine)
