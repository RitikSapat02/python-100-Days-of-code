import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')
yc_webpage = response.text
 
soup = BeautifulSoup(yc_webpage,'html.parser')
# print(soup.title)
# print(soup.title.name, soup.title.string)

articles = soup.find_all(name = "span",class_='titleline')
# for article_span_tag in articles:

#     article_tag = article_span_tag.findChildren("a" , recursive=False)
#     article_text = article_tag[0].getText()
#     article_link = article_tag[0].get('href')
    
#     print(article_text)
#     print(article_link)
#     print()
    # print(article_upvote)
    # print(article_span_tags)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span',class_='score')]

article_text = []
article_link = []

for article in articles:
    article_tag = article.findChildren("a",recursive=False)

    text = article_tag[0].getText()
    article_text.append(text)
    link = article_tag[0].get('href')
    article_link.append(link)

# print(article_text)
# print(article_link)
# print(article_upvotes)


#find article info for article having highest upvotes
largest_number = max(article_upvotes)
find_index = article_upvotes.index(largest_number)

print(article_text[find_index])
print(article_link[find_index])
print(largest_number)