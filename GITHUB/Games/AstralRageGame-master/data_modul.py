import json
import random
import threading
import simpleaudio as sa


class JsonConnector(object):

    @classmethod
    def get_from_config(cls, key):
        file = open("data/config.json", "r")
        content = file.read()
        content = json.loads(content)
        file.close()
        return content[key]

    @classmethod
    def save_key_to_config(cls, key, value):
        file = open("data/config.json", "r")
        content = file.read()
        content = json.loads(content)
        file.close()

        content[key] = value

        content = json.dumps(content)
        scores_file = open("data/config.json", "w")
        scores_file.write(content)
        scores_file.close()

    @staticmethod
    def get_skin_list():
        file = open("data/skinStatus.json", "r")
        content = file.read()
        content = json.loads(content)
        file.close()
        return content["skins"]

    @staticmethod
    def save_skin_list(skin_list):
        skin_list = {"skins": skin_list}
        skin_list = json.dumps(skin_list)
        scores_file = open("data/skinStatus.json", "w")
        scores_file.write(skin_list)
        scores_file.close()

    @staticmethod
    def get_skills_dict():
        file = open("data/skillsStatus.json", "r")
        content = file.read()
        content = json.loads(content)
        file.close()
        return content

    @staticmethod
    def save_skills_dict(skills_list):
        skills_list = json.dumps(skills_list)
        scores_file = open("data/skillsStatus.json", "w")
        scores_file.write(skills_list)
        scores_file.close()


class Chest(object):
    @staticmethod
    def open(score):
        if score <= 1:
            score = 100
        coins = JsonConnector.get_from_config("coins")
        random_ = random.randint(int(score/200), score/100)
        coins += random_
        JsonConnector.save_key_to_config("coins", coins)
        return random_


class SoundThread(threading.Thread):
    def __init__(self, address, loop=False, **kwargs):
        threading.Thread.__init__(self, **kwargs)
        self.address = "sounds/" + address
        self.loop = loop

    def run(self):
        wave_obj = sa.WaveObject.from_wave_file(self.address)
        self.play_obj = wave_obj.play()
        self.play_obj.wait_done()
        while self.loop:
            self.play_obj = wave_obj.play()
            self.play_obj.wait_done()

    def stop(self):
        self.loop = False
        self.play_obj.stop()
