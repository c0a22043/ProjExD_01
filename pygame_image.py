import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bird_flipped = pg.image.load("ex01/fig/3.png")
    bird_flipped = pg.transform.flip(bird_flipped, True, False)
    bird_rotozoom = pg.transform.rotozoom(bird_flipped, 10,1.0)
    bird_images = [bird_flipped, bird_rotozoom]
    tmr = 0
    bird_x, bird_y = 300, 200
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x -= 1
        if x < 0:
            x = 1599

        screen.blit(bg_img, [x, 0])
        screen.blit(bg_img, (x - 1600, 0))
        screen.blit(bird_images[tmr%2], (bird_x, bird_y))
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()