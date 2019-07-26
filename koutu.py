from removebg import RemoveBg
import requests
import os
if __name__ == '__main__':
    path = '%s\picture'%os.getcwd()
    ispath = os.path.exists(path)
    if not ispath:
        os.mkdir(path)
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(path+'/juqiamyi.jpg', 'rb')},
        # data={'size': 'auto','bg_color':'FFB6C1'},
        data={'size': 'auto'},
        headers={'X-Api-Key': '****YOU API KEY****'},
    )
    if response.status_code == requests.codes.ok:
        with open(path+'/juqiamyi.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)