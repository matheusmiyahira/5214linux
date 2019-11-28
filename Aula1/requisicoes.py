#!/usr/bin/env python3

import requests as r
import json

url_api = 'http://gen-net.herokuapp.com/api/users'
# realizando requisições com o modulo request
res = r.get(url_api)
# print(res.json())

dados = {
    "name":"jubile",
    "email":"xabla1@4linux.com",
    "password":"senhaSegura"
}

# res = r.post(url_api,json=dados)
# print(res.json())

res = r.get('http://gen-net.herokuapp.com/api/users?{}={}'.format('name','jubileu'))
# print(res.json())

res = r.put(url_api + '/272',json=dados)
print(res.json())