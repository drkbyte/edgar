from bs4 import BeautifulSoup
import re
import requests
import os

link_list = [ ]

base_url = "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=CNAT&type=10-Q&datea=20140930&owner=exclude&output=xml&count=10"
r = requests.get(base_url)
data = r.text
soup = BeautifulSoup(data)
 
for link in soup.find_all('filinghref'):
	l1 = str(link)
	l2 = l1.replace('<filinghref>','')
	link_list = l2.replace('</filinghref>','')

r = requests.get(link_list)
data = r.text
soup = BeautifulSoup(data)

listr = [ ]

for link in soup.find_all('a'):
	listr.append(link)

for l in listr:
	print l

listr[9]
new_link = 	listr[9]
n2 = str(new_link)
n3 = n2.replace('<a href="','http://www.sec.gov')
n4 = n3.partition('"')
n5 = n4[0]
source_doc = str(n5)
print source_doc
