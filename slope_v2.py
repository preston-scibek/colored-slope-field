from __future__ import division
from math import *
import turtle
side = 2000
interval = side / 10
step = interval
enlarge = 30
prestons_turtle = turtle
prestons_turtle.setup(side, side)
prestons_turtle.Screen()
prestons_turtle.showturtle()
prestons_turtle.mode("standard")
line_seg = 10
prestons_turtle.speed(999999999999)
points = [
	(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10),
	(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10),
	(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10),
	(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10),
	(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10),
	(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10),
	(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10),
	(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10),
	(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10),
	(9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10),
	(10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10),
	(-1, 0), (-1, 1), (-1, 2), (-1, 3), (-1, 4), (-1, 5), (-1, 6), (-1, 7), (-1, 8), (-1, 9), (-1, 10),
	(-2, 0), (-2, 1), (-2, 2), (-2, 3), (-2, 4), (-2, 5), (-2, 6), (-2, 7), (-2, 8), (-2, 9), (-2, 10),
	(-3, 0), (-3, 1), (-3, 2), (-3, 3), (-3, 4), (-3, 5), (-3, 6), (-3, 7), (-3, 8), (-3, 9), (-3, 10),
	(-4, 0), (-4, 1), (-4, 2), (-4, 3), (-4, 4), (-4, 5), (-4, 6), (-4, 7), (-4, 8), (-4, 9), (-4, 10),
	(-5, 0), (-5, 1), (-5, 2), (-5, 3), (-5, 4), (-5, 5), (-5, 6), (-5, 7), (-5, 8), (-5, 9), (-5, 10),
	(-6, 0), (-6, 1), (-6, 2), (-6, 3), (-6, 4), (-6, 5), (-6, 6), (-6, 7), (-6, 8), (-6, 9), (-6, 10),
	(-7, 0), (-7, 1), (-7, 2), (-7, 3), (-7, 4), (-7, 5), (-7, 6), (-7, 7), (-7, 8), (-7, 9), (-7, 10),
	(-8, 0), (-8, 1), (-8, 2), (-8, 3), (-8, 4), (-8, 5), (-8, 6), (-8, 7), (-8, 8), (-8, 9), (-8, 10),
	(-9, 0), (-9, 1), (-9, 2), (-9, 3), (-9, 4), (-9, 5), (-9, 6), (-9, 7), (-9, 8), (-9, 9), (-9, 10),
	(-10, 0), (-10, 1), (-10, 2), (-10, 3), (-10, 4), (-10, 5), (-10, 6), (-10, 7), (-10, 8), (-10, 9), (-10, 10),
	(0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7), (0, -8), (0, -9), (0, -10),
	(1, -1), (1, -2), (1, -3), (1, -4), (1, -5), (1, -6), (1, -7), (1, -8), (1, -9), (1, -10),
	 (2, -1), (2, -2), (2, -3), (2, -4), (2, -5), (2, -6), (2, -7), (2, -8), (2, -9), (2, -10),
	(3, -1), (3, -2), (3, -3), (3, -4), (3, -5), (3, -6), (3, -7), (3, -8), (3, -9), (3, -10),
	 (4, -1), (4, -2), (4, -3), (4, -4), (4, -5), (4, -6), (4, -7), (4, -8), (4, -9), (4, -10),
	(5, -1), (5, -2), (5, -3), (5, -4), (5, -5), (5, -6), (5, -7), (5, -8), (5, -9), (5, -10),
	(6, -1), (6, -2), (6, -3), (6, -4), (6, -5), (6, -6), (6, -7), (6, -8), (6, -9), (6, -10),
	 (7, -1), (7, -2), (7, -3), (7, -4), (7, -5), (7, -6), (7, -7), (7, -8), (7, -9), (7, -10),
	 (8, -1), (8, -2), (8, -3), (8, -4), (8, -5), (8, -6), (8, -7), (8, -8), (8, -9), (8, -10),
	(9, -1), (9, -2), (9, -3), (9, -4), (9, -5), (9, -6), (9, -7), (9, -8), (9, -9), (9, -10),
	 (10, -1), (10, -2), (10, -3), (10, -4), (10, -5), (10, -6), (10, -7), (10, -8), (10, -9), (10, -10),
	(-1, -1), (-1, -2), (-1, -3), (-1, -4), (-1, -5), (-1, -6), (-1, -7), (-1, -8), (-1, -9), (-1, -10),
	 (-2, -1), (-2, -2), (-2, -3), (-2, -4), (-2, -5), (-2, -6), (-2, -7), (-2, -8), (-2, -9), (-2, -10),
	(-3, -1), (-3, -2), (-3, -3), (-3, -4), (-3, -5), (-3, -6), (-3, -7), (-3, -8), (-3, -9), (-3, -10),
	(-4, -1), (-4, -2), (-4, -3), (-4, -4), (-4, -5), (-4, -6), (-4, -7), (-4, -8), (-4, -9), (-4, -10),
	 (-5, -1), (-5, -2), (-5, -3), (-5, -4), (-5, -5), (-5, -6), (-5, -7), (-5, -8), (-5, -9), (-5, -10),
	 (-6, -1), (-6, -2), (-6, -3), (-6, -4), (-6, -5), (-6, -6), (-6, -7), (-6, -8), (-6, -9), (-6, -10),
	(-7, -1), (-7, -2), (-7, -3), (-7, -4), (-7, -5), (-7, -6), (-7, -7), (-7, -8), (-7, -9), (-7, -10),
	(-8, -1), (-8, -2), (-8, -3), (-8, -4), (-8, -5), (-8, -6), (-8, -7), (-8, -8), (-8, -9), (-8, -10),
	(-9, -1), (-9, -2), (-9, -3), (-9, -4), (-9, -5), (-9, -6), (-9, -7), (-9, -8), (-9, -9), (-9, -10),
	(-10, -1), (-10, -2), (-10, -3), (-10, -4), (-10, -5), (-10, -6), (-10, -7), (-10, -8), (-10, -9), (-10, -10),

]

