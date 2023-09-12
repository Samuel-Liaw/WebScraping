from bs4 import BeautifulSoup
import requests

booklist = []
pages = range(1,6)
for page in pages:
    url = f'https://books.toscrape.com/catalogue/page-{page}.html'
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'lxml')
    content = soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    # print(soup.prettify())
    # print(content)
    for book in content:
        name = book.find('a').find('img')['alt']
        rating = book.find('p')['class'][1]
        price = float(book.find('div', class_="product_price").find('p', class_="price_color").text[2:])
        booklist.append([name, rating, price])
import pandas as pd
df = pd.DataFrame(booklist)
df.columns = ['Book', 'Rating', 'Price']
df.to_csv('book.csv')