import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

data=[]
box_left=0
box_low=0
height=500
width=1000
init_speed=0.04
init_left_mouse=False
left_mouse=None
space=False
color_data=[]

def random_points(x,y):
    if box_left<x<width and box_low<y<height:
        color_data.append([random.random(),random.random(),random.random()])        
        x_dir=random.choice([-1,1])
        y_dir=random.choice([-1,1])
        data.append([x,y,color_data[-1],x_dir,y_dir])
        
    
    

def points():
    global init_left_mouse,space,interval
    glPointSize(10)
    glBegin(GL_POINTS)
    
    for i in range (len(data)):
        x,y,color,dir_x,dir_y=data[i]
        
        if space==True:
            dir_x=0
            dir_y=0
            init_left_mouse=False
            
        if init_left_mouse==True and space==False:
            time=glutGet(GLUT_ELAPSED_TIME)//1000
            if time%2==0:
                glColor3f(0,0,0)
            else:
                glColor3f(color[0],color[1],color[2])
        else:
            glColor3f(color[0],color[1],color[2])
                
            
        
        glVertex2f(x,y)
        
        x+=dir_x*init_speed  #updating the direction 
        y+=dir_y*init_speed

        #Boundary corner case
        if x<box_left+10:
            x=box_left+10
            dir_x=-dir_x

        if x>width-10:
            x=width-10
            dir_x=-dir_x

        if y<box_low+10:
            y=box_low+10
            dir_y=-dir_y

        if y>height-10:
            y=height-10
            dir_y=-dir_y
        data[i]=[x,y,color,dir_x,dir_y]
    glEnd()
    
    
    
    

def mouseListener(button,state,x,y):
    global space,height,init_left_mouse
    if space==True:
        return       #If the spacebar is true the function will exit here 
    
    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        if init_left_mouse==False:
            init_left_mouse= True
            print("Blinking started")
            
        elif init_left_mouse==True:
            init_left_mouse=False
            print("Blinking stopped")
    if button==GLUT_RIGHT_BUTTON and state==GLUT_DOWN:
        random_points(x,height-y)
        print("Random points added")
    glutPostRedisplay()
        
            
        
        
    
    


def specialKeyListener(key, x, y):
    global init_speed 
    
    if key==GLUT_KEY_DOWN:
        if init_speed==0 or init_speed<0:
            print("This is the lowest speed!")
            init_speed=0
        else:
                init_speed-=0.01
                print("Lowering Speed")
    
    if key==GLUT_KEY_UP:        
        init_speed+=0.01
        print("Increasing speed")

    glutPostRedisplay()
        
def keyboardListener(key,x,y):
    
    if key == b' ':
        global space
        space = not space
        if space == True:
            global init_left_mouse,left_mouse
            left_mouse=init_left_mouse
            left_mouse=False
            for i in range (len(data)):
                x,y,color,dir_x,dir_y=data[i]
                new_x=0
                new_y=0
                data[i]=[x,y,color,new_x,new_y]
            print("Paused")
            
            
        else:
            init_left_mouse=left_mouse
            left_mouse=None
            for i in range (len(data)):
                x,y,color,dir_x,dir_y=data[i]

                new_x=random.choice([-1,1])
                new_y=random.choice([-1,1])
                data[i]=[x,y,color,new_x,new_y]
            print("Resumed")
    elif key == b'r':
        global init_speed
        init_speed=0.04
        init_left_mouse=False
        left_mouse=None

    glutPostRedisplay()
    
    
  
#Driver code from here 
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)  # Use orthographic projection for 2D
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Draw the initial box
    glLineWidth(1)
    glBegin(GL_LINES)
    
    glVertex2f(width, height)     # Upper Boundary
    glVertex2f(box_left, height)
    
    glVertex2f(box_left, height)  # Left Boundary
    glVertex2f(box_left, box_low)
    
    glVertex2f(width, box_low)    # Lower Boundary
    glVertex2f(box_left, box_low)
    
    glVertex2f(width, box_low)    # Right Boundary
    glVertex2f(width, height)
    
    glEnd()
    points()
    
    glutSwapBuffers()

def animate():    
    glutPostRedisplay()

def init():
    glClearColor(0, 0, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)  # Set orthographic projection for 2D
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

glutInit()
glutInitWindowSize(width, height)
glutInitWindowPosition(10, 10)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) # Depth, Double buffer, RGB color

wind = glutCreateWindow(b"Random Shooter Balls")
init()

glutDisplayFunc(display)  # Display callback function
glutIdleFunc(animate)    # Update function for animation
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutMainLoop()  # The main loop of OpenGL
