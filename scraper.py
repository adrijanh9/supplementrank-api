from bs4 import BeautifulSoup
import requests
import json

def getHtml(url):

    resp = requests.get(url)

    if resp.status_code != 200:
        raise Exception("request failed")
    
    return resp.content

def getProducts():

    product_list = []

    #-----------------------------------
    # Polleo Sport hr
    #-----------------------------------

    store = "https://polleosport.hr/proteini/whey-protein/"
    soup = BeautifulSoup(getHtml(store), 'html.parser')

    contents = soup.find_all("div", {"class": "item product-layout polleo-new-product"})

    for product in contents:

        p_name = product.findChild("div", {"class": "name"}).find("a").text

        p_link = product.findChild("div", {"class": "name"}).findChild("a")["href"]

        p_img = product.findChild("div", {"class": "image"}).find("img")["src"]

        discounted = product.findChild("span", {"class": "price-new"})


        if discounted:

            p_priceold = product.findChild("span", {"class": "price-old"}).text.split("k")[0].replace(".", "").replace(",",".")
            p_price = discounted.text.split("k")[0].replace(".", "").replace(",",".")

            p_discount = round((1 - (float(p_price)/float(p_priceold))) * 100)

            p_price = p_price + "kn"

            p_discount = str(p_discount) + "%"
        else:

            p_price = product.findChild("div", {"class": "price"}).findChild("span").text.split("k")[0].replace(".", "").replace(",",".")

            p_price = p_price + "kn"

            p_priceold = 0
            p_discount = 0

        item = {

            "name" : p_name,
            "link": p_link,
            "image" : p_img,
            "price" : p_price,
            "discount" : p_discount
        }

        product_list.append(item)



    #-----------------------------------
    # Proteone hr
    #-----------------------------------

    store = "https://proteone.hr/proizvodi/proteini/"
    soup = BeautifulSoup(getHtml(store), 'html.parser')

    contents = soup.find_all("div", {"class": "clear cp"})


    for product in contents:

        p_name = product.findChild("div", {"class": "cp-title"}).text

        p_link = product.findChild("div", {"class": "cp-title"}).findChild("a")["href"]

        p_img = product.findChild("img")["data-lazy"]

        discounted = product.findChild("div", {"class": "cp-discount-price red"})

        
        if discounted:

            p_priceold = product.findChild("div", {"class": "cp-old-price line-through"}).text.split("k")[0].replace(".", "").replace(",",".")
            p_price = discounted.text.split("k")[0].replace(".", "").replace(",",".")

            p_discount = round((1 - (float(p_price)/float(p_priceold))) * 100)

            p_price = p_price[:-1] + "kn"

            p_discount = str(p_discount) + "%"
        else:

            p_price = product.findChild("div", {"class": "cp-current-price"}).text.split("k")[0].replace(".", "").replace(",",".")

            p_price = p_price[:-1] + "kn"

            p_priceold = 0
            p_discount = 0

        item = {

            "name" : p_name,
            "link": p_link,
            "image" : p_img,
            "price" : p_price,
            "discount" : p_discount
        }

        product_list.append(item)
        
    return product_list

    
            


    