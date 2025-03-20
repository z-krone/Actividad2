"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

colors = ["blue", "orange", "pink", "cyan", "purple"]

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    """Move food randomly one step while staying inside boundaries."""
    new_x = food.x + randrange(-1, 2) * 10  
    new_y = food.y + randrange(-1, 2) * 10  

    if -200 < new_x < 190:
        food.x = new_x
    if -200 < new_y < 190:
        food.y = new_y
    
    ontimer(move_food, 500)

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
    else:
        snake.pop(0)

    clear()

    snakeColor = choice(colors)
    foodColor = choice(colors)

    for body in snake:
        square(body.x, body.y, 9, snakeColor)

    square(food.x, food.y, 9, foodColor)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
move_food()
done()
