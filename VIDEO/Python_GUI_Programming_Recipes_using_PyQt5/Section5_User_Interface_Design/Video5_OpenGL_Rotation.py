'''
Created on Sep 26, 2017
Some of the code in this module was inspired by the official PyQt "Hello GL" example
@author: Burkhard A. Meier
'''

import sys
from OpenGL.GL import *
from PyQt5.QtWidgets import QOpenGLWidget, QApplication
from PyQt5.QtCore import pyqtSignal, QPoint, Qt


class PyQtOpenGL(QOpenGLWidget):
    # rotation signals mouse movement
    x_rotation_changed = pyqtSignal(int)
    y_rotation_changed = pyqtSignal(int)
    z_rotation_changed = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.paint_0 = True
        self.paint_1 = True
        self.paint_2 = True
        self.resize_lines = True    # set orthographic matrix multiplier to large/small
#         self.resize_lines = False
        
        self.paint_rotation = True
#         self.paint_rotation = False
        self.x_rotation = 0         # rotation variables
        self.y_rotation = 0
        self.z_rotation = 0

        self.last_pos = QPoint()

    def normalize_angle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle
    
    # slots for xyz-rotation 
    def set_x_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.x_rotation:
            self.x_rotation = angle
            self.x_rotation_changed.emit(angle)
            self.update()

    def set_y_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.y_rotation:
            self.y_rotation = angle
            self.y_rotation_changed.emit(angle)
            self.update()

    def set_z_rotation(self, angle):
        angle = self.normalize_angle(angle)
        if angle != self.z_rotation:
            self.z_rotation = angle
            self.z_rotation_changed.emit(angle)
            self.update()
            
    def initializeGL(self):
        # reimplemented
        glClearColor(0.0, 0.0, 1.0, 0.0)    # blue
        
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)  
        
        lightPosition = [0, 0, 10, 1.0]  
        glLightfv(GL_LIGHT0, GL_POSITION, lightPosition) 

    def paintGL(self):
        # reimplemented
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -10.0)
        glRotatef(self.x_rotation / 16.0, 1.0, 0.0, 0.0)
        glRotatef(self.y_rotation / 16.0, 0.0, 1.0, 0.0)
        glRotatef(self.z_rotation / 16.0, 0.0, 0.0, 1.0)
        self.draw()      
   
    def draw(self):
        if self.paint_rotation:
            glColor3f(1.0, 0.0, 0.0)    
            glBegin(GL_QUADS)           # bottom of pyramid
            glNormal3f(0, 0, -1)
            glVertex3f(-1 ,-1, 0)
            glVertex3f(-1 ,1, 0)
            glVertex3f(1, 1, 0)
            glVertex3f(1, -1, 0)
            glEnd()
            
            glColor3f(0.0, 0.0, 0.0)
            glBegin(GL_TRIANGLES)       # four sides of pyramid
            glNormal3f(0, -1, 0.707)
            glVertex3f(-1, -1, 0)
            glVertex3f(1, -1, 0)
            glVertex3f(0, 0, 1.2)
            glEnd()

            glBegin(GL_TRIANGLES)
            glNormal3f(1,0, 0.707)
            glVertex3f(1,-1,0)
            glVertex3f(1,1,0)
            glVertex3f(0,0,1.2)
            glEnd()
            
            glBegin(GL_TRIANGLES)
            glNormal3f(0,1,0.707)
            glVertex3f(1,1,0)
            glVertex3f(-1,1,0)
            glVertex3f(0,0,1.2)
            glEnd()
     
            glBegin(GL_TRIANGLES)
            glNormal3f(-1,0,0.707)
            glVertex3f(-1,1,0)
            glVertex3f(-1,-1,0)
            glVertex3f(0,0,1.2)
            glEnd()   

        # square and lines
        if self.paint_0:       
            glColor3f(1.0, 0.0, 0.0)    # functions expects 3 f(loats); RGB: red
            glRectf(-5, -5, 5, 5)       # draw a filled rectangle with above color, position(x,y) pairs from center of window
  
        if self.paint_1: 
            glColor3f(0.0, 1.0, 0.0)    # set color to RGB: green
            x=10
            y=10
            self.draw_loop(x, y)
         
        if self.paint_2: 
            glColor3f(0.0, 0.0, 0.0)    # set color to RGB: black
            x=5
            y=5
            self.draw_loop(x, y)
        
         
    def resizeGL(self, width, height):
        # reimplemented
        side = min(width, height)
        if side < 0:
            return
  
        glViewport((width - side) // 2, (height - side) // 2, side, side)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        
        if self.resize_lines:
            glOrtho(-50, 50, -50, 50, -50.0, 50.0)  # for square and lines; combined with pyramid
        else:
            glOrtho(-2, +2, -2, +2, 1.0, 15.0)      # original pyramid setting
            
        glMatrixMode(GL_MODELVIEW)            
                
                
    def draw_loop(self, x, y, incr=10):
        for _ in range(5):
            self.draw_square_lines(x, y)
            x += incr
            y += incr

    def draw_square_lines(self, x=10, y=10, z=0):
        glBegin(GL_LINES)         # begin to draw a line
        glVertex3f(x, y, z)       # start line relative to center of window
        glVertex3f(x, -y, z)      # draw first line
         
        glVertex3f(x, -y, z)
        glVertex3f(-x, -y, z)
         
        glVertex3f(-x, -y, z)
        glVertex3f(-x, y, z)
         
        glVertex3f(-x, y, z)
        glVertex3f(x, y, z)
        glEnd()      


    def mousePressEvent(self, event):
        # reimplemented
        self.last_pos = event.pos()

    def mouseMoveEvent(self, event):
        # reimplemented
        move_x = event.x() - self.last_pos.x()
        move_y = event.y() - self.last_pos.y()

        if event.buttons() & Qt.LeftButton:                     # left mouse button
            self.set_x_rotation(self.x_rotation + 8 * move_y)
            self.set_y_rotation(self.y_rotation + 8 * move_x)
            
        elif event.buttons() & Qt.RightButton:                  # right mouse button 
            self.set_x_rotation(self.x_rotation + 8 * move_y)
            self.set_z_rotation(self.z_rotation + 8 * move_x)   # spin pyramid around itself

        self.last_pos = event.pos()     
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = PyQtOpenGL()
    widget.show()
    app.exec_()