from requests_html import HTMLSession
import csv

s = HTMLSession()
#
# def get_product_links(page):
product_links = []
url = f'https://themes.woocommerce.com/storefront/product-category/clothing/page/2'
r = s.get(url)

products = r.html.find('ul.products li')
for product in products:
    print(product.find('a', first=True).attrs['href'])
    product_links.append(product.find('a', first=True).attrs['href'])
    # return product_links
    print(product_links)


# def parse_product(link):
test_link = 'https://themes.woocommerce.com/storefront/product/lowepro-slingshot-edge-250-aw/'
r = s.get(test_link)
title = r.html.find('h1.product_title.entry-title', first=True).text.strip()
price = r.html.find('p.price', first=True).text.strip()
sku = r.html.find('span.sku', first=True).text.strip()
cat = r.html.find('span.posted_in', first=True).text.strip()

print(title, price, sku, cat)
