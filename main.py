from tkinter import *

win = Tk()
win.geometry("600x500+100+50")
win.title("n4c's multitool")
win.resizable(False, False)
win.minsize(600, 500)
win.maxsize(600, 500)
    
def changedownloader():
    exec(open('downloader.py').read)
    quit()



win.mainloop()