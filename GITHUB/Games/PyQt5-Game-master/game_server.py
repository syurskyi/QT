# this code wroted by: Omar Othman
# 2018.06.08 - 11:32 PM

from modules.service.service import WebsocketServer
from modules.json import Json
from threading import Thread
import logging
from colorlog import ColoredFormatter
import os
import sys
import traceback
import random
from callback.levels import Levels
LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "%(log_color)s%(message)s%(reset)s"
logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOG_FORMAT)
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
log = logging.getLogger()
log.setLevel(LOG_LEVEL)
if log.hasHandlers():
    log.handlers.clear()
log.addHandler(stream)
os.chdir(os.path.dirname(__file__))
_GAMES = {}

def client_left(client, server):
    msg = "Client (%s) left" % str(client['id'])
    if client["id"] in _GAMES:
        del _GAMES[client["id"]]
    log.info(msg)


def new_client(client, server):
    msg = "New client (%s) connected" % client['id']
    log.info(msg)
    _GAMES[client["id"]] = {"c": client, "level": -1, "sec": -1}

def msg_received(client, server, packet):
    try:
        packet = eval(packet)
    except NameError:
        log.warning("can't eval packet! error from client!")
        return
    json = Json()
    json.set_json(packet)
    clicked = json.get("space")
    if clicked:
        _GAMES[client["id"]]["sec"] = _GAMES[client["id"]]["sec"] + 1
    n1 = _GAMES[client["id"]]["level"]
    n2 = _GAMES[client["id"]]["sec"]
    _id = client["id"]
    l = Levels()
    if _id in _GAMES:
        l = Levels()
        f, s = l.get_next_level(n1, n2)
        if f == -1 and s == -1:
            server.send_message(client, str({"type": "success", "space": "end"}))
        else:
            server.send_message(client, l.get_Q_as_json(f, s))
    if _GAMES[client["id"]]["level"] == -1:
            _GAMES[client["id"]]["level"] = 0
    if _GAMES[client["id"]]["sec"] == -1:
            _GAMES[client["id"]]["sec"] = 0


server = WebsocketServer(80)
log.info("start service on port: 80")
log.info("----------------------------------")
log.warning("Game server has been started!")
log.warning("""

Welcome To Game service

""")
log.warning("This server wroted by: Omar Othman")
log.info("----------------------------------")
server.set_fn_client_left(client_left)
server.set_fn_new_client(new_client)
server.set_fn_message_received(msg_received)
server.run_forever()
