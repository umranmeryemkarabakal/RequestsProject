"""
concurrent : aynı anda birden fazla işi yaptırmak, tek çekirdek üstünde taskları aynı anda yapmak taskları bölüp çalıştırırız kütüphanesi threadingtir
parallel : görevi işlemcideki çekirdeklere ayırıp çalıştırmak

"""

import threading
import requests
import time

def get_data_sync(urls):
    st = time.time() #start time
    json_array = []
    for url in urls:
        json_array.append(requests.get(url).json())
    et = time.time() #end time
    elapsed_time = et - st #geçen zaman
    print("execution time:", elapsed_time, "seconds")
    return json_array

"""
# threading kullanma:
# target çalıştıracağımız fonksiyon
# join, thread bitene kadar bekler bittikten sonra program kapanır
"""

class ThreadingDownloader(threading.Thread): #kalıtım kullanırız
    json_array = []

    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        print(self.json_array)
        return self.json_array

def get_data_threading(urls):
    st = time.time()
    threads = []
    for url in urls:
        t = ThreadingDownloader(url)
        t.start() #run fonksiyonu çalıştırır
        threads.append(t)
    for t in threads:
        t.join()
        print(t)
    et = time.time()
    elapsed_time = et - st
    print("execution time:", elapsed_time, "seconds")

urls = ["https://postman-echo.com/delay/3"] * 10
#get_data_sync(urls) #38 saniye
#get_data_threading(urls) #4 saniye