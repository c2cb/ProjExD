print("hallo world")

import tkinter as tk # tkinterの名前をtkとしている
import tkinter.messagebox


def Button_click(event):
    btn = event.widget
    btn["fg"]
    tkm.showwarning("けいこく", f"{txt}ボタンが押されました")


root = tk.Tk() # tkのインスタンスを生成している。Tkはウィンドウ。
root.title("おためしか")
root.geometry("500200")

label = tk.Label(root,
                text="らべるを書いてみたken",
                font=("", 30)
                )
label.pack()

button = tk.Button(root,
                    txt="押すな",
                    font=("", 30),
                    bg="#000FF"),        
button.pack()

entry = tk.Entry(root,
                width=30,
                font=("", 30)
                )
entry.insert(tk.End, "fugapiyo")
entry.pack()


button = tk.Button(root, text="押すな", font="")
button.bind("<1>")




root.mainloop()



