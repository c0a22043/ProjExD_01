import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bird_flipped = pg.image.load("ex01/fig/3.png")
    bird_flipped = pg.transform.flip(bird_flipped, True, False)
    bird_rotated = pg.transform.rotate(bird_flipped, 10)
    bird_images = [bird_flipped, bird_rotated]
    tmr = 0
    idx = 0  
    bird_x, bird_y = 300, 200
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        screen.blit(bird_images[idx], (bird_x, bird_y))
        idx = 1 - idx
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()