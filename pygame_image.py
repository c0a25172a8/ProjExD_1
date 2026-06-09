import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False) #練習8背景二枚目反転
    kk_img = pg.image.load("fig/3.png") #練習3こうかとん表示
    kk_img = pg.transform.flip(kk_img,True,False)
    kk_rct = kk_img.get_rect() #練習10-1こうかとんrectの取得
    kk_rct.center = 300,200 #練習10-2初期位置

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() #練習10-3キーの押してる情報の取得
        #print(key_lst)
        if key_lst[pg.K_UP]: #練習10-4こうかとん移動
            kk_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:
            kk_rct.move_ip((0,1))
        if key_lst[pg.K_LEFT]:
            kk_rct.move_ip((-1,0))
        else: #演習1-1何も押していないと左にいく
            kk_rct.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:
            kk_rct.move_ip((1,0))
        
        
        x = tmr % 3200 #練習9ループさせる計算
        screen.blit(bg_img, [-x, 0]) #練習5背景動くように
        screen.blit(bg_img2, [-x+1600, 0]) #練習7背景残像の2枚目
        screen.blit(bg_img, [-x+3200, 0]) #練習9背景の3枚目
        #screen.blit(kk_img, [300, 200]) #練習4こうかとん位置
        screen.blit(kk_img,kk_rct) #練習10-5
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習6FPS変更


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()