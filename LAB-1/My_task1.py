import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

direction=0

bg=0
r=1.0
g=1.0
b=1.0

def house():
    glPointSize(10)
    glColor3f(r,g,b)
    
    glBegin(GL_TRIANGLES) #ceeling/roof
    glVertex2f(0,100)
    glVertex2d(90,0)
    glVertex2d(-90,0)
    glEnd()
    
    
    glBegin(GL_LINES) #pillars
    glColor3f(r,g,b)
    
    glVertex2f(71,0) #rightwall
    glVertex2f(71,-120)
    
    glVertex2f(-71,0) #leftwall
    glVertex2f(-71,-120)
    
    glVertex2f(71,-120) #bottom floor
    glVertex2f(-71,-120)
    
    glEnd()
    
    glBegin(GL_LINES) #enterance
    glColor3f(r,g,b)
    
    glVertex2f(-50,-50) #left
    glVertex2f(-50,-120)
    
    glVertex2f(-10,-50) #right
    glVertex2f(-10,-120)
    
    glVertex2f(-50,-50) #bottom floor
    glVertex2f(-10,-50)
    
    glEnd()
    
    glBegin(GL_POINTS) #door knob
    glVertex2f(-20,-90) 
    glEnd()
    
    
    glBegin(GL_LINES) #window
    glColor3f(r,g,b)
    
    glVertex2f(50,-30) #right 
    glVertex2f(50,-50)
    
    glVertex2f(10,-30) #left
    glVertex2f(10,-50)
    
    glVertex2f(10,-30) #top
    glVertex2f(50,-30)
    
    glVertex2f(10,-50) #bottom
    glVertex2f(50,-50)
    
    glVertex2f(30,-30) #Crosshair
    glVertex2f(30,-50)
    
    glVertex2f(10,-40) #Crosshair
    glVertex2f(50,-40)   
    glEnd()
    
    
    
    
    
    
    
def rain():
    global direction
    glLineWidth(3)
    glColor3f(0.1,0.8,1)
    
    glBegin(GL_LINES)
    for i in range(400):
        
        x = random.uniform(-500, 500)
        y = random.uniform(-100, 500)
        if -90<x<90:
            y = random.uniform(0, 500)

    
        length = random.uniform(5,10)

        glVertex2f(x, y)
        glVertex2f(x+direction, y+length)
    glEnd()
    

def keyboardListener(key,x,y):
    global bg
    global r
    global g
    global b
    global direction
    
    if key==b'a':
        bg+=0.05
        r-=0.05
        g-=0.05
        b-=0.05
        
        print("Night to day !")
        
    if key==b'f':
        bg-=0.05
        r+=0.05
        g+=0.05
        b+=0.05
        
        print("Day to night !")
        
    if key==b'r':
        bg=0
        r=1.0
        g=1.0
        b=1.0
        direction=0
        
        print("Reset Done !")

    glutPostRedisplay()
    
    
    
    
def specialKeyListener(key,x,y):
    global direction
    
    if key==GLUT_KEY_RIGHT:        
        direction-=1
        print("Going Right")      
        
    if key==GLUT_KEY_LEFT:
        direction+=1
        print("Going Left")


    
def display():
    #//clear the display
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(bg,bg,bg,0);	#//color black
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #//load the correct matrix -- MODEL-VIEW matrix
    glMatrixMode(GL_MODELVIEW)
    #//initialize the matrix
    glLoadIdentity()
    #//now give three info
    #//1. where is the camera (viewer)?
    #//2. where is the camera looking?
    #//3. Which direction is the camera's UP direction?
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)
    
    rain()
    house()
    glutSwapBuffers()

def animate():
    #//codes for any changes in Models, Camera
    glutPostRedisplay()
    
def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance
    
glutInit()
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"Task-1 House in the rain")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animate)	#what you want to do in the idle time (when no drawing is occuring)

glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)


glutMainLoop()		#The main loop of OpenGL

