'''
Created on 2017年3月9日

@author: wujianxin
'''
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.hi_there = tk.Button(self, fg='orange', bg='blue')
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.req = tk.Button(self, fg='orange', bg='blue')
        self.req["text"] = "Send\n(click me)"
        self.req["command"] = self.request
        self.req.pack(side="left")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def request(self):
        print("to send a request")


root = tk.Tk()

app = Application(master=root)
app.master.maxsize(800, 600)
app.mainloop()
