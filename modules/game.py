import tkinter as tk

turn_count = 0
position_dict = {'X':[], 'O':[]}
combination_dict = {'0':([0,1,2],[0,3,6],[0,4,8]), '1':[1,4,7], '2':([2,4,6],[2,5,8]), '3':(3,4,5), '6':[6,7,8]}
buttons_list = []
victories = {'X': 0, 'O': 0}

def one_vs_one(game_window, message_window_func):

    game_frame = tk.Frame(game_window,  bg='#472836', relief=tk.GROOVE, bd=3, height='200') # grid

    title_label = tk.Label(game_frame,text="TIC TAC TOE",bg='#472836',fg = "#F2E3D5", font=("Helvetica", 20, "bold"))
    j1_label = tk.Label(game_frame,text="PLAYER 1 ",bg='#472836',fg = "#F2E3D5", font=("Helvetica", 14, "bold"))
    j2_label = tk.Label(game_frame,text="PLAYER 2 ",bg='#472836',fg = "#F2E3D5", font=("Helvetica", 14, "bold"))
    j1_count_label = tk.Label(game_frame,text="0",bg='#96C5F7',fg = "#242325", font=("Helvetica", 20, "bold"))
    j2_count_label = tk.Label(game_frame,text="0",bg='#BCB6FF',fg = "#242325", font=("Helvetica", 20, "bold"))

    buttons_frame = tk.Frame(game_window,  bg='#024554', relief=tk.GROOVE, bd=3, height='200') # grid

    # Buttons
    position_00_btn = tk.Button(buttons_frame, text=" ", state='normal',
                    command= lambda: player_turn(turn_count, 0, position_00_btn, j1_count_label, j2_count_label, message_window_func), 
                    bg='#C0BDA5', 
                    font=("Helvetica", 20, "bold"),
                    fg="#F2E3D5"
    )

    position_01_btn = tk.Button(buttons_frame, text=" ", state='normal',
                    command= lambda: player_turn(turn_count, 1, position_01_btn, j1_count_label, j2_count_label, message_window_func), 
                    bg='#C0BDA5', 
                    font=("Helvetica", 20, "bold"),
                    fg="#F2E3D5"
    )

    position_02_btn = tk.Button(buttons_frame, text=" ", state='normal',
                    command= lambda: player_turn(turn_count, 2, position_02_btn, j1_count_label, j2_count_label, message_window_func), 
                    bg='#C0BDA5', 
                    font=("Helvetica", 20, "bold"),
                    fg="#F2E3D5"
    )
    
    position_10_btn = tk.Button(buttons_frame, text=" ", state='normal',
                    command= lambda: player_turn(turn_count, 3, position_10_btn, j1_count_label, j2_count_label, message_window_func), 
                    bg='#C0BDA5', 
                    font=("Helvetica", 20, "bold"),
                    fg="#F2E3D5"
    )

    position_11_btn = tk.Button(buttons_frame, text=" ", state='normal',
                    command= lambda: player_turn(turn_count, 4, position_11_btn, j1_count_label, j2_count_label, message_window_func), 
                    bg='#C0BDA5', 
                    font=("Helvetica", 20, "bold"),
                    fg="#F2E3D5"
    )

    position_12_btn = tk.Button(buttons_frame, text=" ", state='normal',
                    command= lambda: player_turn(turn_count, 5, position_12_btn, j1_count_label, j2_count_label, message_window_func), 
                    bg='#C0BDA5', 
                    font=("Helvetica", 20, "bold"),
                    fg="#F2E3D5"
    )

    position_20_btn = tk.Button(buttons_frame, text=" ", state='normal',
                    command= lambda: player_turn(turn_count, 6, position_20_btn, j1_count_label, j2_count_label, message_window_func), 
                    bg='#C0BDA5', 
                    font=("Helvetica", 20, "bold"),
                    fg="#F2E3D5"
    )

    position_21_btn = tk.Button(buttons_frame, text=" ", state='normal',
                    command= lambda: player_turn(turn_count, 7, position_21_btn, j1_count_label, j2_count_label, message_window_func), 
                    bg='#C0BDA5', 
                    font=("Helvetica", 20, "bold"),
                    fg="#F2E3D5"
    )

    position_22_btn = tk.Button(buttons_frame, text=" ", state='normal',
                    command= lambda: player_turn(turn_count, 8, position_22_btn, j1_count_label, j2_count_label, message_window_func), 
                    bg='#C0BDA5', 
                    font=("Helvetica", 20, "bold"),
                    fg="#F2E3D5"
    )

    title_label.grid(row=0, columnspan=4, pady=(30,0), padx=(200,200))
    j1_label.grid(row=1, column=0, pady=(10,10), padx=(70,0))
    j1_count_label.grid(row=1, column=1, pady=(10,10), padx=(0,30))
    j2_count_label.grid(row=1, column=2, pady=(10,10), padx=(0,0))
    j2_label.grid(row=1, column=3, pady=(10,10), padx=(0,70))

    position_00_btn.grid(row=0,column=0, ipadx=(75), ipady=(16), sticky="we")
    position_01_btn.grid(row=0,column=1, ipadx=(75), ipady=(16), sticky="we")
    position_02_btn.grid(row=0,column=2, ipadx=(75), ipady=(16), sticky="we")
    position_10_btn.grid(row=1,column=0, ipadx=(75), ipady=(16), sticky="we")
    position_11_btn.grid(row=1,column=1, ipadx=(75), ipady=(16), sticky="we")
    position_12_btn.grid(row=1,column=2, ipadx=(75), ipady=(16), sticky="we")
    position_20_btn.grid(row=2,column=0, ipadx=(75), ipady=(16), sticky="we")
    position_21_btn.grid(row=2,column=1, ipadx=(75), ipady=(16), sticky="we")
    position_22_btn.grid(row=2,column=2, ipadx=(75), ipady=(16), sticky="we")

    game_frame.pack(fill="x")
    buttons_frame.pack(fill="y")
   

