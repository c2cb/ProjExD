import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    # 練習1
    root.title("迷えるこうかとん")

    # 練習2
    canv = tk.Canvas(root, width=1500, height=900, bg="black")
    canv.pack()

    # 練習3
    tori = tk.PhotoImage(file="ex03/fig/1.png")
    cx, cy = 300, 400
    canv.create_image(cx, cy, image=tori, tag="tori")

    # 練習4
    key = ""# 現在押されているキーを表す

    root.mainloop()

