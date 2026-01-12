import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0IiwiZXhwIjoxNzY4Nzc5OTY1fQ.mULCmQzcEvnvlixgTQp5GiE2MjFGnvIDiCV-v_SI8gI"
}

resul = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)

print(resul)
print(resul.json())