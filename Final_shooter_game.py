import pygame,random,math
pygame.init()

w,h=600,740
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("Shooter Game")




step=40
left=(-step,0)
right=(step,0)
direction=(1,1)


FPS=60
clock = pygame.time.Clock()
timer=0


score=0
font = pygame.font.SysFont("Arial", 24, True)
def display_score(screen, score):
    text_surface = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text_surface, (15,15))



## making a class for player

class player() :
    playerimg=pygame.image.load("player2.png")
    playerx=370
    playery=650#480

    def play(self,x,y):
        screen.blit(self.playerimg,(x,y))


    ## adding the player bullet
    bulletimg=pygame.image.load('hero_bullet.png')
    bulletx=0
    bullety=650
    bulletx_change=0
    bullety_change=20   
    bullet_state="loading"#loading==not firing   fire==firing
    #bullet_state="loading"
    def fire_bullet(self,x,y):
        global bullet_state
        self.bullet_state="fire"
        screen.blit(self.bulletimg,(x+16,y+10))











## making a class for demon

class enemy() :

    demonimg=pygame.image.load('demon.png')
    demonx=random.randint(15,525)
    demony=random.randint(50,200)
    demonx_change=3
    demony_change=5

    #def __init__(self,x_change=3,y_change=5) :
    #    demonx_change=x_change#3
    #    demony_change=y_change#5
        
        
    def demon(self,x,y):
        
        screen.blit(self.demonimg,(x,y))

    
    #adding bullets to the demon
    bulletimg=pygame.image.load('demon_bullet.png')
    dembulletx=demonx
    dembullety=demony
    dembulletx_change=0
    dembullety_change=10#20
    dembullet_state="loading"
    def bullet(self,x,y):
        global dembullet_state
        self.dembullet_state="fire"
        screen.blit(self.bulletimg,(x-16,y-5))#10





pl=player()
playx=pl.playerx
playy=pl.playery
#pl.play
#pl.fire_bullet(pl.playerx,pl.playery)
dem=enemy()
demx=dem.demonx
demy=dem.demony
dem1=enemy()
dem1x=dem1.demonx
dem1y=dem1.demony





#to detect collision
def iscollision(demx,demy,bulletx,bullety):
    distance1=math.sqrt(math.pow(demx-bulletx,2) + math.pow(demy-bullety,2))
    if distance1<27:
        return True
    else:
        return False







pretime=0
run=True
while run:
    timer+=1
    screen.fill((0,0,0))
    clock.tick(FPS)

    for ev in pygame.event.get():
        if ev.type==pygame.QUIT: 
            print("Quit")
            run=False

        elif ev.type==pygame.KEYDOWN:## ye part ho gaya game arrow key ke use ke detect hone pe active 
            if ev.key==pygame.K_LEFT and playx>=15:##movement toward left side of the screen
                #print("left\n")
                playx-=step
            elif ev.key==pygame.K_RIGHT and playx<=525:## movement towards right side of the screen
                #print("right\n")
                playx+=step
            elif ev.key==pygame.K_SPACE:## to fire a bullet from the player
                if pl.bullet_state == "loading":
                    pl.bulletx=playx
                    #print("fire")
                    pl.fire_bullet(pl.bulletx, pl.bullety)



    ## to display the player and make it move
    pl.play((playx),(playy))


    ## to display the enemy and make it move 
    dem.demon((demx),(demy))


    ##to display the 2nd enemy and to make it move
    dem1.demon((dem1x),(dem1y))




    ## demon automovement
    demx+=dem.demonx_change
    ## demon constrain
    if demx<=15 :
        dem.demonx_change=3
    elif demx>=525:
        dem.demonx_change=-3





    ## demon 2 automovement
    dem1x+=dem1.demonx_change
    ## demon 2 constrain
    if dem1x<=15:
        dem1.demonx_change=3
    elif dem1x>=525 :
        dem1.demonx_change=-3




    ##bullet movement
    if pl.bullety<=0: ## to shoot multipul bullets
        pl.bullety=650
        pl.bullet_state="loading"



    if pl.bullet_state=="fire" :
        pl.fire_bullet(pl.bulletx,pl.bullety)
        pl.bullety-=pl.bullety_change



    collision=iscollision(demx,demy,pl.bulletx,pl.bullety)
    if collision:
        pl.bullety=650
        pl.bullet_state="loading"
        score+=1
        demx=random.randint(15,525)
        demy=random.randint(50,200)
        continue



    collision2=iscollision(dem1x,dem1y,pl.bulletx,pl.bullety)
    if collision2:
        pl.bullety=650
        pl.bullet_state="loading"
        score+=1
        dem1x=random.randint(15,525)
        dem1y=random.randint(50,200)
        continue





    ##giving demons there bullets
    if timer%30==0 :
        if dem.dembullet_state=="loading":
            dem.dembulletx=demx
            dem.dembullety=demy
            #print("reverse fire")
            dem.bullet(dem.dembulletx,dem.dembullety)




    ## demon bullet movement
    if dem.dembullety>=700:
        dem.dembullety=0
        dem.dembullet_state="loading"


    if dem.dembullet_state=="fire":
        dem.bullet(dem.dembulletx,dem.dembullety)
        dem.dembullety+=dem.dembullety_change


    collision3=iscollision(playx,playy,dem.dembulletx,dem.dembullety)
    if collision3 :
        dem.dembullety=0
        dem.dembullet_state="loading"
        print("Died 1")
        run=False
        break






    ## demon 2 bullet movement
    if timer%18==0:
        if dem1.dembullet_state=="loading":
            dem1.dembulletx=dem1x
            dem1.dembullety=dem1y
            #print("reverse fire")
            dem1.bullet(dem1.dembulletx,dem1.dembullety)


    if dem1.dembullety>=700:
        dem1.dembullety=0
        dem1.dembullet_state="loading"



    if dem1.dembullet_state=="fire":
        dem1.bullet(dem1.dembulletx,dem1.dembullety)
        dem1.dembullety+=dem1.dembullety_change



    collision4=iscollision(playx,playy,dem1.dembulletx,dem1.dembullety)
    if collision4:
        dem1.dembullety=0
        dem1.dembullet_state="loading"
        print("Died 2")
        run=False
        break




    ##to display the score
    display_score(screen, score)

    ## to refresh the screen
    pygame.display.update()

        