import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(10)

# Function to draw a spiral
def draw_spiral(color):
    pen.pencolor(color)
    for i in range(100):
        pen.forward(i * 10)
        pen.right(45)

# Function to draw a heart
def draw_heart(color):
    pen.pencolor(color)
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

# Function to choose a random color
def random_color():
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "white"]
    return random.choice(colors)

# Main function to execute the art generation
def generate_art():
    # Get user input for the pattern
    pattern = screen.textinput("Choose Pattern", "Enter 'spiral' or 'heart':")
    
    if pattern == "spiral":
        color = screen.textinput("Choose Color", "Enter a color for the spiral:")
        draw_spiral(color)
    
    elif pattern == "heart":
        color = screen.textinput("Choose Color", "Enter a color for the heart:")
        draw_heart(color)
    
    else:
        pen.write("Invalid pattern choice! Please enter 'spiral' or 'heart'.", align="center", font=("Arial", 16, "bold"))

# Start the art generation
generate_art()

# Hide the turtle after drawing
pen.hideturtle()

# Keep the window open
turtle.done()
