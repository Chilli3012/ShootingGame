import pygame,random,math
pygame.init()

w,h=600,800
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("Shooter Game")

step=20
left = (-step, 0)
right = (step,0)
direction=(1,1)

FPS=60
clock = pygame.time.Clock()
timer=0

## for score part
score=0
font = pygame.font.SysFont("Arial", 24, True)
def display_score(screen, score):
    text_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text_surface, (15,15))


##adding play
playerimg=pygame.image.load('player2.png')
playerx=370
playery=650#480
def player(x,y):
    screen.blit(playerimg,(x,y))

## adding the demon
demonimg=pygame.image.load('demon.png')
demonx=random.randint(0,600)
demony=random.randint(50,200)
demonx_change=3
demony_change=5
def demon(x,y):
    screen.blit(demonimg,(x,y))


## adding the 2nd demon
demon2img=pygame.image.load('demon.png')
demon2x=random.randint(0,600)
demon2y=random.randint(50,200)
demon2x_change=5
demon2y_change=2
def demon2(x,y):
    screen.blit(demonimg,(x,y))


## adding the hero bullet
bulletimg=pygame.image.load('hero_bullet.png')
bulletx=0
bullety=650
bulletx_change=0
bullety_change=20
bullet_state="loading"#loading==not firing   fire==firing
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+16,y+10))


## adding bullet to the demons
bullet1img=pygame.image.load('demon_bullet.png')
bullet1x1=demonx
bullet1y1=demony



##adding second bullets to the demon
bullet2img=pygame.image.load('demon_bullet.png')
bullet2x1=demon2x
bullet2y1=demon2y


#to detect collision
def iscollision(demonx,demony,bulletx,bullety):
    distance1=math.sqrt(math.pow(demonx-bulletx,2) + math.pow(demony-bullety,2))
    if distance1<27:
        return True
    else:
        return False


pretime=0
run=True
while run :
    timer+=1
    screen.fill((0,0,0))
    clock.tick(FPS)



    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            print("Quit")
            run=False

        if ev.type==pygame.KEYDOWN:
            if ev.key==pygame.K_LEFT and playerx>=10:
                playerx-=step
            elif ev.key==pygame.K_RIGHT and playerx<=590:
                playerx+=step
            elif ev.key==pygame.K_SPACE:
                if bullet_state is "loading":
                    bulletx=playerx
                    fire_bullet(bulletx, bullety)

    
    ## to display the player and make it move
    player(playerx,playery)
    

    ## to display the enemy
    demon(demonx,demony)

    ## to display the 2nd enemy
    demon2(demon2x,demon2y)

    ## demon automovement
    demonx+=demonx_change
    ## demon constrain
    if demonx<=0 :
        demonx_change=3
    elif demonx>=590:
        demonx_change=-3

    ## demon 2 automovement
    demon2x+=demon2x_change
    ## demon 2 constrain
    if demon2x<=0:
        demon2x_change=3
    elif demon2x>=590 :
        demon2x_change=-3

    ##bullet movement
    if bullety<=0: ## to shoot multipul bullets
        bullety=650
        bullet_state="loading"


    if bullet_state=="fire" :
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change

    #for collision
    collision=iscollision(demonx,demony,bulletx,bullety)
    if collision:
        bullety=650
        bullet_state="loading"
        score+=1
        demonx=random.randint(0,600)
        demony=random.randint(50,200)

    collision2=iscollision(demon2x,demon2y,bulletx,bullety)
    if collision2:
        bullety=650
        bullet_state="loading"
        score+=1
        demon2x=random.randint(0,600)
        demon2y=random.randint(50,200)


    ##to display the score
    display_score(screen, score)

    ## to refresh the screen
    pygame.display.update()


