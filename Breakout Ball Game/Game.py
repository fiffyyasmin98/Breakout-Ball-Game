from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import pygame as pg

pg.init()
tick = pg.mixer.Sound('jazz.wav')
crash = pg.mixer.Sound('crash.wav')
music = pg.mixer.music.load('Werq.mp3')
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(.1)

FROM_RIGHT = 1
FROM_LEFT = 2
FROM_TOP = 3
FROM_BOTTOM = 4
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500
deltaX = 1
deltaY = 1
time_interval = 5


class BLOCK:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

ball = BLOCK(100, 100, 120, 120)
border = BLOCK(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
Stick = BLOCK(370, 0, 470, 10)
side1 = BLOCK(0, 0, 10, 280)
side2 = BLOCK(790, 0, 800, 280)
blockList = []
sidesList=[]
x = 15
y = 350
sidex=0
sidey=280
for i in range(0, 156):
    if (i % 13 == 0):
        x = 15
        y += 30
    if(i%39==0):
        y+=50

    blockList.append(BLOCK(x, y, x + 50, y + 20))
    x += 60

def defaultVlaues():
    global sidesList
    global blockList
    global x
    global y
    global move
    global pause
    global sidex
    global sidey
    blockList.clear()
    sidesList.clear()
    pause = True
    move=0
    x = 15
    y = 350
    # sidex = 0
    # sidey = 280
    for i in range(0, 156):
        if (i % 13 == 0):
            x = 15
            y += 30
        if (i % 39 == 0):
            y += 50
        blockList.append(BLOCK(x, y, x + 50, y + 20))
        x += 60
# Initialization
def init():
    glClearColor(0, 0, 0.1,1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT, 0, 1)

    glMatrixMode(GL_MODELVIEW)

def DrawRectangle(rect,r,g,b):
    glLoadIdentity()
    glColor(r,g,b)
    glBegin(GL_QUADS)
    glVertex(rect.left, rect.bottom, 0)  # Left Bottom
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()

def DrawPolygon(rect,r,g,b):
    glLoadIdentity()
    glColor(r,g,b)
    glBegin(GL_POLYGON)
    glVertex(rect.left+4, rect.top, 0)
    glVertex(rect.left , rect.top -4, 0)
    glVertex(rect.left , rect.bottom +4 , 0)  # Left Bottom
    glVertex(rect.left+4, rect.bottom, 0)
    glVertex(rect.right-4, rect.bottom, 0)
    glVertex(rect.right, rect.bottom+4, 0)
    glVertex(rect.right, rect.top-4, 0)
    glVertex(rect.right-4, rect.top, 0)
    glEnd()

def DrawBall(rect,r,g,b,width):
    posx, posy = rect.right-8, rect.top-8
    sides = 32
    R = 14
    glBegin(GL_POLYGON)
    glColor(r, g, b)
    for i in range(32):
        x = width * cos(i * 2 * pi / sides) + posx
        y = R * sin(i * 2 * pi / sides) + posy
        glVertex(x, y)
    glEnd()

def drawText(string, x, y):
    glLineWidth(2)
    glColor(0, 0, 1)
    glLoadIdentity()
    glTranslate(x, y, 0)
    glScale(0.13, 0.13, 1)
    string = string.encode()
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def drawEndText(string, x, y):
    glLineWidth(2.5)
    glColor(1, 1, 1)
    glLoadIdentity()
    glTranslate(x, y, 0)
    glScale(0.15, 0.15, 1)
    string = string.encode()
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, c)

def ball_wall(ball, wall):  # Collision Detection between Ball and Wall
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM

    # print(ball.right)

    if ball.right >= wall.right-14:
        return FROM_RIGHT
    if ball.left <= wall.left+14:
        return FROM_LEFT
    if ball.top >= wall.top-14:
        return FROM_TOP
    if ball.bottom <= wall.bottom:
        return FROM_BOTTOM

def ball_paddle(ball, player):  # Collision Detection between Ball and Bat
    if ball.bottom <= player.top and ball.left >= player.left and ball.right <= player.right:
        return True
    return False

exit = False
made = -10
by = -40
Nurul = -90
Yasmine = -160
BS18110359 = -230
HS09 = -300
SC22403 = -420