slopes = []
colors = ["aquamarine","black","blue","blue violet","brown","burlywood","cadet blue","chartreuse","chocolate","coral","cornflower blue","cyan","dark blue","dark cyan","dark goldenrod","dark gray","dark green","dark grey","dark khaki","dark magenta","dark olive green","dark orange","dark orchid","dark red","dark salmon","dark sea green","dark slate blue","dark slate gray","dark slate grey","dark turquoise","dark violet","deep pink","deep sky blue","dim gray","dim grey","dodger blue","firebrick","forest green","gainsboro","gold","goldenrod","gray","green","green yellow","grey","hot pink","indian red","IndianRed","khaki","lawn green", "light blue","light coral","light cyan","light goldenrod","light gray","light green","light grey","light pink","light salmon","light sea green","light sky blue","light slate blue","light slate gray","light slate grey","light steel blue","lime green","magenta","maroon","medium aquamarine","medium blue","medium orchid","medium purple","medium sea green","medium slate blue","medium spring green","medium turquoise","medium violet red","midnight blue","moccasin","navy","navy blue", "olive drab","orange","orange red","orchid","pale goldenrod","pale green","pale turquoise","pale violet red", "papaya whip","peru","pink","plum","powder blue","purple","red","rosy brown","royal blue","saddle brown","salmon","sandy brown","sea green","sienna","sky blue","slate blue","slate grey","spring green","steel blue","tan","thistle","tomato","turquoise","violet","violet red","wheat","yellow","yellow green"]

