# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))          # 0 == input int
# total_words = pages * word_per_page
# print(total_words)

##solved👇
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
print(f"pages = {pages}\nword_per_page = {word_per_page}")
total_words = pages * word_per_page
print(total_words)
