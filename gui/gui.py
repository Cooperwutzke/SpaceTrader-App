# Cooper Wutzke
# Custom GUI for Spacetraders.io

from tkinter import Tk, ttk
from tkinter import StringVar
from game import gamelogin, newagent, get_factions

def newagent_dialog():
    dialog = Tk()
    dialog.title('New Agent')
    dialog.geometry("200x200")
    dialog.columnconfigure(0, weight=1)
    dialog.rowconfigure(0, weight=1)

    callsign_label = ttk.Label(dialog, text='Callsign')
    callsign_label.grid(row=1, column=1)
    callsign = StringVar() 
    callsign_entry = ttk.Entry(dialog, width=15, textvariable=callsign)
    callsign_entry.grid(row=1, column=2)

    faction = StringVar()
    faction_list = get_factions(True)
    print(faction_list)
    faction_choice = ttk.OptionMenu(dialog, faction, faction_list)
    faction_choice.grid(row=1, column=3, padx=10)


root = Tk()
root.title("SpaceTraders")
root.geometry("250x200")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
loginframe = ttk.Frame(root)
loginframe.grid(column=0, row=0)

access_token_label = ttk.Label(loginframe, text='Access token')
access_token_label.grid(row=1, column=1)
access_token = StringVar()
access_token_entry = ttk.Entry(loginframe, width=25, textvariable=access_token)
access_token_entry.grid(row=2, column=1)

login_button = ttk.Button(loginframe, text='Login', command=gamelogin)
login_button.grid(row=3, column=1, pady=(15, 0))
separator = ttk.Separator(loginframe, orient="horizontal")
separator.grid(row=4, column=1, ipadx=120, pady="10")

newagent_button = ttk.Button(loginframe, text='New Agent', command=newagent_dialog)
newagent_button.grid(row=5, column=1)






root.mainloop()