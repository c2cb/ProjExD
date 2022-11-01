import pygame as pg
import sys
from random import randint

# コメント14を受けての修正
# プロジェクト演習テーマD 第5回授業資料、P13
# 一貫性にこだわりすぎるのは、狭い心の表れである
# より見やすさのために、臨機応変さも必要であるため、ここでは関数と関数の区切りに
# 使用した改行は3
# 中身の処理の区切りに使用した改行は2、状況を見て1
# 以上の通り修正した。


class Screen:
    def __init__(self, title, wh, bgimg):
        pg.display.set_caption(title) #逃げろ！こうかとん
        self.sfc = pg.display.set_mode(wh) #(1600, 900)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgimg) #"fig/pg_bg.jpg"
        self.bgi_rct = self.bgi_sfc.get_rect()
        

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)



class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }


    def __init__(self, img, zoom, xy, scr):
        sfc = pg.image.load(img) # "fig/6.png"
        self.zoom = zoom
        self.sfc = pg.transform.rotozoom(sfc, 0, self.zoom) # 2.0
        self.rct = self.sfc.get_rect()
        self.rct.center = xy # 900, 400
        self.bolls = []
        self.scr = scr


    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)


    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        img = "ex05/fig/0.png"
        if (key_states[pg.K_UP]):
            img = "ex05/fig/6.png"
        if (key_states[pg.K_DOWN]):
            img = "ex05/fig/3.png"
        if (key_states[pg.K_LEFT]):
            img = "ex05/fig/5.png"
        if (key_states[pg.K_RIGHT]):
            img = "ex05/fig/2.png"
        new_img = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(new_img, 0, self.zoom)

        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)

 # コメント13を受けての修正
    def atakku(self): # こうかとんの領域展開の発動について
        key_states = pg.key.get_pressed() 
        if (key_states[pg.K_SPACE]): # スペースキーを押した際に領域が展開される
            ata = Atakku(self, (50, 50, 255), 10, 1, 1) #self, bird, color, radius, Vx, Vy
            self.bolls.append(ata)
        for i in range(len(self.bolls)):
            self.bolls[i].update(self.scr) # 領域の展開



class Bomb:
    def __init__(self, color, radius, vxy, scr:Screen):
        self.sfc = pg.Surface((radius*2, radius*2)) # 空のSurface
        self.sfc.set_colorkey((0, 0, 0)) # 四隅の黒い部分を透過させる
        pg.draw.circle(self.sfc, color, (radius, radius), radius) # 爆弾用の円を描く
        self.rct = self.sfc.get_rect() 
        self.vx, self.vy = vxy


    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)


    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)


 # コメント13を受けての修正
class Atakku: # こうかとんの領域展開の大元
    def __init__(self, bird, color, radius, Vx, Vy):
        self.sfc = pg.Surface((radius*2, radius*2))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (radius, radius), radius)
        self.rct = self.sfc.get_rect()
        self.rct.center = bird.rct.center
        self.vx = Vx
        self.vy = Vy
    

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)


    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate 
        self.blit(scr) # =scr.sfc.blit(self.sfc, self.rct)

        

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
    scr = Screen("逃げろ！こうかとん", (1600, 900), "ex05/fig/pg_bg.jpg")

    # 練習3
    kkt = Bird("ex05/fig/6.png", 2.0, (900, 400), scr)

    # 練習5
    bkd = Bomb((255, 0, 0), 10, (+1, +1), scr)

    clock = pg.time.Clock() # 練習1
    while True:
        scr.blit() # 練習2
        
        for event in pg.event.get(): # 練習2
            if event.type == pg.QUIT:
                return

        # 練習4
        kkt.update(scr)
        # 練習7
        bkd.update(scr)
        kkt.atakku()

        # 練習8
        if kkt.rct.colliderect(bkd.rct): # こうかとんrctが爆弾rctと重なったら
            return

        pg.display.update() #練習2
        clock.tick(1000)

if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()


    