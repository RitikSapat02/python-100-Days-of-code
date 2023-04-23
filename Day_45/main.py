from bs4 import BeautifulSoup
# import lxml   #some website doesnt support html.parser

with open('./index.html') as file:
    contents = file.read()

#parsing

soup = BeautifulSoup(contents,'html.parser')             #object       #object of class (content,parser)

# print(soup)
# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

print(soup.a)      #first anchor tag
print(soup.li)      #first li tag
print(soup.p)       #first paragraph tag