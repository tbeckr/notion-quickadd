import tkinter as tk
import json
from tkinter import ttk
from notion_client import Client
import os

NOTION_TOKEN = os.environ['NOTION_TOKEN'] 
DATABASE_ID = os.environ['NOTION_DB_ID']
notion = Client(auth=NOTION_TOKEN)


def setup_gui(gui: tk.Tk):
    gui.title("Notion - Nota rápida")
    setup_window_size(gui)
    set_icon(gui)

    input = tk.StringVar()

    def save(args=None):
        add_task(input.get())
        input.set("")

    textbox = ttk.Entry(gui, textvariable=input)
    textbox.pack(expand=False, fill="x", padx=10)
    textbox.bind("<Return>", save)
    textbox.focus()

    btn_save = ttk.Button(text="Salvar", command=save)
    btn_save.pack(side=tk.RIGHT, padx=10)

    btn_cancel = ttk.Button(text="Cancelar", command=exit)
    btn_cancel.pack(side=tk.RIGHT, padx=0)


def set_icon(gui):
    gui.iconbitmap("icon.ico")


def setup_window_size(gui):
    width = 300
    height = 70
    screen_width = gui.winfo_screenwidth()
    screen_height = gui.winfo_screenheight()
    center_x = int(screen_width / 2 - width / 2)
    center_y = int(screen_height / 2 - height / 2)

    gui.geometry(f"{width}x{height}+{center_x}+{center_y}")


def add_task(task):
    if task == "":
        exit()

    result = notion.pages.create(
       **{
            "parent": {
                "database_id": DATABASE_ID,
            },
            "icon": {
                "type": "emoji",
                "emoji": "✅"
            },
            "properties": {
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": task,
                            },
                        },
                    ],
                }
            },
        }
    )
    print(json.dumps(result))
    exit()


def main():
    root = tk.Tk()
    setup_gui(root)

    root.mainloop()


if __name__ == "__main__":
    main()
