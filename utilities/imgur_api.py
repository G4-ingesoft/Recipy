from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError, ImgurClientRateLimitError
from os import path
from Recipy.settings import MEDIA_ROOT

# access_token = '42699650d1536571f008da028ed41dff484deaf2'
# refresh_token = '0b1ee9f95c02f9372e8236b04f0aa78e9cc7a05c'
#client = ImgurClient(client_id, client_secret, access_token, refresh_token)

##UploadImage retorna el ID
def upload_image_imgur(image): 
    client_id = '921f4adb2a271b1'
    client_secret = 'a6387bb7caa543354d5a464692b1d0bb37473de4'
    client = ImgurClient(client_id, client_secret)
    #ruta_abs = path.abspath(image)
    ruta_abs = MEDIA_ROOT.join("/"+image)
    print("IMPRIMIENDOOOOO")
    print(ruta_abs)
    print(image)
    print("THNX")
    try:
        image_link = client.upload_from_path(ruta_abs, config=None, anon=False)['link']
        return image_link
    except ImgurClientError as e:
        print(e.error_message)
        print(e.status_code)
    except ImgurClientRateLimitError as e:
        print(e)

##GetImage obtiene la imagen
"""
def get_image_imgur(image_id):
    client_id = '921f4adb2a271b1'
    client_secret = 'a6387bb7caa543354d5a464692b1d0bb37473de4'
    client = ImgurClient(client_id, client_secret)
    try:
        image = client.get_image(image_id)
        return image
    except ImgurClientError as e:
        print(e.error_message)
        print(e.status_code)
    except ImgurClientRateLimitError as e:
        print(e)
"""