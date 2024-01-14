#importing necessary libraries
import turtle
import random


def curve():
##this function creates a curve shape on the turtle canvas by constantly turning and going forward at the same rate 
##preconditions: no preconditions!
##parameters: no parameters!
##returns: returns a curve-like shape on the turtle canvas. 
    for i in range(100):
        for i in range(2):
            t.forward(1)
            t.right(1)

def color_input_validation(choice):
##this function checks if the input the user gives matches a color in the list provided
##preconditions: choice (parameter) must be of a string value
##parameters: choice - is the input the user puts for the certain feature they want in their drawing
##returns: choice of a certain color on the list 'colors' if the choice was not already that 
    while not choice in colors: 
        print("This is not a valid choice! Please choose a color specified in the list!")
        choice = input("Choose a color please! ").lower() 
    return choice 

print("Hello! This is a program where you get to either personalize a given drawing based on certain options or have it randomized!")

#ask if user wants features chosen randomly or if they want to choose them 
random_or_choice_features = input("Do you want to personally select the features of the drawing or shall it be randomly chosen? Type random for a random selection or leave this question empty for it to be your choice: ")

#validates choice to ensure that the input matches the corresponding options
while not (random_or_choice_features == "random" or random_or_choice_features == ""):
    random_or_choice_features = input("This is not a valid answer. Please either type in random or skip the question to proceed: ").lower()
    
print("The image being drawn is a heart!")

#list of all colors available for user to choose from in their drawing 
colors = ['red', 'blue', 'green', 'purple', 'pink', 'orange', 'yellow', 'brown', 'gold', 'magenta']


#setting up randomized features for the drawing 
if random_or_choice_features == "random":
    print("You have chosen the random feature! Everything within the drawing will be randomized, like the background color and the color of the heart.") 
    #selects a random index from the list 'colors' and assigns it to the corresponding variable 
    heart_outline = colors[random.randint(1,10)] 
    heart_color = colors[random.randint(1,10)]
    background_color = colors[random.randint(1,10)]
    
    #selects a random integer from the given range to assign to the corresponding variable 
    pen_size = random.randint(1, 20)
    speed_of_drawing = random.randint(1, 10)
    

#under the condition that the user wants to choose the features of the turtle drawing, the following code would run: 
elif random_or_choice_features == "":
    print("Let's get into it! First, choose the colors to be used in this drawing! Below are the options available for you for each color component:")
    print(colors)
    
    heart_outline = input("Begin by choosing the heart's outline color here. Type the color as you see it! : ").lower() 
    #validating whether the input the user gives is a color provided in the list 
    color_input_validation(heart_outline)
    heart_outline = color_input_validation(heart_outline)
    
    heart_color = input("Next, choose the color of your heart! ").lower() 
    heart_color = color_input_validation(heart_color)
    

    
    background_color = input("Choose the color of your background: ")
    background_color = color_input_validation(background_color).lower() 
        
    pen_size = int(input("Choose your pensize now! The number you pick should be between 1-20. "))
    
    while pen_size > 20 or pen_size < 0:
        pen_size = int(input("This is not the correct range! Pick your pensize again, please. "))
    
    speed_of_drawing = int(input("Finally, pick the speed at which you want the drawing to be.. well.. drawn! This should be between 1-10, with 1 being the slowest, and 10 being the fastest. "))
    
    while speed_of_drawing > 10 or speed_of_drawing < 0:
        speed_of_drawing = int(input("Invalid speed. Pick your speed again! ")) 

print("Time to draw the heart! Enjoy!")
#initialize turtle program 
t = turtle.Turtle()

#setting speed,  pensize, pencolor, bg and fill color based on either random pick or user's pick
turtle.speed(speed_of_drawing)
turtle.bgcolor(background_color) 
turtle.pensize(pen_size)
t.pencolor(heart_outline)
 

#setting up starting position of drawing
t.penup() 
t.setpos(0,0)
t.pendown()

#begins to fill the shape being drawn!
t.fillcolor(heart_color) 
t.begin_fill()
t.left(135) 
t.forward(100)
curve() 
t.left(125)
curve()
t.forward(125)
t.right(90)
t.forward(50) 
#ends this fill! (actually fills it) 
t.end_fill() 
