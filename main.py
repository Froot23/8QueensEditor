# This is a sample Python script.
import pygame as pg
import pygame.image
import sets

mat = []
run = True
img = pygame.image.load("queen.png")
img = pg.transform.scale(img, (80,80))
wrong = set()

def board_size(n):
    return [[False for j in range(n)] for i in range(n)]

def add_queen(x, y):
    mat[x][y] = True
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def draw():
    for i in range(8):
        for j in range(8):
            if ((j + i) % 2 == 0):
                pg.draw.rect(win, (153, 110, 57), boxes[i][j])
            else:
                pg.draw.rect(win, (89, 63, 31), boxes[i][j])
            if(mat[i][j]):
                if (i,j) in wrong:
                    err = pg.Surface((80,80))
                    err.fill((255,0,0))
                    err.set_alpha(128)
                    win.blit(err, boxes[i][j])
                win.blit(img, boxes[i][j])
    pg.display.update()

def check():
    wrong.clear()
    for i in range(8):
        for j in range(8):
            if(mat[i][j]):
                for k in range(8):
                    #horiztonal
                    if(mat[i][k] and k != j):
                        wrong.add((i,k))
                        wrong.add((i,j))
                    #vertical
                    if(mat[k][j] and k != i):
                        wrong.add((k, j))
                        wrong.add((i, j))
                    #diagonal right
                    if(k+i+1 < 8 and k+j+1 < 8 and mat[k+i+1][k+j+1]):
                        wrong.add((i,j))
                        wrong.add((k+i+1, k+j+1))
                    #diagonal left
                    if(k+i+1 < 8 and j-k-1 >=0 and mat[k+i+1][j-k-1]):
                        wrong.add((i, j))
                        wrong.add((k + i + 1, j-k-1))


# def color():
    # for i in range(len(wrong)):
#             TODO make the color do colory things
# TODO make the color an opaque red that covers the tile not the queen

win = pg.display.set_mode(size=(800,800))
win.fill((191, 225, 242))
mat = board_size(8)
boxes = [[pg.Rect(j*80 + 80,i*80 + 80,80,80) for j in range(8)] for i in range(8)]
for i in range(8):
    for j in range(8):
        if((j+i) % 2 == 0):
            pg.draw.rect(win, (153, 110, 57), boxes[i][j])
        else:
            pg.draw.rect(win, (89, 63, 31), boxes[i][j])



pg.display.update()

while(run):
    for e in pg.event.get():
        if(e.type == pg.MOUSEBUTTONUP):
            if(e.button == 1):
                if(not(e.pos[1] < 80 or e.pos[1] > 720 or e.pos[0] < 80 or e.pos[0] > 720)):
                    mat[e.pos[1]//80 - 1][e.pos[0]//80 - 1] = True
            elif(e.button == 3):
                if (not (e.pos[1] < 80 or e.pos[1] > 720 or e.pos[0] < 80 or e.pos[0] > 720)):
                    mat[e.pos[1]//80 - 1][e.pos[0]//80 - 1] = False
            check()
            draw()
        if e.type == pg.QUIT:
            run = False