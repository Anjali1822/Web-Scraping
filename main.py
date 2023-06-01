#Web Scrappping Practice

import requests
from bs4 import BeautifulSoup
url="https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/"

#Step 1 : Get the HTML
r=requests.get(url)
htmlContent=r.content
#print(htmlContent)

#step 2 : parse the HTML
soup=BeautifulSoup(htmlContent,'html.parser') #creating the soup
#print(soup.prettify)#display the content/text beautiful

#step 3 : HTML Tree Traversal : (soup is tree)
#Commonly Used types of objects
#1.Tag                print(type(title))
#2.NavigableString    print(type(title.string))
#3.BeautifulSoup      print(type(soup))
#4.Comment

#Get the title of the HTML Page
title=soup.title
#print(title) #title tag is print

#Get all the paragraphs from the page
paras=soup.find_all('p')
#print(paras)

#Get all the anchor tags from the page
anchors=soup.find_all('a')
#print(anchors)

#print(soup.find('p'))#First Para : Get First element in HTML page
#print(soup.find('p')['class'])   Get class/id of any element in the HTML page

#Find all the elements with class lead
#print(soup.find_all("p",class_="lead"))

#Get the text from tags/soup
#print(soup.find('p').get_text())
#print(soup.get_text())


all_links=set()
#Get all the links on the page::
for link in anchors:
    if(link.get('href')!='#'):
        linkText="https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/"+link.get('href')
        all_links.add(link)
       # print(linkText)


#4.Comment
markup="<p><!-- this is a comment --></p>"
soup2=BeautifulSoup(markup)
#print(soup2.p.string) #type ()

#ID 
#.contents = A tag's children are available as list. _content saved in memory.
#.children = A tag's children are available as a generator _got through iteration _not saved in memory


navbarSupportedContent=soup.find(id='td-outer-wrap')
#for elm in navbarSupportedContent.contents:#children #content : Get all the content from website
   #print(elm)

#for item in navbarSupportedContent.stripped_strings:   #all the Strings in page
 #   print(item)

#print(navbarSupportedContent.parent)#print the parent of object 
#print(navbarSupportedContent.parents)#print object of parent

#for item in navbarSupportedContent.parents:
#    print(item.name)

#print(navbarSupportedContent.next_sibling.next_sibling)
#print(navbarSupportedContent.previous_sibling.previous_sibling)

elem=soup.select('.td-scroll-up')
print(elem)