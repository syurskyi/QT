'''
Created on Sep 23, 2017

@author: Burkhard A. Meier
'''

import sys
from OpenGL.GL import *
from PyQt5.QtWidgets import QOpenGLWidget, QApplication


class PyQtOpenGL(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.paint_0 = False        # control what gets painted
        self.paint_1 = False
        self.paint_2 = False


    def initializeGL(self):                 # This virtual function is called once before the first call to paintGL() or resizeGL(). Reimplement it in a subclass.
        glClearColor(0.0, 0.0, 1.0, 0.0)    # RGBA: R=0.0, G=0.0, B=1.0  => becomes Blue
        glClear(GL_COLOR_BUFFER_BIT)        # clear color buffer and set window with color defined above

    def resizeGL(self, w, h):                   # called when window gets resized (also when it first appears)
        glMatrixMode(GL_PROJECTION)             # define the viewing volume
        glLoadIdentity()                        # reset coordinate system
        glOrtho(-50, 50, -50, 50, -50.0, 50.0)  # multiply the current matrix with an orthographic matrix
                                                # ( left , right , bottom , top , zNear , zFar )
        glViewport(0, 0, w, h)                  # set Viewport to Window dimensions
        
    def paintGL(self):                  # This virtual function is called whenever the widget needs to be painted. Reimplement it in a subclass.
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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = PyQtOpenGL()
    widget.show()
    app.exec_()