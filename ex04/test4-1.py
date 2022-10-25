import pygame as pg
import sys



def main():
    pg.display.set_caption("初めてのPyGame")
    scrn_sfc = pg.display.set_mode((800, 600))

    tori_sfc = pg.image.load("fig/6.png")
    tori_rct = tori_sfc.get_rect()
    # これ
    tori_rct.center = 700, 400
    # tori_rct.centerx = 700
    # tori_rct.centerx = 400
    # でもできる

    # スクリーンにこうかとんを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct)


    clock = pg.time.Clock()
    clock.tick(0.5)




if __name__ == "__main__":
    pg.init() # 初期化
    main() # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit() # プログラムを終了する


