import xml.etree.ElementTree as XmlElementTree
import os
import requests


def decode_synthes(filename, key, uuid_num, topic, codecs):
    url = 'https://asr.yandex.net/asr_xml?uuid={}&key={}&topic={}&lang=ru-RU'.format(uuid_num, key, topic)
    data = open(filename, mode="rb").read()
    headers = {"Content-Length": os.path.getsize(filename), "Content-Type": codecs[filename[filename.rfind("."):]]}
    response = requests.post(data=data, headers=headers, url=url)
    if response.status_code == 200:
        res = response.content.decode()
        xml = XmlElementTree.fromstring(res)
        return [child.text for child in xml]
