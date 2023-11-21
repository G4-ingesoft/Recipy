from imgurpython import ImgurClient
from os import path

client_id = '921f4adb2a271b1'
client_secret = 'a6387bb7caa543354d5a464692b1d0bb37473de4'

client = ImgurClient(client_id, client_secret)
##
# If you already have an access/refresh pair in hand
access_token = '42699650d1536571f008da028ed41dff484deaf2'
refresh_token = '0b1ee9f95c02f9372e8236b04f0aa78e9cc7a05c'

# Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)
client = ImgurClient(client_id, client_secret, access_token, refresh_token)
##
ruta = 'imagen.jpg'
ruta_abs = path.abspath(ruta)
print(ruta_abs)

var = client.upload_from_path(ruta_abs, config=None, anon=False)
print(var['link'])