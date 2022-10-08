#impoting libraries
import turtle as t
import time 
import random as rd


#background colour
#t.bgcolor('yellow')
t.bgcolor('blue')

#defining turtles initiallly _SNAKE
snake=t.Turtle(shape='square',visible=False)
#snake.shape('square')
snake.speed(0)
snake.penup()
snake.hideturtle()


#defining turtles initiallly _frit
leaf=t.Turtle(shape='circle',visible=False)
leaf.color('orange')
leaf.penup()
leaf.speed()
snake.hideturtle()

#defining turtles initiallly _START TEXT
text=False
text=t.Turtle()
text.write('Hello to snake game \n\n        by ARBAZ \n\n press space to start',align='center',font=['Arial',18,'bold'])
text.hideturtle()

#defining turtles initiallly _SCORE
score=t.Turtle()
score.speed(0)
score.hideturtle()


#defining functions
def outside_win():
    left  =-t.window_width()/2
    right = t.window_width()/2
    top   = t.window_height()/2
    bottom=-t.window_height()/2
    (x,y) = snake.pos()
    outside = x<left or x>right or y>top or y<bottom 
    return outside

def place_leaf():
    leaf.hideturtle()
    leaf.setx(rd.randint(-200,200))
    leaf.sety(rd.randint(-200,200))
    leaf.showturtle()

def gameover(current_score):
    snake.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write(f"GAME OVER \n Your score={current_score}",align='center',font=['Arial',30,'bold'])
    
def dis_score(current_score):
    score.clear()
    score.penup()
    x=(t.window_width()/2)-50
    y=(t.window_height()/2)-50
    score.setpos(x,y)
    score.write(f"score = {current_score}",align="right",font=['Arial',40,'bold'])

def start():
    game_started = False
    if game_started:
        return
    else:
        game_started= True
        current_score=0
        text.clear()
        snake_speed=2
        snake_length=3
        snake.shapesize(1,snake_length,1)
        snake.showturtle()
        dis_score(current_score)
        place_leaf()
        

    
    while True:
        snake.forward(snake_speed)
        if snake.distance(leaf)<20:
            place_leaf()
            snake_length=snake_length+1
            snake.shapesize(1,snake_length,1)
            snake_speed=snake_speed+1
            current_score=current_score+10
            dis_score(current_score)
           
        if outside_win():
            gameover(current_score)
            break
           

def move_up():
    if snake.heading()==0 or snake.heading()== 180:
        snake.setheading(90)


def move_down():
    if snake.heading()==0 or snake.heading()== 180:
        snake.setheading(270)


def move_left():
    if snake.heading()==90 or snake.heading()== 270:
        snake.setheading(180)


def move_right():
    if snake.heading()==90 or snake.heading()== 270:
        snake.setheading(0)



t.onkey(start,'space')
t.onkey(move_up,'Up')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.onkey(move_right,'Right')
t.listen()
t.mainloop()

time.sleep(10)
