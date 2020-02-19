import matplotlib.pyplot as plt
import numpy as np
from graphics import *
import random, time
import sys

def draw_all(cordlst,e,win,color):
    #print("dwg")
    obj_list = []
    for i in range(e):
        cir = Circle(Point(cordlst[i,0]+win.getWidth()/2,cordlst[i,1]+win.getHeight()/2),2)
        obj_list.append(cir)
    for i in range(e):
        obj_list[i].setFill(color)
        obj_list[i].draw(win)
    return obj_list

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

# Draw multiple points.
def draw_multiple_points(points = 10):
    win = GraphWin('Fractals',1000,1000,autoflush=False)
    win.setBackground("black")

    seed_X = np.array([0,5])
    seed_y = np.array([0,0])
    obj = np.stack((seed_X, seed_y), axis=1)

    radss = np.pi/2

    rot = np.array([np.cos(radss),np.sin(radss),-np.sin(radss),np.cos(radss)])
    rot = rot.reshape(2,2)

    i = 1
    while i <= points:

        rotated = np.matmul(obj,rot)
        e = int(obj.size/2-1)

        rotated[:,0] = -rotated[:,0] -obj[e,0]
        rotated[:,1] = -rotated[:,1] -obj[e,1]

        obj = np.vstack((obj,rotated))
        #obj = np.unique(obj,axis=1)
        win.update()
        print(i)
        color = color_rgb(random.randrange(256), random.randrange(256), random.randrange(256))
        pts = draw_all(obj,e,win,color)
        #clear(win)
        i += 1

    win.getMouse()
    win.close()
    print("Size is:",e)

if __name__ == '__main__':
        #print(sys.argv)
        if len(sys.argv) > 1:
            draw_multiple_points(points = int(sys.argv[1]))
        else:
            draw_multiple_points()
