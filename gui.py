from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from downloader import download

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Variables
        self.PATH: str

        # Insert destination path here
        self.path_label = Label(self, text="Choose location for the file")
        self.path_input = Button(self, text="Choose location", command=self.select_path)
        self.path_input["width"] = 30
        self.path_label.grid(row=0, column=0)
        self.path_input.grid(row=0, column=1)

        # Insert URL here
        self.url_label = Label(self, text="Enter the video URL: ")
        self.url_input = Entry(self)
        self.url_input["width"] = 35
        self.url_label.grid(row=1,column=0)
        self.url_input.grid(row=1,column=1)

        # button to submit url
        self.button = Button(self, text="Download", command=self.call_downloader)
        self.button.grid(row=1, column=2)

        # Warning label
        self.warning = Label(self, fg="red", text="Location or URL are invalid")
    
    def set_path(self, path: str) -> None:
        self.PATH: str = path

    def select_path(self) -> None: # Users can select the location
        folder_selected: str = filedialog.askdirectory()
        self.set_path(folder_selected)
        self.path_input["text"] = folder_selected # Button shows the currently chosen path

    def call_downloader(self) -> None:
        try:
            url = self.url_input.get()
            path = self.PATH
            self.url_input.delete(0,"end") # url input is cleared after clicking the button
            download(url, path) # download() is imported from the downloader.py
            self.warning.grid_forget() # Hides warning if no problems occur
        except:
            self.warning.grid(row=2, column=1)
            

app = App().mainloop()