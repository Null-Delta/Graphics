from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

global time
 
def init():
    global time
    time = 0

    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.5, 1.5, -1.5, 1.5)
    glRotatef(-90, 1.0, 0.0, 0.0)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, (1.0, 0.0, 0.5, 1))
    glLightfv(GL_LIGHT0, GL_POSITION, (-2, -2, 2))
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glScaled(0.5, 0.5, 0.5)
    glLineWidth(3)

    glEnable(GL_FOG)
    glFogfv(GL_FOG_COLOR, (0.0, 0.0, 0.0, 1.0))
    glFogf(GL_FOG_START, 1)
    glFogf(GL_FOG_END, 0)
    glFogi(GL_FOG_MODE, GL_LINEAR)

def draw():
    global time
    time += 0.1
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glFogf(GL_FOG_END, ( (math.cos(time / 5)) - 0.5))

    glPushMatrix()
    glRotate(time * 2, 1, 0.5, 0.25)
    glutWireDodecahedron()
    glPopMatrix()       
    glutSwapBuffers()

def redraw():
    glutPostRedisplay()


glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(300, 300)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"Chillipizdrik")
glutDisplayFunc(draw)
glutIdleFunc(redraw)
init()
glutMainLoop()