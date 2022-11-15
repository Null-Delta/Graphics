from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


# Объявляем все глобальные переменные
global xrot  # Величина вращения по оси x
global yrot  # Величина вращения по оси y
global ambient  # рассеянное освещение
global skincolor  # Цвет
global lightpos  # Положение источника освещения


def drawBody():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, skincolor)
    glTranslatef(0.0, 0.0, -0.3)
    quadratic = gluNewQuadric()
    gluSphere(quadratic, 0.4, 100, 100)

    glTranslatef(0.0, 0.0, 1)
    gluSphere(quadratic, 0.4, 100, 100)
    glTranslatef(0.0, 0.0, -0.5)
    gluCylinder(quadratic, 0.4, 0.4, 1, 100, 100)

    glPopMatrix()

def drawBodyandFace():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.5, 0.4, 0.2, 0.7))
    glTranslatef(0.0, -0.389, 0.2)
    glScale(0.9, 0.27, 1.2)
    quadratic = gluNewQuadric()
    gluSphere(quadratic, 0.3, 100, 100)
    glPopMatrix()

    glPushMatrix()
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.5, 0.4, 0.2, 0.7))
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)

    glTranslatef(0.0, -0.5, 0.8)
    glScale(1.5, 0.35, 1.0)
    quadratic = gluNewQuadric()
    gluSphere(quadratic, 0.45, 100, 100)

    glPopMatrix()

def drawHead():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glScale(1.5, 1.0, 1.0)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, skincolor)
    quadratic = gluNewQuadric()
    glTranslatef(0.0, -0.1, 0.8)
    gluSphere(quadratic, 0.55, 200, 100)

    glPopMatrix()

def drawEars():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glScale(1.5, 0.5, 1.3)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, skincolor)
    quadratic = gluNewQuadric()
    glTranslatef(0.6, -0.1, 0.6)
    gluSphere(quadratic, 0.4, 100, 100)

    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glScale(1.5, 0.5, 1.3)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, skincolor)
    quadratic = gluNewQuadric()
    glTranslatef(-0.6, -0.1, 0.6)
    gluSphere(quadratic, 0.4, 100, 100)

    glPopMatrix()

def drawHands():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glScale(0.6, 0.4, 1.1)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, skincolor)
    quadratic = gluNewQuadric()
    glTranslatef(0.6, -1.0, 0.1)
    gluSphere(quadratic, 0.3, 100, 50)

    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glScale(0.6, 0.4, 1.1)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, skincolor)
    quadratic = gluNewQuadric()
    glTranslatef(-0.6, -1.0, 0.1)
    gluSphere(quadratic, 0.3, 100, 50)

    glPopMatrix()

def drawLegs():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glScale(0.8, 0.6, 0.5)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, skincolor)
    quadratic = gluNewQuadric()
    glTranslatef(0.6, -0.1, -1.4)
    gluSphere(quadratic, 0.3, 100, 50)

    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glScale(0.8, 0.6, 0.5)

    glMaterialfv(GL_FRONT, GL_DIFFUSE, skincolor)
    quadratic = gluNewQuadric()
    glTranslatef(-0.6, -0.1, -1.4)
    gluSphere(quadratic, 0.3, 100, 50)

    glPopMatrix()


def drawEyes():


    ##########################

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1, 1))
    quadratic = gluNewQuadric()
    glTranslatef(0.25, -0.6, 0.8)
    gluSphere(quadratic, 0.15, 100, 100)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 1, 1, 1))
    quadratic = gluNewQuadric()
    glTranslatef(-0.25, -0.6, 0.8)
    gluSphere(quadratic, 0.15, 100, 100)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 0, 0, 1))
    quadratic = gluNewQuadric()
    glTranslatef(0.25, -0.69, 0.8)
    gluSphere(quadratic, 0.09, 100, 100)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 0, 0, 1))
    quadratic = gluNewQuadric()
    glTranslatef(-0.25, -0.69, 0.8)
    gluSphere(quadratic, 0.09, 100, 100)

    glPopMatrix()


def drawMounth():
    glPushMatrix()
    glTranslatef(0, 0.1, 0)
    glRotatef(xrot, 1.0, 0.0, 0.0)
    glRotatef(yrot, 0.0, 1.0, 0.0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, (1, 0, 0.3, 1))
    quadratic = gluNewQuadric()
    glTranslatef(0, -0.6, 0.6)
    gluSphere(quadratic, 0.05, 100, 100)
    glPopMatrix()


# Процедура инициализации
def init():
    global xrot  # Величина вращения по оси x
    global yrot  # Величина вращения по оси y
    global ambient  # Рассеянное освещение
    global skincolor  # Цвет елочного ствола
    global lightpos  # Положение источника освещения

    xrot = 0.0  # Величина вращения по оси x = 0
    yrot = 0.0  # Величина вращения по оси y = 0
    ambient = (1.0, 1.0, 1.0, 0.7)  # Первые три числа цвет в формате RGB, а последнее - яркость
    skincolor = (0.2, 0.1, 0.03, 0.7)  # цвет
    lightpos = (2, -2, 0)  # Положение источника освещения по осям xyz

    glClearColor(0.5, 0.5, 0.5, 1.0)  # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.5, 1.5, -1.5, 1.5)  # Определяем границы рисования по горизонтали и вертикали
    glRotatef(-90, 10.0, 0.0, 0.0)  # Сместимся по оси Х на 90 градусов
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)  # Определяем текущую модель освещения
    glEnable(GL_LIGHTING)  # Включаем освещение
    glEnable(GL_LIGHT0)  # Включаем один источник света
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Определяем положение источника света
    glEnable(GL_DEPTH_TEST)


# Процедура обработки специальных клавиш
def specialkeys(key, x, y):
    global xrot
    global yrot
    # Обработчики для клавиш со стрелками
    if key == GLUT_KEY_UP:  # Клавиша вверх
        xrot -= 4.0  # Уменьшаем угол вращения по оси Х
    if key == GLUT_KEY_DOWN:  # Клавиша вниз
        xrot += 4.0  # Увеличиваем угол вращения по оси Х
    if key == GLUT_KEY_LEFT:  # Клавиша влево
        yrot -= 4.0  # Уменьшаем угол вращения по оси Y
    if key == GLUT_KEY_RIGHT:  # Клавиша вправо
        yrot += 4.0  # Увеличиваем угол вращения по оси Y

    glutPostRedisplay()  # Вызываем процедуру перерисовки


# Процедура перерисовки
def draw():
    global xrot
    global yrot
    global lightpos
    global greencolor
    global skincolor

    # glClear(GL_COLOR_BUFFER_BIT)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)  # Источник света

    drawBody()
    drawHead()
    drawHands()
    drawBodyandFace()
    drawEyes()
    drawMounth()
    drawLegs()
    drawEars()
    glutSwapBuffers()  # Выводим все нарисованное в памяти на экран


# Здесь начинается выполнение программы
# Использовать двойную буферизацию и цвета в формате RGB (Красный, Зеленый, Синий)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
# Указываем начальный размер окна (ширина, высота)
glutInitWindowSize(400, 400)
# Указываем начальное положение окна относительно левого верхнего угла экрана
glutInitWindowPosition(40, 30)
# Инициализация OpenGl
glutInit(sys.argv)
# Создаем окно с заголовком "Happy New Year!"
glutCreateWindow(b"Cheburashka")
# Определяем процедуру, отвечающую за перерисовку
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку клавиш
glutSpecialFunc(specialkeys)

# Вызываем нашу функцию инициализации
init()

glScale(0.75, 0.75, 0.75)

# Запускаем основной цикл
glutMainLoop()