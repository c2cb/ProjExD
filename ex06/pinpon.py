import pygame as pg
import sys
from pygame.locals import *
from random import randint


p1s = 0
p2s = 0


key_delta = {
    pg.K_UP:    [0, -1],
    pg.K_DOWN:  [0, +1],
}



# ピンポン玉が壁に当たった際の判定
def check_bound(obj_rct, scr_rct):
    global p1s, p2s
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: # yoko
        if (obj_rct.left < scr_rct.left) :
            p2s += 1
        elif (scr_rct.right < obj_rct.right) :
            p1s += 1
        obj_rct.centerx = 800
        obj_rct.centery = 450
        
        print(p1s, p2s)
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: # tate
        tate = -1
    return yoko, tate



# ラケットが壁に当たった際の判定
def check_bound2(obj_rct, scr_rct):
    tate = +1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return tate



def main():
    global p1s, p2s
    # キャプション、ディスプレイ作成
    pg.display.set_caption("ピンポン対戦ゲーム")
    screen1 = pg.display.set_mode((1600, 900))
    scrn1 = screen1.get_rect()
    screen2 = pg.image.load("ex06/shikancha.png")
    scrn2 = screen2.get_rect()

    # ピンポン玉
    bomb_sfc = pg.Surface((20, 20)) # 空のSurface
    bomb_sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10) # 円を描く
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(0, scrn1.width)
    bomb_rct.centery = randint(0, scrn1.height)
    vx, vy = +5, +5

    # 左のラケット
    L_raket = pg.Surface((20, 200))
    pg.draw.rect(L_raket, (72, 61, 139), (5, 5, 25, 25))
    L_raket2 = L_raket.get_rect()
    L_raket2.center = 100, 500

    # 右のラケット
    R_raket = pg.Surface((20, 200))
    pg.draw.rect(R_raket, (0, 128, 0), (5, 5, 25, 25))
    R_raket2 = R_raket.get_rect()
    R_raket2.center = 1500, 500



    while True:
        screen1.blit(screen2, scrn2)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        
        screen1.blit(L_raket, L_raket2)
        screen1.blit(R_raket, R_raket2)

        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]: # 縦座標を+1
            if (R_raket2.centery > 100):
                R_raket2.centery -= 4
        if key_states[pg.K_DOWN]: # 縦座標を-1
            if (R_raket2.centery < 800):
                R_raket2.centery += 4
        if key_states[pg.K_w]:# 縦座標を-1
            if (L_raket2.centery > 100):
                L_raket2.centery -= 4
        if key_states[pg.K_s]: # 縦座標を-1
            if (L_raket2.centery < 800):
                L_raket2.centery += 4

        # ピンポン玉を動かす
        yoko, tate = check_bound(bomb_rct, scrn1)
        vx *= yoko
        vy *= tate

        # ピンポン玉がラケットにあたった際の反射
        if L_raket2.colliderect(bomb_rct):
            vx *= -1
        if R_raket2.colliderect(bomb_rct):
            vx *= -1
        
        bomb_rct.move_ip(vx, vy)
        screen1.blit(bomb_sfc, bomb_rct)
        
        
        pr1 = "Player1 Score:"
        fonto = pg.font.Font(None, 40)
        txt = fonto.render(str(pr1), True, (72, 61, 139))
        screen1.blit(txt, (300, 50))

        txt = fonto.render(str(p1s), True, (72, 61, 139))
        screen1.blit(txt, (520, 50))

        pr2 = "Player2 Score:"
        fonto = pg.font.Font(None, 40)
        txt = fonto.render(str(pr2), True, (0, 128, 0))
        screen1.blit(txt, (950, 50))

        txt = fonto.render(str(p2s), True, (0, 128, 0))
        screen1.blit(txt, (1170, 50))


        pg.display.update()

    
if __name__ == "__main__":
    pg.init() # モジュールを初期化する
    main()
    pg.quit() # モジュールの初期化を解除する
    sys.exit() # プログラムを終了する


