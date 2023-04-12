import requests
response = requests.get('https://www.economist.com/')
response.cookies


# i wanted to understand how cookies work and whats in them, but 
# only the website internally can understand the string responses
# and what they mean...but still interesting. 

for cookie in response.cookies:

  print("cookie domain = " + cookie.domain)

  print("cookie name = " + cookie.name)

  print("cookie value = " + cookie.value)

  print("*************************************")

print(response.cookies)