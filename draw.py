from tkinter import *
import time
from PIL import Image, ImageDraw


def num_to_range(num, inMin, inMax, outMin, outMax):
    return outMin + (float(num - inMin) / float(inMax - inMin) * (outMax- outMin))


WIDTH, HEIGHT = 1000, 1000
# set width and height of canvas to be 500

CENTER = WIDTH // 2
# set the center of the canvas to be half of the width


class canvasGUI:
    def __init__(self):
        self.root = Tk()
        # the root is the gui app
        self.root.title("Mage Canvas")

        self.current_color = "#000000"
        # set default brush size and width
        self.cnv = Canvas(self.root, width=WIDTH-10,height=HEIGHT-10, bg='white',)
        # now create canvas. set width and height, background and make the self.root area the are you can draw

        self.cnv.pack()
        # fits the canvas widget within the main app window
        self.x_min,self.y_min = 1000, 1000
        self.x_max ,self.y_max = 0, 0

        self.prev_x, self.prev_y = None, None  # To keep track of the previous point

        self.cnv.bind("<B1-Motion>", self.paint)
        self.cnv.bind("<ButtonRelease-1>", self.reset)

        # binds an event handler to canvas widget
        # refers to motion of the mouse while the left button is held down
        # calls the paint function
        # on release clears previous points and resets

        self.root.mainloop()

    def paint(self, event):
        x, y = event.x, event.y

        if self.prev_x and self.prev_y:
            if x > self.x_max:
                self.x_max = x
            if x< self.x_min:
                self.x_min = x
            if y > self.y_max:
                self.y_max = y
            if y< self.y_min:
                self.y_min = y
            
            # check the x and y value to see if it adjusts the bounding box

            distance = ((x - self.prev_x) ** 2 + (y - self.prev_y) ** 2) ** 0.5
            distance = num_to_range(distance,0,300,3,15)

            # create a distance function and map it to a width for the brush
            self.cnv.create_line(self.prev_x, self.prev_y, x, y, fill="black",width=distance, smooth=1,splinesteps=1, joinstyle=BEVEL, capstyle=ROUND)
        
        self.prev_x, self.prev_y = x, y
        # set previous points to current points


    def reset(self, event):
        self.cnv.create_rectangle(self.x_min,self.y_min,self.x_max,self.y_max, outline='black')
        self.prev_x, self.prev_y = None, None
        self.x_max ,self.y_max = 0, 0
        self.x_min,self.y_min = WIDTH, HEIGHT

        # draw bounding box around drawing, and reset all the values





canvasGUI()
