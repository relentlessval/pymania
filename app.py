import random, time, os, sys, json
from tkinter import *

app = Tk()
app.geometry = [800,600]
app.resizable = [False, False]
app.winfo_name = "pymania"

def dump(dumpfile):
    json.dumps(dumpfile)

playerfile = json.load(open("player.json", 'w'))

if playerfile.name == "":

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
    playerfile.lang = lang
    dump(playerfile)
    if lang = "English":
        playerfile.name = input("What's your name? (default: Guest) ")
        dump(playerfile)
    elif lang = "日本語":
        playerfile.name = input("あなたの名前は何ですか？　(デフォルト: Guest) ")
        dump(playerfile)
    elif lang = "Español":
        playerfile.name = input("Como te llamas? (nombre predeterminado: Guest) ")
        dump(playerfile)
    