import tkinter as tk


def count_up():
    global tmr
    tmr = tmr+1
    label["text"] = tmr
    root.after(1000, count_up)


if __name__ == "__main__":
    root = tk.Tk()

    label = tk.Label(root, font=("", 80))
    label.pack()

    tori = tk.PhotoImage(file="fig/5.png")
    cx, cy = 300, 400
    
    canvas.create_image(cx, cy, image=tori, tag="tori")

    tmr = 0
    root.after(1000, count_up)

    root.mainloop()






