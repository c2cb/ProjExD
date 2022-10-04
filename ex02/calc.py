print("aaa")

import tkinter as tk

#練習１
root = tk.Tk() 
root.geometry("300*500")


# 練習2
for num in range(9, -1, -1):
    btn =tk.Button(root, text=f"{num}", font=("", 30), whidth=4, height=2)
    btn.grid(row=r, column=c)

    if (i%3==0):
        r += 1
        c += 0
    c += 1
    

btn.pack()

root.mainloop
