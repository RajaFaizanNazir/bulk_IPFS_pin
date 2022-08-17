from tkinter import *
from tkinter import ttk
import json


def update_env(path, key):
    json_read = open("constants/env.json", "r")
    env = json.loads(json_read.read())
    json_read.close()
    env["X-API-Key"] = key
    env["parentFolder"] = path
    json_write = open("constants/env.json", "w")
    json_write.write(json.dumps(env))
    json_write.close()


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="").grid(column=1, row=0)
ttk.Label(frm, text="Change constants! ").grid(column=1, row=0)
ttk.Label(frm, text="Enter absolute path of data folder! ").grid(column=0, row=1)
ttk.Entry(frm).grid(column=1, row=1)
ttk.Label(frm, text="Enter X-API-Key of Moralis! ").grid(column=0, row=2)
ttk.Entry(frm).grid(column=1, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=3)
ttk.Button(frm, text="Save", command=update_env(path="", key="")).grid(column=0, row=3)
root.mainloop()
