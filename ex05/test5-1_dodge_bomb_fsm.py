import pygame as pg
import sys
from random import randint





class Screen:
    def __init__(self, title, whi):
        # 練習1
        pg.display.set_caption(title) # "逃げろ！こうかとん"
        self.sfc = pg.display.set_mode(wh) # (1600, 900)
        self.rct = sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) # "fig/pg_bg.jpg"
        self.bgi_rct = bgi_sfc.get_rect()


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init___(self, img, zoom, xy):
        # 練習3
        sfc = pg.image.load(img) # "fig/6.png"
        self.sfc = pg.transform.rotozoom(sfc, 0, zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) # 練習3


class  Bomb:
    def __init__(self, color, radius, vxy, scr:Screen):
        # 練習5
        self.sfc = pg.Surface((raduys*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.ct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self._rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6



def update(self, scr;Screen):
    key_states = pg.key.get_pressed()
    for key, delta in Bird.key_delta.items():
        if key_states[key]:
            self.rct.centerx += delta[0]
            self.rct.centery += delta[1]
            # 練習7
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
    self.blid(scr) # = scr.sfc.blit(self.sfc, self.rct)



def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate


def main():
    # 練習1
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")

    # 練習3
    kkt = Bird("fig/6.png", 2.0, (900, 400))

    # 練習5
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)
    
    

    clock = pg.time.Clock() # 練習1
    while True:
        scrn_sfc.blit(bg_sfc, bg_rct) # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        kkt.update(scr)

        

        # 練習7
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx, vy) # 練習6
        scrn_sfc.blit(bomb_sfc, bomb_rct) # 練習5

        # 練習8
        if tori_rct.colliderect(bomb_rct): # こうかとんrctが爆弾rctと重なったら
            return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()
