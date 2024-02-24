import requests
import lxml
from bs4 import BeautifulSoup

session = requests.Session()
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

for j in range(1, 10):
    url = f"https://rozetka.com.ua/notebooks/c80004/page={j}"
    print(f"PAGE")
    response = session.get(url, headers=header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_products = soup.find('ul', class_="catalog-grid ng-star-inserted")
        products = all_products.find_all('div', class_="goods-tile__content")

        for elem in products:
            try:
                elem.find("div", class_="goods-tile__price--old price--gray ng-star-inserted")
                get_name = elem.find("div", class_="goods-tile__title").text
                get_price = elem.find("div", class_="goods-tile__price-value").text

                with open("result.txt", "a", encoding="utf-8") as file:
                    file.write(f"{get_name} -->> {get_price}\n")
            except:
                print(f"{products} - знижки немає")
