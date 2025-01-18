from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__(player_image, player_x, player_y, player_speed, wight, height)
        self.score = 0

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__(player_image, player_x, player_y, player_speed, wight, height)
        self.speed_x = 3
        self.speed_y = 3
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > win_height-50 or self.rect.y < 0:
            self.speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            self.speed_x *= -1


back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)        

game = True
finish = False
clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3


racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = Ball('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE', True, (180, 0, 0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        racket1.reset()
        racket2.reset()
        ball.reset()

        score_all = font.render(str(racket2.score)+':'+str(racket1.score), True, (180, 0, 0))
        window.blit(score_all, (200, 50))

        if ball.rect.x < 0 :
            racket1.score += 1
            ball.rect.x, ball.rect.y = 200, 200
            ball.speed_x *= -1 ** (randint(1,2))
        if racket1.score >= 3:
            finish = True
            window.blit(lose1, (200, 200))    
            
            
        if ball.rect.x > 600 :
            racket2.score += 1
            ball.rect.x, ball.rect.y = 200, 200
        if racket2.score >= 3:
            finish = True
            window.blit(lose2, (200, 200))
            ball.speed_x *= -1 ** (randint(1,2))
            


    display.update()
    clock.tick(FPS)
from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__(player_image, player_x, player_y, player_speed, wight, height)
        self.score = 0

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height-80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height-80:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__(player_image, player_x, player_y, player_speed, wight, height)
        self.speed_x = 3
        self.speed_y = 3
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y > win_height-50 or self.rect.y < 0:
            self.speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            self.speed_x *= -1


back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)        

game = True
finish = False
clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3


racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = Ball('tenis_ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE', True, (180, 0, 0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.update()

        racket1.reset()
        racket2.reset()
        ball.reset()

        score_all = font.render(str(racket2.score)+':'+str(racket1.score), True, (180, 0, 0))
        window.blit(score_all, (200, 50))

        if ball.rect.x < 0 :
            racket1.score += 1
            ball.rect.x, ball.rect.y = 200, 200
            ball.speed_x *= -1 ** (randint(1,2))
        if racket1.score >= 3:
            finish = True
            window.blit(lose1, (200, 200))    
            
            
        if ball.rect.x > 600 :
            racket2.score += 1
            ball.rect.x, ball.rect.y = 200, 200
        if racket2.score >= 3:
            finish = True
            window.blit(lose2, (200, 200))
            ball.speed_x *= -1 ** (randint(1,2))
            


    display.update()
    clock.tick(FPS)
