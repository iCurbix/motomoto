from bs4 import BeautifulSoup
import requests
from math import ceil


def fourbiker_products_on_page(soup , search):
    productlist = []
    products = soup.select(".product.s-grid-3.product-main-wrap")
    for product in products:
        name = product.select(".productname")[0].text.lower()
        if not all(i in name for i in search.lower().split()): continue
        img = product.select("img img")[0].get("src")
        price = float(''.join(filter(lambda x: x.isdigit() or x == '.', product.select(".price em")[0].text.replace(',', '.'))))
        link = product.select("a")[0].get("href")
        productlist.append({
            "img": f"https://sklep4biker.pl{img}",
            "name": name,
            "price": price,
            "link": f"https://sklep4biker.pl{link}"
        })
    return productlist


def fourbiker(search):
    productslist = []

    i = 1
    r = requests.get(f"https://sklep4biker.pl/pl/searchquery/{search}/{i}")
    soup = BeautifulSoup(r.text, "html.parser")
    maxpage = ceil(int(soup.select("#box_mainproducts > div.boxhead > .category-name")[0].text.strip().split()[-1])/30)

    productslist.extend(fourbiker_products_on_page(soup , search))

    for i in range(1 , maxpage):
        r = requests.get(f"https://sklep4biker.pl/pl/searchquery/{search}/" + str(i := i + 1))
        soup = BeautifulSoup(r.text, "html.parser")
        productslist.extend(fourbiker_products_on_page(soup, search))

    return productslist
