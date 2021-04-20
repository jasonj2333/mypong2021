TITLE = "Pong 2021"
WIDTH = 700
HEIGHT = 500

start_game = False
game_over = False

player1 = Actor('player', (10, HEIGHT / 2))
player2 = Actor('player', (WIDTH - 10, HEIGHT / 2))

ball = Actor('ball', (WIDTH / 2, HEIGHT / 2))
ball_x = 5
ball_y = 5

player1_score = 0
player2_score = 0

def draw():
    screen.clear()
    player1.draw()
    player2.draw()
    screen.draw.line((WIDTH / 2, 0), (WIDTH / 2, HEIGHT), (255, 255, 255))
    ball.draw()
    screen.draw.text(str(player1_score), center=(WIDTH / 4, 30), fontsize=60)
    screen.draw.text(str(player2_score), center=(WIDTH / 4 * 3, 30), fontsize=60)
    if game_over:
        screen.draw.text('Koniec gry !!!', center=(WIDTH / 2, HEIGHT / 2), fontsize=60)
    
    
def update():
    global ball_x
    global ball_y
    global player1_score
    global player2_score
    global start_game
    global game_over
    
    if keyboard.space and not start_game:
            start_game = True
            game_over = False
            player1_score = 0
            player2_score = 0
    
    if not game_over:
    
        if start_game:
        
            ball.x += ball_x
            ball.y += ball_y
            
            if ball.y > HEIGHT or ball.y < 0:
                ball_y *= -1
                
            if ball.x > WIDTH or ball.x < 0:
                if ball.x < 0:
                    player2_score += 1
                else:
                    player1_score += 1
                
                if player1_score == 2 or player2_score == 2:
                    game_over = True
                    start_game = False
                
                ball_x *= -1
                ball.x = WIDTH / 2
                ball.y = HEIGHT / 2
                
            
            if ball.colliderect(player1) or ball.colliderect(player2):
                ball_x *= -1
                
            
            #player1 move
            if keyboard.w and player1.top > 0:
                player1.y -= 5
            if keyboard.s and player1.bottom < HEIGHT:
                player1.y += 5
                
            #player2 move
            if keyboard.up and player2.top > 0:
                player2.y -= 5
            if keyboard.down and player2.bottom < HEIGHT:
                player2.y += 5