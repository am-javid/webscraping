from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

service = webdriver.ChromeService(executable_path = '/Users/Amelia/Desktop/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/a~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq=")

content = driver.page_source
soup = BeautifulSoup(content, features = "html.parser")
# for a in soup.findAll('a',href=True, attrs={'class':'_1YokD2 _3Mn1Gg'}):
for a in soup.findAll('div', attrs={'class':'_1YokD2 _3Mn1Gg'}):
    name=a.find('div', attrs={'class':'_4rR01T'})
    price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=a.find('div', attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')