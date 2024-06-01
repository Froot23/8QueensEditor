# This is a sample Python script.
import pygame as pg
import pygame.image
pg.init()
# import sets

placedQueens = 0
mat = []
run = True
img = pygame.image.load("queen.png")
wrong = set()
#TODO it inputable (text field + increment/decrement buttons)
n = 4;
border = 100;
y = pg.display.get_desktop_sizes()[0][1] - 75
x = pg.display.get_desktop_sizes()[0][0]
size = (y-border*2)//n
img = pg.transform.scale(img, (size,size))

def sizing(n):
    global size
    global img
    size = (y - border * 2) // n
    img = pg.transform.scale(img, (size, size))
def board_size(n):
    return [[False for j in range(n)] for i in range(n)]

def add_queen(x, y):
    mat[x][y] = True
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def draw():
    win.fill((191, 225, 242))
    pygame.draw.rect(win, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    win.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    pygame.draw.rect(win, pygame.Color('chartreuse3'), inn)
    pygame.draw.rect(win, pygame.Color('red'), dec)
    plus_text = base_font.render("+", True, (255, 255, 255))
    win.blit(plus_text, (inn.x + 25, inn.y + 5))
    min_text = base_font.render("-", True, (255, 255, 255))
    win.blit(min_text, (dec.x + 25, dec.y + 5))

    text_color = (255, 255, 255)

    if (len(wrong) == 0 and placedQueens == n):
        r = pg.Rect((90, 90), (size * n + 20, size * n + 20))
        pg.draw.rect(win, (63, 222, 35), r)
        text_color = (pg.Color("green"))
    else:
        r = pg.Rect((90, 90), (size * n + 20, size * n + 20))
        pg.draw.rect(win, (191, 225, 242), r)
        text_color = (255, 255, 255)

    for i in range(n):
        for j in range(n):
            if ((j + i) % 2 == 0):
                pg.draw.rect(win, (153, 110, 57), boxes[i][j])
            else:
                pg.draw.rect(win, (89, 63, 31), boxes[i][j])
            if(mat[i][j]):
                if (i,j) in wrong:
                    err = pg.Surface((size,size))
                    text_color = (pg.Color("red"))
                    # TODO make text red then github
                    err.fill((255,0,0))
                    err.set_alpha(128)
                    win.blit(err, boxes[i][j])
                win.blit(img, boxes[i][j])

    score = base_font.render(f"Score: {placedQueens}/{n}", True, (text_color))
    pic = pg.Surface((score.get_width(), score.get_height()))
    pic.fill(pg.Color('black'))
    pic.blit(score, (0, 0))
    win.blit(pic, (input_rect.x + 15, input_rect.y - 50))
    pg.display.update()

def check():
    wrong.clear()
    for i in range(n):
        for j in range(n):
            if(mat[i][j]):
                for k in range(n):
                    #horiztonal
                    if(mat[i][k] and k != j):
                        wrong.add((i,k))
                        wrong.add((i,j))
                    #vertical
                    if(mat[k][j] and k != i):
                        wrong.add((k, j))
                        wrong.add((i, j))
                    #diagonal right
                    if(k+i+1 < n and k+j+1 < n and mat[k+i+1][k+j+1]):
                        wrong.add((i,j))
                        wrong.add((k+i+1, k+j+1))
                    #diagonal left
                    if(k+i+1 < n and j-k-1 >=0 and mat[k+i+1][j-k-1]):
                        wrong.add((i, j))
                        wrong.add((k + i + 1, j-k-1))

def resize(n):
    global mat
    global boxes
    global img
    global placedQueens
    placedQueens = 0;
    img = pygame.image.load("queen.png")
    sizing(n)
    mat = board_size(n)
    boxes = [[pg.Rect(j * size + border, i * size + border, size, size) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if ((j + i) % 2 == 0):
                pg.draw.rect(win, (153, 110, 57), boxes[i][j])
            else:
                pg.draw.rect(win, (89, 63, 31), boxes[i][j])

win = pg.display.set_mode(size=(x, y))
win.fill((191, 225, 242))
mat = board_size(n)
boxes = [[pg.Rect(j*size + border,i*size + border,size,size) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if((j+i) % 2 == 0):
            pg.draw.rect(win, (153, 110, 57), boxes[i][j])
        else:
            pg.draw.rect(win, (89, 63, 31), boxes[i][j])

base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(x-800, y-500, 140, 32)
inn = pygame.Rect(x-710, y-450, 50, 32)
# inn.topleft = input_rect.bottomleft
dec = pygame.Rect(x-800, y-450, 50, 32)
color = pygame.Color('chartreuse4')
active = False
pygame.draw.rect(win, color, input_rect)
pygame.draw.rect(win, pygame.Color('chartreuse3'), inn)
pygame.draw.rect(win, pygame.Color('red'), dec)
text_surface = base_font.render(user_text, True, (255, 255, 255))
win.blit(text_surface, (input_rect.x+5, input_rect.y+5))
plus_text = base_font.render("+", True, (255, 255, 255))
win.blit(plus_text, (inn.x+25, inn.y+5))
min_text = base_font.render("-", True, (255, 255, 255))
win.blit(min_text, (dec.x+25, dec.y+5))
# input_rect.w = max(100, text_surface.get_width()+10)
score = base_font.render(f"Score: {placedQueens}/{n}", True, (255, 255, 255))
pic = pg.Surface((score.get_width(), score.get_height()))
pic.fill(pg.Color('black'))
pic.blit(score, (0,0))
win.blit(pic, (input_rect.x+15, input_rect.y-50))


pg.display.update()

while(run):
    for e in pg.event.get():
        if(e.type == pg.MOUSEBUTTONUP):
            if(e.button == 1):
                if(not(e.pos[1] < border or e.pos[1] > border-1+ n * size or e.pos[0] < border or e.pos[0] > border-1+ n * size)):
                    if(mat[(e.pos[1]-border)//size][(e.pos[0]-border)//size] == False):
                        mat[(e.pos[1]-border)//size][(e.pos[0]-border)//size] = True
                        placedQueens += 1
                if input_rect.collidepoint(e.pos):
                    active = True
                elif inn.collidepoint(e.pos):
                    n = n+1
                    resize(n)
                #     TODO resize stuff
                elif dec.collidepoint(e.pos):
                    n = (1 if n==1 else n-1)
                    resize(n)
                else:
                    active = False
            elif(e.button == 3):
                if (not (e.pos[1] < border or e.pos[1] > border-1+ n * size or e.pos[0] < border or e.pos[0] > border-1+ n * size)):
                    if(mat[(e.pos[1]-border)//size][(e.pos[0]-border)//size] == True):
                        mat[(e.pos[1]-border)//size][(e.pos[0]-border)//size] = False
                        placedQueens -= 1
            check()
            draw()
        if(e.type == pg.KEYDOWN):
            if(active):
                if e.key == pygame.K_BACKSPACE:
                  user_text = user_text[:-1]
                elif e.key == pygame.K_RETURN:
                    # if(not user_text.isalpha()):
                    n = int(user_text)
                    user_text = ''
                    resize(n)
                elif(e.unicode.isnumeric()):
                    user_text += e.unicode
                draw()
        if e.type == pg.QUIT:
            run = False