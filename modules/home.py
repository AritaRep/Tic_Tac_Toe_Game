import tkinter as tk
from PIL import Image, ImageTk


def create_home_window(form_frame, game_window):

    #Labels
    frame = tk.Frame(form_frame, bg='#472836', bd=3) # grid
    title_label = tk.Label(frame,text="TIC TAC TOE",bg='#472836',fg = "#F2E3D5", font=("Helvetica", 20, "bold"))
    

    # Buttons
    one_vs_one_btn = tk.Button(frame, text="START", 
                    command= lambda: one_vs_one(game_window), 
                    bg='#DEFFFC', 
                    font=("Helvetica", 10, "bold"),
                    fg="#242325"
    )

    image_frame = tk.Frame(frame, relief=tk.GROOVE, bd=3) # pack
    
    global new_image
    image_game = Image.open(r'icons\game.ico')
    image_game = image_game.resize((100,100))
    new_image = ImageTk.PhotoImage(image_game)
    image_label = tk.Label(image_frame, image=new_image)

    image_label.pack()

    image_frame.grid(row=0, columnspan=3, pady=(30,0))
    title_label.grid(row=1, columnspan=3, pady=(30,10), padx=(60,60))
    one_vs_one_btn.grid(row=3, column=1, pady=(10,35), sticky="we")

    
    """     
    help_btn = tk.Button(master, text="?", 
                   # command= instrucciones, 
                    bg='#53736A', 
                    font=("Helvetica", 10, "bold"),
                    fg="#F2E3D5"
    )
    help_btn.grid(row=3, column=2, pady=(20,10))
    """
     # Icono
    form_frame.iconbitmap(r'icons\game.ico')

    
    frame.pack(fill="y")
    
 
def one_vs_one(game_window):
    game_window()
        
    
        