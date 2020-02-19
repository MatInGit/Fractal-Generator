import matplotlib.pyplot as plt
import numpy as np
import sys


# Draw multiple points.
def draw_multiple_points(points = 15):

    seed_X = np.array([0,1])
    seed_y = np.array([0,0])
    obj = np.stack((seed_X, seed_y), axis=1)

    radss = np.pi/2

    rot = np.array([np.cos(radss),np.sin(radss),-np.sin(radss),np.cos(radss)])
    rot = rot.reshape(2,2)


    i = 1
    #Change this value to generate bigger fractals
    while i <= points:
        #radss = -radss
        #rot = np.array([np.cos(radss),np.sin(radss),-np.sin(radss),np.cos(radss)])
        #rot = rot.reshape(2,2)

        rotated = np.matmul(obj,rot)
        e = int(obj.size/2-1)
        #print(e)
        rotated[:,0] = -rotated[:,0] -obj[e,0]
        rotated[:,1] = -rotated[:,1] -obj[e,1]

        obj = np.vstack((obj,rotated))
        obj = np.unique(obj,axis=1)

        # Draw point based on above x, y axis values.

        i += 1
        print(i)
    print("Size is:",e)
    plt.title("Fractal")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.scatter(obj[:,0],obj[:,1],s=0.1)
    plt.draw()
    plt.show()


if __name__ == '__main__':
    #print(sys.argv)
    if len(sys.argv) > 1:
        draw_multiple_points(points = int(sys.argv[1]))
    else:
        draw_multiple_points()
