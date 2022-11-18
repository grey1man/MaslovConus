import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from threading import Thread

class Drawer():
    display = None
    tick_time = None
    objectToDraw = None

    def __init__(self, display = (800, 600), fps = 30, objectToDraw = None):
        self.display = display
        self.tick_time = round(1000 / fps)
        self.objectToDraw = objectToDraw
    
    def setObjectToDraw(self, objectToDraw):
        self.objectToDraw = objectToDraw
    
    def start(self):
        DrawerThread = Thread(target=self.run)
        DrawerThread.start()
    
    def draw(self):
        glBegin(GL_LINES)
        for edge in self.objectToDraw.edges:
            for vertex in edge:
                glVertex3fv(self.objectToDraw.verticies[vertex])
        glEnd()

    def run(self):    
        pygame.init()

        smallfont = pygame.font.SysFont(None, 35)
        screen = pygame.display.set_mode(self.display, DOUBLEBUF|OPENGL)
        
        gluPerspective(45, (self.display[0]/self.display[1]), 0.1, 50.0)
        glTranslatef(0.0,0.0, -5)
        mouseCoordsHook = [self.display[0] / 2, self.display[1] / 2]
        while True:
            screen.fill((60,25,60))
            mouseCoords = pygame.mouse.get_pos()
            mousePressed = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                mouseCoordsHook = pygame.mouse.get_pos()
                if mousePressed[0]:
                    for vertex in self.objectToDraw.verticies:
                        vertex[0] += (mouseCoordsHook[0] - mouseCoords[0]) / 400
                        vertex[1] += (mouseCoords[1] - mouseCoordsHook[1]) / 300
                        print(vertex[0])
                    
                        

            

            #glRotatef(1, 3, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            if (self.objectToDraw != None):
                self.draw()
    
            pygame.display.flip()
            pygame.time.wait(self.tick_time)