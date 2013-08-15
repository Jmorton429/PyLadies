#!/usr/bin/python
# -*- coding: UTF-8 -*-
# included in this folder is an html file called wynn.html
# 
# if you view it in a browser you will see that it shows a series of hotel room names and their prices.
# 
# Write code that extracts the rooom names and their corresponding price.
# 
# Input: wynn.html
# Output: [ ["Resort Suite King", 151], ["Panoramic View King", 239], ....etc]
#
# Requires installation:
# easy_install beautifulsoup4
# easy_install lxml

#this seemed to be the most efficient parser
from bs4 import BeautifulSoup
from collections import defaultdict
#instantiating the lists
hlist=[]
plist=[]
#open up the html file
doc = BeautifulSoup(open("wynn.html"))
#find all the hotels
hotels = doc.find_all("a", "togglelink jqrt")
#find all the prices
prices = doc.find_all("strong", "click_change_currency")
#get the text from the html and put in a list
for hotel in hotels:
	hlist.append(hotel.get_text())
for price in prices:
	plist.append(price.get_text())
i=0
#instantiate the defaultdict
hl = defaultdict(str)
#match list of rooms with prices and add to dictionary
while i<len(hlist):
	hl[hlist[i]]=plist[i]
	i+=1

print hl.items()