from requests import get, post
from os import system, listdir
from time import sleep
from json import loads

config = loads(s=open('config.json', 'r').read())

ecid = config['device']['ecid']
identifier = config['device']['identifier']
bot_token = config['telegram']['bot_token']  # Telegram Bot Token
chat_id = config['telegram']['chat_id']  # As string
path = config['storage_path']
disable_notification = config['telegram']['disable_notification']

while True:
    response = get(url=f'https://api.ipsw.me/v4/device/{identifier}?type=ipsw').json()
    for firmware in response['firmwares']:
        version = firmware['version']
        signed = firmware['signed']
        build_id = firmware['buildid']
        is_saved = version + '-' + build_id in [file.split('_')[2] for file in listdir(path=path)]

        if not signed or is_saved:
            print(f'Skipping version {version}... ({signed}, {is_saved})')
            continue

        system(f'./tsschecker -e {ecid} -d {identifier} -i {version} -s --save-path {path}')

        response = post(url=f'https://api.telegram.org/bot{bot_token}/sendDocument', data={
            'chat_id': chat_id,
            'caption': f'Blobs for iOS {version}',
            'parse_mode': 'Markdown',
            'disable_notification': disable_notification
        }, files={'document': open(file=path + listdir(path=path)[0], mode='rb')})

    sleep(900)
