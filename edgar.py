from bs4 import BeautifulSoup
import re
import requests
import os

link_list = [ ]

base_url = "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001383701&type=&datea=20140930&owner=exclude&output=xml&count=10"
r = requests.get(base_url)
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('filinghref'):
	#print link
	l1 = str(link)
	#print type(l1)
	l2 = l1.replace('<filinghref>','')
	#print l2
	l3 = l2.replace('</filinghref>','')
	link_list.append(l3)
'''
for url in link_list:
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data)
	print soup
'''

#while '<filinghref>' in link_str:
#	link_str.remove('<filinghref>')

print link_list
base_url = link_list[0]
r = requests.get(base_url)
data = r.text
soup = BeautifulSoup(data)
print soup
#l2 = l1.strip('<filinghref>')
#l3 = l2.strip('</filinghref>')