def player_turn(turn, position, button, j1, j2, message_window_func):
    global turn_count
    turn_count = turn + 1
    
    if position == 0:
        simbol, color = even_or_odd(turn_count, position)
        button.configure(text=simbol, state='disabled', bg=color)
        check_combination(turn_count, simbol, button, j1, j2, message_window_func)       
        print(simbol)
    elif position == 1:
        simbol, color = even_or_odd(turn_count, position)
        button.configure(text=simbol, state='disabled', bg=color)
        check_combination(turn_count, simbol, button, j1, j2, message_window_func)
        print(simbol)
    elif position == 2:
        simbol, color = even_or_odd(turn_count, position)
        button.configure(text=simbol, state='disabled', bg=color)
        check_combination(turn_count, simbol, button, j1, j2, message_window_func)
        print(simbol)
    elif position == 3:
        simbol, color = even_or_odd(turn_count, position)
        button.configure(text=simbol, state='disabled', bg=color)
        check_combination(turn_count, simbol, button, j1, j2, message_window_func)
        print(simbol)
    elif position == 4:
        simbol, color = even_or_odd(turn_count, position)
        button.configure(text=simbol, state='disabled', bg=color)
        check_combination(turn_count, simbol, button, j1, j2, message_window_func)
        print(simbol)
    elif position == 5:
        simbol, color = even_or_odd(turn_count, position)
        button.configure(text=simbol, state='disabled', bg=color)
        check_combination(turn_count, simbol, button, j1, j2, message_window_func)
        print(simbol)
    elif position == 6:
        simbol, color = even_or_odd(turn_count, position)
        button.configure(text=simbol, state='disabled', bg=color)
        check_combination(turn_count, simbol, button, j1, j2, message_window_func)
        print(simbol)
    elif position == 7:
        simbol, color = even_or_odd(turn_count, position)
        button.configure(text=simbol, state='disabled', bg=color)
        check_combination(turn_count, simbol, button, j1, j2, message_window_func)
        print(simbol)
    elif position == 8:
        simbol, color = even_or_odd(turn_count, position)
        button.configure(text=simbol, state='disabled', bg=color)
        check_combination(turn_count, simbol, button, j1, j2, message_window_func)
        print(simbol)

def even_or_odd(turn_count, position):
    if turn_count%2 == 0:
        position_dict["O"].append(position)
        position_dict["O"].sort()
        print(position_dict)
        return "O", "#BCB6FF"
    else:
        position_dict["X"].append(position)
        position_dict["X"].sort()
        print(position_dict)
        return "X", "#96C5F7"

def check_combination(turn_count, simbol, button, j1, j2, message_window_func):
    buttons_list.append(button)
    if turn_count>= 5:
        print("turno: ", turn_count)
        if 0 in position_dict[simbol]:
            print("aqui 0")
            for combination in combination_dict["0"]:
                if combination[0] in position_dict[simbol] and combination[1] in position_dict[simbol] and combination[2] in position_dict[simbol]:
                    print("SI")
                    victories[simbol] = victories[simbol] + 1
                    j1.configure(text=victories["X"])
                    j2.configure(text=victories["O"])
                    clean_game()
                    show_message(message_window_func)      
        if 1 in position_dict[simbol]:
            print("aqui 1")
            if combination_dict["1"][0] in position_dict[simbol] and combination_dict["1"][1] in position_dict[simbol] and combination_dict["1"][2] in position_dict[simbol]:
                victories[simbol] = victories[simbol] + 1
                j1.configure(text=victories["X"])
                j2.configure(text=victories["O"])
                show_message(message_window_func)
                clean_game()
        if 2 in position_dict[simbol]:
            print("aqui 2")
            for combination in combination_dict["2"]:
                if combination[0] in position_dict[simbol] and combination[1] in position_dict[simbol] and combination[2] in position_dict[simbol]:
                    victories[simbol] = victories[simbol] + 1
                    j1.configure(text=victories["X"])
                    j2.configure(text=victories["O"])
                    show_message(message_window_func)
                    clean_game()
        if 3 in position_dict[simbol]:
            print("aqui 3")
            if combination_dict["3"][0] in position_dict[simbol] and combination_dict["3"][1] in position_dict[simbol] and combination_dict["3"][2] in position_dict[simbol]:
                victories[simbol] = victories[simbol] + 1
                j1.configure(text=victories["X"])
                j2.configure(text=victories["O"])
                show_message(message_window_func)
                clean_game()
        if 6 in position_dict[simbol]:
            print("aqui 6")
            if combination_dict["6"][0] in position_dict[simbol] and combination_dict["6"][1] in position_dict[simbol] and combination_dict["6"][2] in position_dict[simbol]:
                victories[simbol] = victories[simbol] + 1
                j1.configure(text=victories["X"])
                j2.configure(text=victories["O"])
                show_message(message_window_func)
                clean_game()
        if turn_count == 9:
            clean_game()

def show_message(message_window_func):
    if victories["X"] > victories["O"]:
        message_window_func("YOU WIN PLAYER 1")
    elif victories["O"] > victories["X"]:
        message_window_func("YOU WIN PLAYER 2")
    elif victories["O"] == victories["X"]:
        message_window_func("RANKEDMATCH")

def clean_game():
    global turn_count, position_dict, buttons_list
    turn_count = 0
    position_dict = {'X':[], 'O':[]}
    for button in buttons_list:
        button.configure(text=" ", state="normal", bg='#C0BDA5')
    buttons_list = []

