# Fun-Drawing
The purpose of this project is to allow the user to customize a ready-made drawing (a heart). The program takes in parameters that allow the heart's color and outline, background of drawing, pen size (how big the pen used to draw the drawing is), and the speed of the drawing to be customized either randomly or by the choices of the user. 

This project uses the turtle and random Python libraries, while loops, input statements, and some built-in functions in Python. 

The program begins by asking the user if they would like to have their pre-made drawing's features (stated above) customized to their choosing or randomly selected. Any input other than "random" or "" (enter) results in the input entering a while loop which prompts the user to reenter their input until it is of the correct value. 

If the user chooses the features to be randomly selected, the program will use the random library in Python to assign numerical or color values to variables that can be used in the process of the drawing process. The randomized color selection is based on a list that contains various colors that are compatible with the Python turtle library. This is done using the random library in Python. 

If the user chooses the features to be customized based on their liking, the program will begin by asking the user for their choices on all of the parameters provided and assigning their answer to a corresponding variable. For the colors the user can select from, they are prompted with a list of colors. They must choose their option from the colors. If they do not, there is a function, 'color_input_validator' that will prompt the user again to enter their color selection if it is of the incorrect data value. Additionally, there are also while loops that validate if any other data is not of the correct value. 

At the end of this program, based on the user's choices, a Python Turtle window will pop up with either a random selection to the parameters mentioned above, or the exact parameters the user provided if the user chooses to have their own ideas used. 
