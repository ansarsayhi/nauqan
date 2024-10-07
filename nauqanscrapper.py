from playwright.sync_api import sync_playwright
import json

def set_up():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True, downloads_path="/Users/ansarantayev/Documents/nauqas/nauqas1/screens")
    wpage = browser.new_page()
    wpage.goto("https://magnum.kz/catalog?discountType=all&srsltid=AfmBOooqQYGKrKrv5dq4De7wQgcxqnewJJQ8Hq8An_zVKJ_0ZVvZcRX0&city=almaty")
    return p, browser, wpage


def get_products(wpage, filename):

    def get_yest_names(filename):
        with open(filename, 'r') as file:
            yest_names = set(json.load(file))
        return yest_names
    
    yest_names = get_yest_names(filename)
    new_names = list()
    products = wpage.query_selector_all('.product-block')
    
    for product in products:
        name = product.query_selector('a.product-block__item > span.product-block__content > span.product-block__right > span:nth-child(2)').inner_text()
        yest_names_ln = len(yest_names)
        yest_names.append(name)
        
        if len(yest_names) > yest_names_ln:
            product.screenshot(path = f"{name}.png")
        new_names.append(name)

    with open(filename, 'w') as file:
        json.dump(list(new_names), file)
        

def tear_down(browser, p):
    if browser:
        browser.close()
    if p:
        p.stop()
    




if __name__ == "__main__":
    p, browser, wpage = set_up()
    products = get_products(wpage)
    get_products(wpage, filename='discountset.json')
    tear_down(browser, p)
