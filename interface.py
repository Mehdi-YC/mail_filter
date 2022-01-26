from tkinter import *
from tkinter import font
from turtle import bgcolor
import ttkbootstrap as ttk
from ttkbootstrap import * 
from ttkbootstrap.constants import * 
from filter import get,filter,add
import sqlite3
conn = sqlite3.connect("mails.db")
conn.row_factory = lambda cursor, row: row[0]
cur = conn.cursor()
root = Tk()




st = Style()
st.configure('B1.TButton',borderwidth=0, background='#E85656',font=('Arial', 14 ))
segment = ttk.Button(root, text='Segment', style='B1.TButton').grid(row=0,column=5)

st2 = Style()
st2.configure('B2.TButton',borderwidth=0,background='#E85656' ,font=('Arial', 14 ))



# Pick up List
middle_click = ttk.Labelframe(
            root,
            text='Middle Click',
            padding=(15, 10)
        )

cbo = ttk.Combobox(
            root,
            values=['DZ', 'PRO', 'CASUAL','Garbage'], font=('Arial',15)
        )
cbo.current(0)
cbo.grid(row=0,column=8)
# Option
# Option = Listbox(root,width=15, height=4, selectmode=SINGLE)
# Option.grid(row=0,column=10,padx=(0,10),pady=(20,0))
# Option.insert(0, 'DZ')
# Option.insert(1, 'PRO')
# Option.insert(2, 'CASUAL')
# Option.insert(3, 'GARBAGE')
# DZ List
DZ = Listbox(root,width=30, height=20, selectmode=MULTIPLE,font=("Arial", 15))

# DZ.pack(padx=5, pady=20, side=LEFT)
labelDz = ttk.Label(root,
                    text = "DZ",font=("Arial", 15))
labelDz.grid(column=5, row=4,pady=(100,10))
DZ.grid(row=5,column=5,padx=(20,20))




# PRO list
labelPRO = ttk.Label(root,
                    text = "PRO",font=("Arial", 15))
labelPRO.grid(column=6, row=4,pady=(100,10))
PRO = Listbox(root, width=30, height=20, selectmode=MULTIPLE,  font=("Arial", 15))
# PRO.pack(padx=5, pady=25, side=LEFT)
PRO.grid(row=5,column=6,padx=(20,20))


    



# Casual List 
labelCasual = ttk.Label(root,
                    text = "Casual",font=("Arial", 15))
labelCasual.grid(column=7, row=4,pady=(100,10))
Casual = Listbox(root, width=30, height=20, selectmode=MULTIPLE,font=("Arial", 15))
# Casual.pack(padx=5, pady=25, side=LEFT)
Casual.grid(row=5,column=7,padx=(20,20))




# Garbage List
labelGarbage = ttk.Label(root,
                    text = "Garbage",font=("Arial", 15))
labelGarbage.grid(column=8, row=4,pady=(100,10))
Garbage = Listbox(root, width=30, height=20, selectmode=MULTIPLE,font=("Arial", 15))
# Garbage.pack(padx=5, pady=30, side=LEFT)
Garbage.grid(row=5,column=8,padx=(20,20))


def refresh():
    dz_list_item=get(cur,'DZ')
    Pro_list_item=get(cur,'PRO')
    Casual_list_item=get(cur,'CASUAL')
    Garbage_list_item=get(cur,'ERROR')
    DZ.delete(0,END)   
    PRO.delete(0,END) 
    Casual.delete(0,END)
    Garbage.delete(0,END)   
    for i,j in enumerate(dz_list_item):
        DZ.insert(i, j)
    for i,j in enumerate(Pro_list_item):
        PRO.insert(i, j)
        print(i) 
    for i,j in enumerate(Casual_list_item):
        Casual.insert(i, j)
    for i,j in enumerate(Garbage_list_item):
        Garbage.insert(i, j)

refresh()

def change():
  
    email_list=[DZ,Casual,PRO,Garbage]

    for i in email_list:
       
      a=[i.get(x) for x in i.curselection()]
      if len(a):
          break
    a = "','".join(a)

    cur.execute(f"Update mails set type='{cbo.get()}'  WHERE mail IN ('{a}');")    
    conn.commit()
    refresh()
    print(a)
     


Change =ttk.Button(root, text='Change', style='B2.TButton',command=change).grid(row=0,column=7,pady=(20,0))



root.geometry('1500x800')
root.resizable(width=0, height=0)
root.title('PythonLobby.com')
root.mainloop()


