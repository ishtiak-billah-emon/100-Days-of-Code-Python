def my_function():
  print("Hello Hi bye bye! -_-")

# call the function
my_function()

x = 15
y = 10

#indentation
def another_function():
  if x > y:
    print("x > y")
  else:
    print("y > x")
another_function()


while not at_goal():
  if front_is_clear() == True:
    move()
  elif wall_in_front() == True:
    jump()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    move()
    
height = 0

def forward_move():
    turn_right()
    move()
    turn_right()
    while height > 0:
        move()
        height -= 1     
    move()
    turn_left()

think(10)
while not at_goal(): 
    if wall_in_front():
        while wall_in_front():
            jump()
            height += 1
            while wall_on_right():
                move()
                height += 1
        forward_move()
    else:
        move()


