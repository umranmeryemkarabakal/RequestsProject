#https://jsonplaceholder.typicode.com/

import requests
import json

"""
#get
user_input = input("enter id: ")
url = f"https://jsonplaceholder.typicode.com/todos/{user_input}"
get_response = requests.get(get_url)
print(get_response.json())
"""

#post yeni bir to do eklemek istiyor isem
to_do_item = {"userId":2,"title":"my to do","completed":False}
post_url = "https://jsonplaceholder.typicode.com/todos"
#optional_header
headers = {"Content-Type": "application/json"}
#post_response = requests.post(post_url,json=to_do_item,headers=headers)
#print(post_response.json())
post_response = requests.post(post_url,data=json.dumps(to_do_item),headers=headers)
print(json.dumps(to_do_item)) # json döndürür
print(post_response.json())

"""
http header
ekstra bir bilgi yollamak için
responsa header : date,age,server tipi apache ,backend sunucusunun adı,id vs.
reques header : nereden geldiği get  /home.http/1.0,content tye json,text,html
"""

