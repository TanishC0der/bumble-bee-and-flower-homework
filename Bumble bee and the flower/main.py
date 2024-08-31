import pgzrun
from random import randint
WIDTH=500
HEIGHT=500
TITLE="bee game"
score=0
game_over=False

bee=Actor("bee")
flower=Actor("flower")
bee.pos=250,250
flower.pos=300,250


def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score:"+str(score),color="Black",topleft=(10,10))
    if game_over:
        screen.fill("Blue")
        screen.draw.text("Your final score is :"+str(score),color="Black",fontsize=50,midtop=(250,10) )
def place_flower():
    flower.x=randint(70,(WIDTH-70))
    flower.y=randint(70,(HEIGHT-70 ))
def Timer():
    global game_over
    game_over=True


def update():
    global score
    if keyboard.left:
        bee.x=bee.x-20
    if keyboard.right:
        bee.x=bee.x+20
    if keyboard.up:
        bee.y=bee.y-20
    if keyboard.down:
        bee.y=bee.y+20
    if bee.colliderect(flower):
        score=score+1
        place_flower()
    if bee.x<=0 or bee.x>=500:
        bee.x=250
    if bee.y<=0 or bee.y>=500:
        bee.y=250
        
    

clock.schedule(Timer,20.0)
place_flower()
pgzrun.go()