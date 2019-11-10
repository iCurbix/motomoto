from bs4 import BeautifulSoup
import requests
from collections import Counter


def fourbiker(search):
    r = requests.get("https://sklep4biker.pl/pl/searchquery/" + search)
    soup = BeautifulSoup(r.text, "html.parser")
    products = soup.select(".product.s-grid-3.product-main-wrap")
    productslist = []

    for product in products:
        name = product.select(".productname")[0].text.lower()
        if not all(i in name for i in search.lower().split()): continue
        img = product.select("img img")[0].get("src")
        price = float(product.select(".price em")[0].text.split()[0].replace(',' , '.'))
        link = product.select("a")[0].get("href")
        productslist.append({
            "img": f"https://sklep4biker.pl{img}",
            "name": name,
            "price": price,
            "link": f"https://sklep4biker.pl{link}"
        })

    return productslist