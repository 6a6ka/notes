from tkinter import *
import sys
 
WIN = True if sys.platform[:3] == "win" else False
 
class Note(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.wm_title("notes")
        self.minsize(210,100)
        self.maxsize(300,350)
        self.attributes("-topmost", 1)
        if WIN: self.attributes("-toolwindow", 1)
        self.geometry('210x230+%d+%d' % (self.winfo_screenwidth()/2, self.winfo_screenheight()/2)) #position in middle of screen
        self.textbox()
 
    def textbox(self):
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        text = Text(self, wrap=WORD, yscrollcommand=scrollbar.set)
        text.pack()
        scrollbar.config(command=text.yview)
 
 
if __name__ == "__main__":
    window = Note()
    window.mainloop()
