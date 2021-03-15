TITLE = "Pong 2021"
WIDTH = 700
HEIGHT = 500

player1 = Actor('player', (10, HEIGHT / 2))
player2 = Actor('player', (WIDTH - 10, HEIGHT / 2))

ball = Actor('ball', (WIDTH / 2, HEIGHT / 2))
ball_x = 3
ball_y = 3

def draw():
    screen.clear()
    player1.draw()
    player2.draw()
    screen.draw.line((WIDTH / 2, 0), (WIDTH / 2, HEIGHT), (255, 255, 255))
    ball.draw()
    
    
def update():
    global ball_x
    global ball_y
    
    ball.x += ball_x
    ball.y += ball_y
    
    if ball.y > HEIGHT or ball.y < 0:
        ball_y *= -1
        
    if ball.x > WIDTH or ball.x < 0:
        ball_x *= -1