TITLE = "Pong 2021"
WIDTH = 700
HEIGHT = 500

player1 = Actor('player', (10, HEIGHT / 2))
player2 = Actor('player', (WIDTH - 10, HEIGHT / 2))

ball = Actor('ball', (WIDTH / 2, HEIGHT / 2))

def draw():
    screen.clear()
    player1.draw()
    player2.draw()
    ball.draw()
    screen.draw.line((WIDTH / 2, 0), (WIDTH / 2, HEIGHT), (255, 0, 0))
    
    
    
def update():
    pass