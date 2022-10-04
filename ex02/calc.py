# print("aaa") 使わないコードは消す（見えていない予定）


import tkinter as tk
import tkinter.messagebox as tkm


# 練習3
def click_number(event):
    btn = event.widget
    num = btn["text"]
    entry.insert(tk.END, num)


# 練習7
def click_equal(event):
    eqn = entry.get()
    res = eval(eqn)
    entry.delete(0, tk.END)
    entry.insert(tk.END, res)
    

# 練習5
    entry.insert(tk.END, num)


# 練習１
root = tk.Tk()
root.geometry("300x500")


# 練習2
entry = tk.Entry(root, width=10, font=("", 40), justify="right")

# 練習4
entry.grid(row=0, column=0, columnspan=3)


r = 1 # row
c = 0 # column

numbers = list(range(9, -1, -1))
operators = ["+"]
# 四則演算を追加する！！！！！

for i, num in enumerate(numbers+operators, 1):
    btn = tk.Button(root,
                    text=f"{num}",
                    font=("", 30),
                    width=4,
                    height=2)

    btn.bind("<1>", click_number)
    btn.grid(row=r, column=c)
    c += 1

    if (i%3==0):
        r += 1
        c = 0

btn = tk.Button(root, text=f"=",
                font=("", 30),
                width=4,
                height=2)
btn.bind("<1>", click_equal)
btn.grid(row=r, column=c)

    
root.mainloop()

