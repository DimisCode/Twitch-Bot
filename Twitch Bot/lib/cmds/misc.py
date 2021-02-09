import subprocess
import sys

def help(bot, prefix, cmds):
    bot.send_message("Registered commands: " + ", ".join([f"{prefix}{cmd}" for cmd in cmds.keys()]))

def hello(bot, user, *args):
    bot.send_message(f"Hey {user['name']}!")

def test(bot, user, *args):
    bot.send_message(f"Test!")

def overlay(bot, user, *args):
    subprocess.call([sys.executable, "C:\\Users\\Kas\\Desktop\\Programming Projects\\League overlay\\Overlay\\OverlayRUN.py"])