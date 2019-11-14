import requests

AttributeIndexes = {
    'name': 3,
    'img': 7,
    'price': 9,
}


def splitids(ids):
    for i in range(0 , len(ids) , 50):
        yield ids[i : i + 50]


def xlmoto(search):
    productlist = []
    r = requests.post('https://xlmoto-pl.54proxy.com/search' ,
                      headers = {
                          'Content-Type': 'application/json',
                          'Accept-Encoding': 'gzip, deflate, br'
                      },
                      json={
                        "DirectResults_FromIndex": 0,
                        "DirectResults_ToIndex": 999,
                        "FilterOnVehicles": [],
                        "QueryString": search,
                        "RecommendedResults_FromIndex": 0,
                        "RecommendedResults_ToIndex": 999,
                        "Faceting.Brands": [],
                        "Faceting.Category_3": [],
                        "Faceting.Colors": [],
                        "Faceting.Sizes": []})

    if r.status_code != 200:
        return {'products': productlist}

    if not r.json()['Data']['MakesSense']:
        return {'products': productlist}

    ids = [prod['Key']['Attributes']['Id'][0] for prod in r.json()['Data']['DirectResults']]

    for ids2 in splitids(ids):
        r2 = requests.get(f'https://www.xlmoto.pl/INTERSHOP/rest/WFS/Pierce-xlmoto-Site'
                          f'/xlmoto-pl/products?pids={",".join(ids2)}')

        for product in r2.json()['elements']:
            name = product['attributes'][AttributeIndexes['name']]['value']
            img = product['attributes'][AttributeIndexes['img']]['value']
            price = product['attributes'][AttributeIndexes['price']]['value']['value']
            link = product['uri'].split('/')[-1]
            productlist.append({
                "img": img,
                "name": name,
                "price": price,
                "link": f"https://www.xlmoto.pl/products/{link}"
            })
    return {'products': productlist}
