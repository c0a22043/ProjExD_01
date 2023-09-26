import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん！")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    font = pg.font.Font(None, 80)
    background = pg.image.load("ex01/fig/pg_bg.jpg")
    bird = pg.image.load("ex01/fig/3.png")
    bird_flipped = pg.transform.flip(bird, True, False)



    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.blit(background, (0, 0))

        
        screen.blit(bird_flipped, (400, 200))

        txt = font.render(str(tmr), True, (255, 255, 255))
        screen.blit(txt, [100, 100])

        
        pg.display.update()
        tmr += 1
        clock.tick(1)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()