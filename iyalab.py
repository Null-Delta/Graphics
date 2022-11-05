from tokenize import Double
import pygame as pygame
import random as random
import numpy as np

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class point:
    x: float
    y: float
    z: float
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
def triangle(h: float, k: float, offset: float, scale: float):
    d = 2 * k * scale
    
    glColor3fv((1,1,1))
    glBegin(GL_TRIANGLES)
    glVertex3f(0, offset * scale, 0)
    glVertex3f(k * scale, (offset - h) * scale, 0)
    glVertex3f(-k * scale, (offset - h) * scale, 0)
    glEnd()
    
    glBegin(GL_TRIANGLES)
    glVertex3f(0, offset * scale, -d)
    glVertex3f(k * scale, (offset - h) * scale, -d)
    glVertex3f(-k * scale, (offset - h) * scale, -d)
    glEnd()
    
    glColor3fv((0.75,0.75,0.75))
    glBegin(GL_QUADS)
    glVertex3f(-k * scale, (offset - h) * scale, 0)
    glVertex3f(k * scale, (offset - h) * scale, 0)
    glVertex3f(k * scale, (offset - h) * scale, -d)
    glVertex3f(-k * scale, (offset - h) * scale, -d)
    glEnd()
    
    glBegin(GL_QUADS)
    glVertex3f(k * scale, (offset - h) * scale, 0)
    glVertex3f(0, offset * scale, 0)
    glVertex3f(0, offset * scale, -d)
    glVertex3f(k * scale, (offset - h) * scale, -d)
    glEnd()
    
    glBegin(GL_QUADS)
    glVertex3f(-k * scale, (offset - h) * scale, 0)
    glVertex3f(0, offset * scale, 0)
    glVertex3f(0, offset * scale, -d)
    glVertex3f(-k * scale, (offset - h) * scale, -d)
    glEnd()
      
def main():
    scale = 1.0 / 16.0

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), scale * 2, 100)
    
    glTranslatef(scale * -2.5,scale * -2.5, -2)
    glEnable(GL_DEPTH_TEST)

    while True:        
        keys=pygame.key.get_pressed()
        
        glTranslatef(scale * 2.5,scale * 2.5, 0)
        if keys[K_LEFT]:
            glRotate(-0.2, 0, 0, 1)
        if keys[K_RIGHT]:
            glRotate(0.2, 0, 0, 1)
        if keys[K_UP]:
            glRotate(-0.2, 1, 0, 0)
        if keys[K_DOWN]:
            glRotate(0.2, 1, 0, 0)
        if keys[K_a]:
            glRotate(-0.2, 0, 1, 0)
        if keys[K_d]:
            glRotate(0.2, 0, 1, 0)
        glTranslatef(scale * -2.5,scale * -2.5, 0)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        glRotate(0, 0, 0, 0)
        glColor3fv((1,1,1))

        
        triangle(1, 1, 0, 0.1)
        triangle(1, 1, 0.75, 0.1)
        triangle(1, 1, 1.5, 0.1)

        pygame.display.flip()
        pygame.time.wait(1)
main()