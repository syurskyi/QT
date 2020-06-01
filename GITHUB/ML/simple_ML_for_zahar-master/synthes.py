import requests


def synthes(filename, key, syth_text):
    url = 'https://tts.voicetech.yandex.net/generate?text={}&format=wav&lang=ru-RU&' \
          'speaker=zahar&key={}&speed=1&emotion=good'.format(syth_text, key)
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
