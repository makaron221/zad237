from bs4 import BeautifulSoup

with open("task1.html") as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")
hcontent = []
for i in range(1, 7): hcontent += list(map(lambda x: x.contents[0], soup.find_all("h"+str(i))))
h1classcontent = list(map(lambda x: x.contents[0], soup.find_all(attrs={"class":"h1"})))
white_text_and_black_bgcontent =  soup.find_all(attrs={"class":"white-text-and-black-bg"})
print(f"Всі змісти заголовків:\n {hcontent}")
print(f"Всі теги в яких був використаний клас h1:\n {h1classcontent}")
print(f"Всі теги в яких був використаний клас white-text-and-black-bg:\n white_text_and_black_bgcontent")