import requests
from bs4 import BeautifulSoup

target_url = "https://news.ycombinator.com/"
foundLinks = []

def make_requests(url):
    response = requests.get(target_url)
    soup = BeautifulSoup(response.text, "html.parser") #html için kullanıldığını gösterir çalışmasını engellemeyen hatayı kaldırır
    return  soup

def crawl(url):
    links = make_requests(url)
    for link in links.find_all('a'):
        found_link = link.get('href')
        if found_link:
            if "#" in found_link:
                found_link = found_link.split("#")[0] #varsa önce ve sonra diye ikiye ayırıp listeler ve ilk elemanını alır
            if target_url in found_link and found_link not in foundLinks:
                foundLinks.append(found_link)
                print(found_link)
                crawl(found_link) #recursive : kendini tekrarlıyor : fonksiyonun içinde fonksiyonu çağırır

make_requests(target_url)