def slopefield():
	"Draw Slope Field"
	prestons_turtle.ht()
	draw_axes(hash=enlarge)
	colors_used = 0
	fprime = input("Enter your differential equation: ")
	for pair in points:
		# y - f(i) = m(x - i)
		# y = fprime(i)((i - step) - i) + f(i)
		prestons_turtle.penup()
		#print prestons_turtle.heading()
		prestons_turtle.seth(0)
		#print prestons_turtle.heading()
		x = pair[0]
		y = pair[1]
		try:
			slope = round(eval(fprime), 1)
			angle = atan(slope)
			angle = degrees(angle)
		except ZeroDivisionError:
			slope = "infinty"
			angle = 90
		color = None
		found = False
		print x, y, slope, angle
		for slope_pair in slopes:
			if slope_pair[0] == slope:
				color = slope_pair[1]
				found = True
				break
		if not found:
			color = colors[colors_used]
			slopes.append((slope, color))
			colors_used += 1
		prestons_turtle.color(color)

		# y_new = y_old + slope * (x_new - x_old)
		# y_new - y_old = slope * (x_new - x_old)
		# x_new = ((y_new - y_old) / slope) - x_old) 
		prestons_turtle.goto(x * enlarge, y * enlarge)
		#print prestons_turtle.heading()
		prestons_turtle.seth(angle)
		#print prestons_turtle.heading()
		prestons_turtle.pendown()
		prestons_turtle.forward(line_seg//2)
		prestons_turtle.backward(line_seg)

		#prestons_turtle.penup()
		#prestons_turtle.goto(pair[0], pair[1])
		#prestons_turtle.rt(180+2*atan(fprime(pair[0], pair[1])))
		#prestons_turtle.pendown()
		#prestons_turtle.forward(50)
		prestons_turtle.penup()
		# prestons_turtle.rt(atan(eval(fprime)))
		#prestons_turtle.goto((pair[0]-1), pair[1] - fprime(pair[0], pair[1]) * (pair[0]*10 - pair[0]-1))
		
		#prestons_turtle.goto(((((pair[1] + 10 - pair[1]))/ fprime(pair[0], pair[1])) - pair[0]), (pair[1] + 10))
		
		#prestons_turtle.goto((pair[0]-1)*10, (pair[1] - fprime(pair[0], pair[1]))*10)
		#prestons_turtle.pendown()
		#prestons_turtle.goto(line.p2[0]*10, line.p2[1]*10)
		#prestons_turtle.penup()
		# print "Point (%d, %d) with slope %d" % ( i, f(i),  fprime(i))

		# print "Point (%d, %d) with slope %d" % ( i, f(i),  fprime(i))
	key()

def key():
	"Draws Color Key"
	prestons_turtle.penup()
	
	home()
	prestons_turtle.penup()
	prestons_turtle.goto(-400, 360)
	prestons_turtle.penup()
	prestons_turtle.color("black")
	prestons_turtle.pendown()
	prestons_turtle.write("Slope")
	prestons_turtle.penup()
	prestons_turtle.goto(-400, 350)
	count = 1
	for pair in slopes:
		count += 1
		prestons_turtle.color("black")
		prestons_turtle.pendown()
		prestons_turtle.write(str(pair[0] ) + "    ")
		prestons_turtle.penup()
		prestons_turtle.goto(-400, 360 - 10*(count-1))
		prestons_turtle.seth(0)
		prestons_turtle.forward(20)
		prestons_turtle.penup()
		prestons_turtle.penup()
		prestons_turtle.seth(90)
		prestons_turtle.penup()
		prestons_turtle.forward(4)
		prestons_turtle.penup()
		prestons_turtle.seth(90)
		prestons_turtle.penup()
		prestons_turtle.color(pair[1])
		prestons_turtle.pendown()
		prestons_turtle.forward(3)
		prestons_turtle.backward(6)
		prestons_turtle.penup()
		prestons_turtle.goto(-400, 360 - 10*count)


def print_colors():
	"Draws All Available Colors"
	prestons_turtle.penup()
	
	home()
	prestons_turtle.penup()
	prestons_turtle.goto(-400, 360)
	prestons_turtle.penup()
	prestons_turtle.color("black")
	prestons_turtle.pendown()
	prestons_turtle.write("Color")
	prestons_turtle.penup()
	prestons_turtle.goto(-400, 350)
	count = 1
	for color in colors[::-1]:
		count += 1
		prestons_turtle.color("black")
		prestons_turtle.pendown()
		prestons_turtle.write(str(color ) + "    ")
		prestons_turtle.penup()
		prestons_turtle.goto(-400, 360 - 10*(count-1))
		prestons_turtle.seth(0)
		prestons_turtle.forward(50)
		prestons_turtle.penup()
		prestons_turtle.penup()
		prestons_turtle.seth(90)
		prestons_turtle.penup()
		prestons_turtle.forward(4)
		prestons_turtle.penup()
		prestons_turtle.seth(90)
		prestons_turtle.penup()
		prestons_turtle.color(color)
		prestons_turtle.pendown()
		prestons_turtle.forward(3)
		prestons_turtle.backward(6)
		prestons_turtle.penup()
		prestons_turtle.goto(-400, 360 - 10*count)

	home()
	prestons_turtle.penup()
	prestons_turtle.goto(400, 360)
	prestons_turtle.penup()
	prestons_turtle.color("black")
	prestons_turtle.pendown()
	prestons_turtle.write("Color")
	prestons_turtle.penup()
	prestons_turtle.goto(400, 350)
	count = 1
	for color in colors:
		count += 1
		prestons_turtle.color("black")
		prestons_turtle.pendown()
		prestons_turtle.write(str(color ) + "    ")
		prestons_turtle.penup()
		prestons_turtle.goto(400, 360 - 10*(count-1))
		prestons_turtle.seth(0)
		prestons_turtle.forward(50)
		prestons_turtle.penup()
		prestons_turtle.penup()
		prestons_turtle.seth(90)
		prestons_turtle.penup()
		prestons_turtle.forward(4)
		prestons_turtle.penup()
		prestons_turtle.seth(90)
		prestons_turtle.penup()
		prestons_turtle.color(color)
		prestons_turtle.pendown()
		prestons_turtle.forward(3)
		prestons_turtle.backward(6)
		prestons_turtle.penup()
		prestons_turtle.goto(400, 360 - 10*count)


def draw_axes(hash=enlarge):
	"Draw Axes"
	prestons_turtle.ht()
	home()
	prestons_turtle.goto(0, 600)
	home()
	prestons_turtle.goto(0, -600)
	home()
	prestons_turtle.goto(600, 0)
	home()
	prestons_turtle.goto(-600, 0)
	home()
	for i in range(600//hash):
		prestons_turtle.penup()
		prestons_turtle.goto(0, i*enlarge)
		prestons_turtle.color("black")
		prestons_turtle.pendown()
		prestons_turtle.seth(0)
		prestons_turtle.forward(hash//2)
		prestons_turtle.backward(hash)
		prestons_turtle.penup()
		prestons_turtle.penup()
		prestons_turtle.goto(0, -i*enlarge)
		prestons_turtle.color("black")
		prestons_turtle.pendown()
		prestons_turtle.seth(0)
		prestons_turtle.forward(hash//2)
		prestons_turtle.backward(hash)
		prestons_turtle.penup()
		prestons_turtle.penup()
		prestons_turtle.goto(i*enlarge, 0)
		prestons_turtle.color("black")
		prestons_turtle.pendown()
		prestons_turtle.seth(90)
		prestons_turtle.forward(hash//2)
		prestons_turtle.backward(hash)
		prestons_turtle.penup()
		prestons_turtle.penup()
		prestons_turtle.penup()
		prestons_turtle.goto(-i*enlarge, 0)
		prestons_turtle.color("black")
		prestons_turtle.pendown()
		prestons_turtle.seth(90)
		prestons_turtle.forward(hash//2)
		prestons_turtle.backward(hash)
		prestons_turtle.penup()

def home():
    '''Go to turtle home.'''
    prestons_turtle.penup()
    prestons_turtle.home()
    prestons_turtle.pendown()


def clear():
    '''Clear drawing.'''
    prestons_turtle.clear()


def quit():
    prestons_turtle.bye()


prestons_turtle.onkey(draw_axes, "a")
prestons_turtle.onkey(draw_axes, "A")
prestons_turtle.onkey(slopefield, "s")
prestons_turtle.onkey(slopefield, "S")
prestons_turtle.onkey(home, "h")
prestons_turtle.onkey(home, "H")
prestons_turtle.onkey(clear, "c")
prestons_turtle.onkey(clear, "C")
prestons_turtle.onkey(quit, "q")
prestons_turtle.onkey(quit, "Q")
prestons_turtle.onkey(key, "k")
prestons_turtle.onkey(key, "K")
prestons_turtle.onkey(print_colors, "p")
prestons_turtle.onkey(print_colors, "P")

prestons_turtle.listen()
prestons_turtle.mainloop()