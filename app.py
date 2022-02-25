import random, time, os, sys, json
from tkinter import *

class App:

    player = json.load(open("player.json", 'w'))

    def __init__(self, player, app):
        self.player = []
        for x in player:
            self.player.append(x)
        if self.player.name == "":
            self.player.name = "Guest"
        self.app = Tk()
        self.app.geometry = [800,600]
        self.app.resizable = [False, False]
    