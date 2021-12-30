from time import sleep
from requests_html import HTMLSession, AsyncHTMLSession
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

url = "https://www.pccomponentes.com/asus-geforce-rtx-2060-dual-oc-evo-edition-6gb-gddr6"
url_coolmod = "https://www.coolmod.com/asus-tuf-gaming-a15-fa506ii-bq029-ryzen-7-4800h-16gb-1tb-ssd-gtx-1650-ti-freedos-156-portatil-precio"
session = HTMLSession()
product_page = session.get(url_coolmod)
found = product_page.html.find("#main-buy")


def stock_coolmod():


def stock_found(buy_zone):
    while True:
        r = session.get(url)
        buy_zone = r.html.find("#btnsWishAddBuy")
        if len(buy_zone) > 0:
            print("Hay Stock!!!")
            break
            
        else:
            print("Aun no hay Stock :( ")
            sleep(5)


def main():
    stock_found(buy_zone=True)


if __name__ == "__main__":
    main()
