from turtle import *
import random
import math

def SetTurtle():

  # Screen customization
    window = Screen ()
    window.setup(350, 400)
    window.title("Project Task 03")
    window.bgcolor("yellow")

    # Circle boundary 
    T1 = Turtle()
    T1.hideturtle()
    T1.speed(1)
    T1.penup()
    T1.setpos(0,-100)
    T1.pendown()
    
    # Drawing circular boundary
    T1.begin_fill()
    T1.color("Black")
    T1.pen(fillcolor="Black", pencolor="Black", pensize=2)
    T1.circle(100)
    T1.end_fill()
    T1.penup()
    

# Task-03
def Task_03():
    SetTurtle()

    # Moving pointer
    T2 = Turtle()
    # centre_x, centre_y = T2.position() # centre (xcor, ycor)
    T2.speed(0)
    T2.penup()
    
    colors  = ["red","green","blue","orange","purple","pink","yellow"]
    
    '''
    # ---------------------------------------
    # Technique - 01 : Reflection

    # Random moves generator
    while True:

        T2.pendown()
        T2.color(random.choice(colors))
        
        # current position
        x,y = T2.position() # xcor, ycor

        # saving old cordinates for later use
        old_x , old_y = x, y 

        discrete_steps = [0, 0.5, 1]
        discrete_angle = 90 * (random.randint(1, 5) - 1)
        
        # new coordinates 
        new_x , new_y = x+(random.choice(discrete_steps)* math.cos(discrete_angle)) , y+ (random.choice(discrete_steps)* math.sin(discrete_angle))
        
        # if with in the boundary -> move in any direction
        if math.sqrt((new_x)**2 + (new_y)**2) < 100:
            T2.setheading(discrete_angle)
            #T2.goto(new_x, new_y)
            x,y = new_x, new_y
            

        else:
            # bounce back / reverse and move in other direction
            T2.setheading(discrete_angle)
            #T2.goto(old_x, old_y)
            x,y = old_x, old_y
            
        T2.goto(x,y)
    '''

    # -----------------------------------------------------
    # Technique - 02 : Complete 3D Traversal 

    # Random moves generator
    while True:

      T2.pendown()
      T2.color(random.choice(colors))
      
      x,y = T2.position() # xcor, ycor
      old_x , old_y = x, y 
      discrete_steps = [0, 0.5, 1]
      discrete_angle = 90 * (random.randint(1, 5) - 1)
      
      # new coordinates 
      new_x , new_y = x+(random.choice(discrete_steps)* math.cos(discrete_angle)), y+ (random.choice(discrete_steps)* math.sin(discrete_angle))
      
      # if with in the boundary -> move in any direction
      if math.sqrt((new_x)**2 + (new_y)**2) < 100:
          T2.setheading(discrete_angle)
          #T2.goto(new_x, new_y)
          x,y = new_x, new_y
          T2.goto(x,y)
          

      else:
          # bounce back / reverse and move negative in direction
          #T2.setheading(discrete_angle)
          T2.hideturtle()
          T2.penup()
          # reversing the coordinates
          x,y = -old_x, -old_y
          T2.goto(x,y)
          T2.pendown()
    
    # ------------------------------------


def Task_05():
  
  SetTurtle()

  # Moving pointer
  T2 = Turtle()
  # centre_x, centre_y = T2.position() # centre (xcor, ycor)
  T2.speed(0)
  T2.penup()

  colors  = ["red","green","blue","orange","purple","pink","yellow"]

  # Random moves generator
  while True:

      T2.pendown()
      T2.color(random.choice(colors))
      
      # current position
      x,y = T2.position() # xcor, ycor

      # saving old cordinates for later use
      old_x , old_y = x, y 

      continous_steps = random.uniform(0,1)
      continous_angle = random.uniform(0,360)
      
      # new coordinates 
      new_x , new_y = x+(continous_steps* math.cos(continous_angle)) , y+ (continous_steps* math.sin(continous_angle))
      
      # if with in the boundary -> move in any direction
      if math.sqrt((new_x)**2 + (new_y)**2) < 100:
          T2.setheading(continous_angle)
          #T2.goto(new_x, new_y)
          x,y = new_x, new_y
          T2.goto(x,y)
          

      else:
          # bounce back / reverse and move in other direction
          # T2.setheading(continous_angle)
          T2.hideturtle()
          T2.penup()
          x,y = -old_x, -old_y
          T2.goto(x,y)
          T2.pendown() 



def Task_07():
  SetTurtle()

  # Moving pointer
  T2 = Turtle()
  # centre_x, centre_y = T2.position() # centre (xcor, ycor)
  T2.speed(0)
  T2.penup()

  colors  = ["red","green","blue","orange","purple","pink","yellow"]

  # Random moves generator
  while True:

    T2.pendown()
    T2.color(random.choice(colors))
    
    # current position
    x,y = T2.position() # xcor, ycor

    # saving old cordinates for later use
    old_x , old_y = x, y 

    discrete_steps = random.choice([0, 0.5, 1])
    continous_angle = random.uniform(0,360)
    
    # new coordinates 
    new_x , new_y = x+(discrete_steps* math.cos(continous_angle)) , y+ (discrete_steps* math.sin(continous_angle))
    
    # if with in the boundary -> move in any direction
    if math.sqrt((new_x)**2 + (new_y)**2) < 100:
        T2.setheading(continous_angle)
        #T2.goto(new_x, new_y)
        x,y = new_x, new_y
        T2.goto(x,y)
        

    else:
        # bounce back / reverse and move in other direction
        # T2.setheading(continous_angle)
        T2.hideturtle()
        T2.penup()
        x,y = -old_x, -old_y
        T2.goto(x,y)
        T2.pendown() 


            
if __name__ == '__main__':
    #Task_03()
    #Task_05()
    #Task_07()
