import pygame as pg
import sys
from random import randint




# 追加機能で、tkを使用していたら、という方針のコードです。ここから、
# import tkinter as tk
# def botanhantei(event) :
#     btn1 = event.widget
#     txt = btn1["text"]


# def atattatoki() :
#     root = tk.Tk()
#     root.title("イダイ!!!!!!!!!!!!")
#     root.geometry("100x200")

#     label = tk.Label(root,
#                     text="当たってしまいました！\nどうしますか？",
#                     font=("Ricty Diminished", 20)
#                     )
#     label.pack()

#     button1 = tk.Button(root, text="続ける")
#     button2 = tk.Button(root, text="終わる")
#     button1.bind("<1>", botanhantei)
#     button2.bind("<1>", botanhantei)
#     button1.pack()
#     button2.pack()

#     root.mainloop()

#     '''if (button1):
#         return 1
#     if (button2):
#         return 0'''
# ここまで
    



def check_bound(obj_rct, scr_rct) :
    """
    obj_rct:こうかとんrct, または, 爆弾rct
    rcr_rct:スクリーンrct
    領域内：+1 / 領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    global mode
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()

    # コメント12から、modeについて詳しく説明を付けました。
    while True:
        if mode == 0:
            # modeは、ゲームが終了か継続かを判断する際に使われる。
            # 0の場合はゲームは再開となり、0の場合では終了となる。
            bg_sfc = pg.image.load("fig/pg_bg.jpg")
            bg_rct = bg_sfc.get_rect()
    

            # 練習3
            tori_sfc = pg.image.load("fig/6.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
            tori_rct = tori_sfc.get_rect() # Rect
            tori_rct.center = 900, 400
            # tori_rct = tori_sfc


            # 練習5
            bomb_sfc = pg.Surface((20, 20)) # 空のSurface
            bomb_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
            pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) # 円を描く
            bomb_rct = bomb_sfc.get_rect()
            bomb_rct.centerx = randint(0, scrn_rct.width)
            bomb_rct.centery = randint(0, scrn_rct.height)

            # 練習6
            vx, vy = +1, +1


            clock = pg.time.Clock() # 練習1
            while True:
                scrn_sfc.blit(bg_sfc, bg_rct) # 練習2
                # pg.display.update() # 練習2

                for event in pg.event.get(): # 練習2
                    if event.type == pg.QUIT:
                        return

                
                key_states = pg.key.get_pressed()

                # コメント11から、先生のリポジトリを参考に簡潔にまとめてみました。
                # key_delta = {
                #     pg.K_UP:    [0, -1],
                #     pg.K_DOWN:  [0, +1],
                #     pg.K_LEFT:  [-1, 0],
                #     pg.K_RIGHT: [+1, 0],
                # }

                # しかし、こうかとんが移動方法によって動きを変えたいため、
                # ここでは元の文で行かせていただきます。

                # 元の文はここから、
                if key_states[pg.K_UP]: # こうかとんの縦座標を+1
                    tori_rct.centery -= 1
                    tori_sfc = pg.image.load("fig/6.png")
                    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)

                if key_states[pg.K_DOWN]: # こうかとんの縦座標を-1
                    tori_rct.centery += 1
                    tori_sfc = pg.image.load("fig/3.png")
                    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
                
                if key_states[pg.K_LEFT]: # こうかとんの横座標を-1
                    tori_rct.centerx -= 1
                    tori_sfc = pg.image.load("fig/5.png")
                    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)

                if key_states[pg.K_RIGHT]: # こうかとんの横座標を+1
                    tori_rct.centerx += 1
                    tori_sfc = pg.image.load("fig/2.png")
                    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
                # ここまで
                

                yoko, tate = check_bound(tori_rct, scrn_rct)


                if yoko == -1:
                    if key_states[pg.K_LEFT]:
                        tori_rct.centerx += 1
                    if key_states[pg.K_RIGHT]:
                        tori_rct.centerx -= 1
                
                if tate == -1:
                    if key_states[pg.K_UP]:
                        tori_rct.centery += 1
                    if key_states[pg.K_DOWN]:
                        tori_rct.centery -= 1
                scrn_sfc.blit(tori_sfc, tori_rct) # 練習3


                # 練習7
                yoko, tate = check_bound(bomb_rct, scrn_rct)
                vx *= yoko
                vy *= tate
                bomb_rct.move_ip(vx, vy) # 練習6
                scrn_sfc.blit(bomb_sfc, bomb_rct) # 練習5


                # 練習8
                if tori_rct.colliderect(bomb_rct):
                    # tori_sfc = pg.image.load("fig/bakuhatu.png")
                    # tori_sfc = pg.transform.rotozoom(tori_sfc, 0, -2.0)
                    mode = 1
                    break

                # scrn_sfc.blit(tori_sfc, tori_rct) # 練習3
                # scrn_sfc.blit(bomb_sfc, bomb_rct) # 練習5

                pg.display.update() # 練習2
                clock.tick(1000)

        else:
            bg_sfc = pg.image.load("fig/pg_bg.jpg")
            bg_rct = bg_sfc.get_rect()
            clock = pg.time.Clock()
            while True:

                for event in pg.event.get(): # 練習2
                    if event.type == pg.QUIT:
                        return

                key_states = pg.key.get_pressed()
                if key_states[pg.K_UP]: # UPを押した際、modeは0となり、ゲームは再開される
                    mode=0
                    break
                if key_states[pg.K_DOWN]: # DOWNを押した際、tori_rct.colliderectへreturnされ、modeは1となり、ゲームは終了する。
                    return

                scrn_sfc.blit(bg_sfc, bg_rct)
                tmr = "RESTART:UP OVER:DOWN"
                fonto = pg.font.Font(None, 80)
                txt = fonto.render(str(tmr), True, (0, 0, 0))
                scrn_sfc.blit(txt, (300, 200))
                

                pg.display.update()
                
                clock.tick(1000)
            
    

        
    

if __name__ == "__main__":
    mode = 0
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit # 初期化の解除
    sys.exit()
    

    # スクリーンにこうかとんを貼り付ける
    # scrn_sfc.blit(tori_sfc, tori_rct)


    # clock = pg.time.Clock()
    # clock.tick(0.5)






