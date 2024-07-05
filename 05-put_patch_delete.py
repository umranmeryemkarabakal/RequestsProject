import requests

get_url = "https://jsonplaceholder.typicode.com/todos/15"
get_response = requests.get(get_url)
print(get_response.json())

#güncelleme

#put
#komple baştan değiştirirken
to_do_item_15_put = {'userId': 2, 'id': 15, 'title': 'put title', 'completed': False}
put_response = requests.put(get_url, json=to_do_item_15_put) #gerçekten değiştirmez miş gibi yapıyor
print(put_response.json())

#patch
#bir tanesini değiştirirken
to_do_item_15_patch = {"title": "patch title"}
patch_response = requests.patch(get_url,json=to_do_item_15_patch)
print(patch_response.json())

#delete
delete_response = requests.delete(get_url)
print(delete_response.json())
print(delete_response.status_code)