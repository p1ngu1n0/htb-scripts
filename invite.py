import requests; import base64; print("Codigo de invitacion es: ", base64.b64decode(requests.post("https://www.hackthebox.eu/api/invite/generate",  headers={'User-Agent': 'Custom'}).json()["data"]["code"]).decode())