def keyboard(key, x, y):
    global pause
    global Lives
    global exit
    global score
    if key == b"q":
        exit = True
    elif key == b" ":
        pause = not pause
    elif key == b"p":
        glClearColor(0, 0, 0, 1)
        exit = False
        score=0
        Lives = 3
        defaultVlaues()
mouse_x = 0
def MouseMotion(x, y):
    global mouse_x
    mouse_x = x
def Timer(v):
    Display()

    glutTimerFunc(time_interval, Timer, 1)

Lives = 3
pause = True
score= 0
move=0
def Display():
    global score
    global Lives
    global playerResult
    global FROM_RIGHT
    global FROM_LEFT
    global FROM_TOP
    global FROM_BOTTOM
    global deltaX
    global deltaY
    global pause
    global blocList
    global made
    global by
    global Nurul
    global Yasmine
    global BS18110359
    global HS09
    global SC22403
    global move
    global sidesList




    if (Lives > 0 and exit == False):
        glClear(GL_COLOR_BUFFER_BIT)


        if (pause and Lives>0):
            string = "p r e s s  s p a c e  t o  p l a y  ' q '  t o  e x i t"
            drawText(string, 80, 150)
        DrawRectangle(BLOCK(0,WINDOW_HEIGHT-14,WINDOW_WIDTH,WINDOW_HEIGHT),0,1,0)
        DrawRectangle(BLOCK(0,WINDOW_HEIGHT-120,14,WINDOW_HEIGHT-10),0,1,0)
        DrawRectangle(BLOCK(WINDOW_WIDTH-14,WINDOW_HEIGHT-120,WINDOW_WIDTH,WINDOW_HEIGHT-10),0,1,0)
        DrawRectangle(BLOCK(0, WINDOW_HEIGHT - 240, 14, WINDOW_HEIGHT - 120), 1, 1, 0)
        DrawRectangle(BLOCK(WINDOW_WIDTH-14,WINDOW_HEIGHT-240,WINDOW_WIDTH,WINDOW_HEIGHT-120),1,1,0)
        DrawRectangle(BLOCK(0, WINDOW_HEIGHT - 360, 14, WINDOW_HEIGHT - 240), 1, 0.5, 0)
        DrawRectangle(BLOCK(WINDOW_WIDTH - 14, WINDOW_HEIGHT - 360, WINDOW_WIDTH, WINDOW_HEIGHT - 240), 1, 0.5, 0)
        DrawRectangle(BLOCK(0, WINDOW_HEIGHT - 490, 14, WINDOW_HEIGHT - 360), 1, 0, 0)
        DrawRectangle(BLOCK(WINDOW_WIDTH - 14, WINDOW_HEIGHT - 490, WINDOW_WIDTH, WINDOW_HEIGHT - 360), 1, 0, 0)
        DrawRectangle(BLOCK(0, 0, 14, 10), 0, 1, 0)
        DrawRectangle(BLOCK(WINDOW_WIDTH - 14, 0 , WINDOW_WIDTH, 10), 0, 1, 0)
        for x in blockList:
            r = 0
            g = 1
            b = 0
            if (x.bottom <= WINDOW_HEIGHT - 120 and x.bottom > WINDOW_HEIGHT - 240):
                r = 1
                g = 1
                b = 0
            elif (x.bottom <= WINDOW_HEIGHT - 240 and x.bottom > WINDOW_HEIGHT - 360):
                r = 1
                g = 0.5
                b = 0
            elif (x.bottom <= WINDOW_HEIGHT - 360 and x.bottom > WINDOW_HEIGHT - 490):
                r = 1
                g = 0
                b = 0

            DrawPolygon(x, r, g, b)

        if (pause == False):

            move += 10
            if (move % 300 == 0):
                for x in blockList:
                    x.bottom -= 1
                    x.top -= 1
                for x in sidesList:
                    x.bottom-=1
                    x.top-=1
            ball.left = ball.left + deltaX
            ball.right = ball.right + deltaX
            ball.top = ball.top + deltaY
            ball.bottom = ball.bottom + deltaY
            if ball_paddle(ball, Stick) == True:
                if (Stick.right - 50 < ball.left):
                    deltaY = 1
                    deltaX = 1
                else:
                    deltaY = 1
                    deltaX = -1

            if ball_wall(ball, border) == FROM_RIGHT:
                deltaX = -1

            if ball_wall(ball, border) == FROM_LEFT:
                deltaX = 1

            if ball_wall(ball, border) == FROM_TOP:
                deltaY = -1

            if ball_wall(ball, border) == FROM_BOTTOM:
                crash.set_volume(4)
                crash.play()
                deltaY = 1
                Lives = Lives - 1
            for x in blockList:
                if (x.left == 0):
                    score += 1
                    x.left = -10
                elif(x.right==-5):
                    score-=1
                    x.right=-4
                if(x.bottom==Stick.top):
                    x.bottom=-5
                    x.top=-5
                    x.left=-5
                    x.right=-5

        for x in blockList:

            if (((ball.top == x.bottom or ball.bottom == x.top) and (
                    (ball.right >= x.left and ball.right <= x.right) or (
                    ball.left <= x.right and ball.left >= x.left))) or ((
                    (ball.right == x.left or ball.left == x.right) and (
                    (ball.top >= x.bottom and ball.top <= x.top) or (
                    ball.bottom >= x.bottom and ball.bottom <= x.top))))):
                tick.set_volume(4)
                tick.play()
                if (ball.top == x.bottom):
                    deltaY = -1
                elif (ball.right == x.left):
                    deltaX = -1
                elif (ball.left == x.right):
                    deltaX = 1
                else:
                    deltaY = 1
                x.left = 0
                x.bottom = 0
                x.top = 0
                x.right = 0

        glColor(0, 1, 0)

        DrawBall(ball,0,1,0,14)

        # print(Test_Ball_Wall(ball,wall))


        Stick.left = mouse_x - 50
        Stick.right = mouse_x + 50
        if Stick.left <= 14:
            Stick.left = 14
            Stick.right = 114
        if Stick.right >= WINDOW_WIDTH-14:
            Stick.right = WINDOW_WIDTH-14
            Stick.left = WINDOW_WIDTH - 114
        DrawRectangle(Stick,0,1,0)

        string = "Lives : " + str(Lives)
        drawText(string, 700, 20)
        string = "Score : " + str(score)
        drawText(string, 700, 50)
        glutSwapBuffers()
        i=0
        for x in blockList:
            if(x.left>0):
                i+=1;
        if(i==0):
            glClearColor(0, 1, 0, 1)
            glClear(GL_COLOR_BUFFER_BIT)
            string = "p r e s s  ' p '  t o  p l a y  a g a i n "
            drawText(string, 200, 200)
            string = "N i c e  W O R K "
            drawText(string, 320, 300)
            glutSwapBuffers()
    elif (Lives == 0 and exit == False):
        glClearColor(1, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        string = "p r e s s  ' p '  t o  p l a y  a g a i n "
        drawText(string, 200, 200)
        string = "G A M E  O V E R "
        drawText(string, 320, 300)
        glutSwapBuffers()


    else:
        if (SC22403 < 500):
            glClearColor(0, 0, 0, 1)
            glClear(GL_COLOR_BUFFER_BIT)
            string = "M a d e  "
            drawEndText(string, 250, made)
            string = "B y "
            drawEndText(string, 380, by)
            string = "N u r u l "
            drawEndText(string, 290, Nurul)
            string = "Y a s m i n e "
            drawEndText(string, 290, Yasmine)
            string = "B S 1 8 1 1 0 3 5 9 "
            drawEndText(string, 290, BS18110359)
            string = "H S 0 9 "
            drawEndText(string, 290, HS09)
            string = "S C 2 2 4 0 3 "
            drawEndText(string, 350, SC22403)
            made += 1
            by += 1
            Nurul += 1
            Yasmine += 1
            BS18110359 += 1
            HS09 += 1
            SC22403 += 1

            glutSwapBuffers()
        else:
            sys.exit(0)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Breakout Ball Game ")
    glutDisplayFunc(Display)
    glutTimerFunc(time_interval, Timer, 1)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(MouseMotion)
    init()
    glutMainLoop()


main()
