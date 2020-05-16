from bs4 import BeautifulSoup
from selenium import webdriver



# with open("ig.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')

# print(soup.find_all('img'))

url = 'https://www.instagram.com/mayarahealingarts/'
driver = webdriver.Firefox()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

print(soup.findAll('img', 'src'))
# for x in soup.findAll('li', {'class':'photo'}):
#     print(x)
for line in soup.find_all('img'):
    print(line.get('src'))
