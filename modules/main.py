import tkinter as tk
from home import create_home_window 
from game import one_vs_one
from message import Message

class Main(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        create_home_window(master, self.create_game_window)

    def exit(self):
        self.master.destroy()
        self.master.quit() 

    def create_game_window(self):

        self.master.withdraw()

        game_window = tk.Toplevel()
        game_window.title('TIC TAC TOE GAME')
        game_window.geometry("575x400+400+150")
        game_window.rowconfigure(0, weight=1)
        game_window.columnconfigure(1, weight=1)
        game_window.protocol("WM_DELETE_WINDOW", self.exit) # Finalizar la ejecución al presionar la X
        game_window.configure(bg='#472836')

        one_vs_one(game_window, self.create_message_window)
    
    def create_message_window(self, text):
        message_window = tk.Toplevel()
        message_window.geometry("575x100+410+375")
        message_window.rowconfigure(0, weight=1)
        message_window.columnconfigure(1, weight=1)
        message_window.configure(bg='#472836')
        #message_window.overrideredirect(True)
        message_window = Message(message_window, text)
        #msg_window_func(message_window)
        
        #message_window.after(3000, message_window.withdraw())
                
          
if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("300x300+500+150")
    window.configure(bg='#472836')
    main = Main(window)
    main.mainloop()