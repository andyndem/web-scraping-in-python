from requests_html import HTMLSession
import csv

s = HTMLSession()


def get_product_links(page):
    product_links = []
    url = f'https://themes.woocommerce.com/storefront/product-category/clothing/page/{page}'
    r = s.get(url)
    products = r.html.find('ul.products li')
    for product in products:
        product_links.append(product.find('a', first=True).attrs['href'])
    return product_links

# page1 = get_product_links(1)
# print(page1)


def parse_product(url):
    r = s.get(url)
    title = r.html.find('h1.product_title.entry-title', first=True).text.strip()
    price = r.html.find('p.price', first=True).text.strip().replace('\n', ' ')
    cat = r.html.find('span.posted_in', first=True).text.strip()
    try:
        sku = r.html.find('span.sku', first=True).text.strip()
    except AttributeError as err:
        sku = 'None'
        # print(err)
        # print(title, price, sku, cat)

    product = {
        'title': title,
        'price': price,
        'sku': sku,
        'cat': cat,
        }
    return product


# To write a dictionary data to csv file
def save_csv(results):
    keys = results[0].keys() # For header rows
    with open('products.csv', 'w') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)


def main():
# For each urls in range(1, 3) of pages, grap the urls for that page, loop thru them and get me the products
    results = []
    for x in range(1, 4):
        print('Getting Page: ', x)
        urls = get_product_links(x)
        for url in urls:
            # print(parse_product(url))
            results.append(parse_product(url))
        print('Total Results: ', len(results))
        save_csv(results)
    # print(results)
        print('saved, complete')


if __name__ == '__main__':
    main()
