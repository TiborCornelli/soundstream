from tkinter import *
from downloader import download

root = Tk()

title = Label(root, text="This app converts youtube videos into local MP3 files" ).grid(row=0,column=1)

# Insert URL here
url_label = Label(root, text="Enter the video URL here: ")
url_input = Entry(root, width=35)

url_label.grid(row=1,column=0)
url_input.grid(row=1,column=1)

# Insert destination path here
path_label = Label(root, text="Where do you want to store the mp3 file?")
path_input = Entry(root, width=35)

path_label.grid(row=2, column=0)
path_input.grid(row=2, column=1)

# Function to pass URL and path to the download function
# download() is imported from the downloader.py
# URL input is cleared after clicking the button
def call_downloader():
    URL = url_input.get()
    PATH = path_input.get()
    url_input.delete(0,"end")
    download(URL, PATH)

# Button to submit url and path
button = Button(root, text="Confirm", command=call_downloader)
button.grid(row=3, column=1)

root.mainloop() 