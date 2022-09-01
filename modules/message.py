import tkinter as tk

class Message():
    def __init__(self, window, text):  
        self.frame = tk.Frame(window, bg='#472836', bd=3) # grid
        self.text = text
        if self.text == "RANKEDMATCH...":
            self.show_rankedmatch_message()
        else:
            self.show_win_message()

    def show_win_message(self):
        title_label = tk.Label(self.frame,text=self.text,bg='#472836',fg = "#F2E3D5", font=("Helvetica", 20, "bold"))
        title_label.pack(pady=(25,25))
        self.frame.pack(fill="x")
        self.window.after(300, self.window.withdraw())

    def show_rankedmatch_message(self):
        title_label = tk.Label(self.frame,text=self.text,bg='#472836',fg = "#F2E3D5", font=("Helvetica", 20, "bold"))
        title_label.pack()


      