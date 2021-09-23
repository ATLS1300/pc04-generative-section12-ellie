"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Eleanor Kreppein

********* HEY, READ THIS FIRST **********

My creation invokes emotions of happiness and lightheartedness. It is meant to raditate positivity and creativity while stimulating 
the viewers sense of sight. I chose this color palette to imitate the bright colors of sunrise, along with dark colors of fading 
nighttime. In addition to this, I implmented some lighter sea foam colors to symbolize the ocean. The shapes and designs I created
were the product of my exploration of Turtle commands and I resonated with their rambunctious nature. 


"""
import turtle
import random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================

panel.bgcolor("lemonchiffon") # set background color

greenPalette = ["LightGreen", "honeydew", "LightPink", "DarkSlateBlue", "LightSeaGreen", "ForestGreen"]
goldenRodPalette = ["DarkSlateGray", "DarkOrange2", "DeepPink1", "firebrick", "LawnGreen"]

mySlinky = turtle.Turtle() # create first turtle, originally looked like a slinky, my ideas changed a lil
starShape = turtle.Turtle() #create second turtle, replicates a star/asterisk

palette = random.choice([greenPalette, goldenRodPalette])

mySlinky.speed(15) 
mySlinky.width(7)
starShape.speed(5) 
starShape.width(19)


#for loop for spiral of large circles
for i in range(30): # i gets defined by the for loop
    mySlinky.up()
    color = random.choice(palette) #randomize the colors of the large circles
    mySlinky.color(color)
    
    #move to position of spiral
    #modified from https://holypython.com/turtle-spirals/
    mySlinky.forward(1+i)
    mySlinky.right(30)
    mySlinky.down()
    mySlinky.circle(30*i)
    
#for loop for star shape in the center of the big shape
for i in range(15):
    color = random.choice(palette) #randomizes the colors of the smaller shape in the center 
    starShape.color(color)
    starShape.up()
    starShape.goto(0,0)
    starShape.down()
    starShape.forward(50)
    starShape.backward(50)
    starShape.right(35) 
    
turtle.done()
