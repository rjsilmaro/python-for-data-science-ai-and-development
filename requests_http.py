import requests
import os
from PIL import Image
from IPython.display import IFrame

#url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'
#r=requests.get(url)

#path=os.path.join(os.getcwd(),'image.png')
#path

#with open(path,'wb') as f:
 #   f.write(r.content)

#Image.open(path)

url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)
r.url

url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)
print("POST request URL:",r_post.url )
print("GET request URL:",r.url)

print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

r_post.json()['form']