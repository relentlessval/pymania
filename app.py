import random, time, os, sys, json
from tkinter import *

app = Tk()
app.geometry = [800,600]
app.resizable = [False, False]
app.winfo_name = "pymania"

playerfile = json.load(open("player.json", 'w'))
player = []
for x in playerfile:
    player.append(x)

if player.name == "":

    OPTIONS = [
        "English",
        "日本語",
        "Español"
    ] #etc


    lang_select = StringVar(app)
    lang_select.set(OPTIONS[0]) # default value

    w = OptionMenu(master, lang_select, *OPTIONS)
    w.pack()

    lang = lang_select.get()
    if lang = "English":
        player.name = input("What's your name? (default: Guest) ")
    elif lang = "日本語":
        player.name = input("あなたの名前は何ですか？　(デフォルト:Guest) ")
    elif lang = "Español":
        player.name = input("Como te llamas?    ")