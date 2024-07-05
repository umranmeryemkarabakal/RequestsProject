"""
dns domain ismi çözümleyici domain name : google.com, canva.com
api : application programming interface
django : web frame work 
json formatı bir gösterim şeklidir,örn:
[{"currency":"0XBTC","price":"0.19788058"},{"currency":"ACM","price":"0.02835716"}]
request http kütüphanesidir siteye istek atmamızı sağlar
get,post sunucuyla iletişime geçme yöntemleridir
get : veriyi alıp işleyceksek -genelde- veri alırken 
post : veri tabanında değişiklik yapılacaksa,backende bilgi gönderilecekse, büyük veriyi sunucuya yollamak için -genelde-, veri yazarken kullanılır
delete : silmek içins
put,patch : veriyi güncellemek için 
"""
"""
http kodes
2xx success
200 ok
3xx rediction url'ye istek atıldığında başka yere  yönlendirir
4xx client errors tarayıcı,mobil uygulama vs. sunucuya istek atan taraftan kaynaklı hata
401 unauthorized yetkiniz yoktur
402 payment required girmek için ödeme yapmalısınız
5xx server errors sunucu hatası
"""
#https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json :: istek attığımız site

import requests

"""
    for crypto in response.json():
        print(crypto["currency"]) #kripto paradaki isimleri yazdırır
"""

def get_crypto_data():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    print(response)
    print(response.status_code) #direkt 200ü yazdırabiliriz
    if response.status_code == 200:
        print("succes")
        #print(response.text) #metin olarak veriyi yazdırır
        #print(response.json()) #json formatına çevrilir sözlük gibi davranır

        """
            for crypto in response.json():
                print(crypto["currency"]) #kripto paradaki isimleri yazdırır
        """
        return response.json()

crypt_response = get_crypto_data()
x=0
user_input = input("Enter your crypto currency: ")
for crypto in crypt_response:
    x += 1
    print(x)
    if crypto["currency"] == user_input:
        print(crypto["price"])
    break
