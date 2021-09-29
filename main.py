#what is even interlectual property 


import pygame
import math
import random

#conf file
# im going to define some globals, i know ii but my code is too messed up.
conf_globals = []

conf_file = open("conf.txt", "r")
conf=conf_file.read()
conf = conf.split("\n") #oops
for i in conf:
    x = i.split(" = ") #yes i know but i seriusly cant have not spaces
    conf_globals.append(x) #note that i never int so they can be strings
conf_file.close()

def conf_search(name): #just gets the data asosiated with a name in the conf_global list
    for i in conf_globals:
        if name == i[0]:
            return i[1]
    a # this is stupid i want to crash the program and forgot how to throw an exeption or something no weit not that 

#graphics
tile = 300

screen_size = (3, 2)

player_size = 30

window=pygame.display.set_mode((screen_size[0]*tile, screen_size[1]*tile))

class Entity:
    entity_render_list = []
    def __init__(self, hit_box, render):
            self.hit_box = hit_box
            self.__render__ = render #render is a function that takes in an hitbox and renders the object
            __class__.entity_render_list.append(self)
    def render_entity(self):
       self.__render__(self.hit_box)

class Rect_entity:
    def __init__(self, hit_box, color):
        self.entity = Entity(hit_box)
        Entity.entity_render_list.append(self)




def player_render():
  x=(math.sin(jack.angle-0.25)*player_size+jack.x, math.cos(jack.angle-0.25)*player_size+jack.y)

  y=(math.sin(jack.angle+0.35)*player_size+jack.x, math.cos(jack.angle+0.35)*player_size+jack.y)

  z=(math.sin(jack.angle-math.pi)*player_size+jack.x, math.cos(jack.angle-math.pi)*player_size+jack.y)

  pygame.draw.polygon(window, (255, 255, 255), (z, x, y))

jacki=pygame.Surface((10,10))
imag = pygame.image.load(conf_search("filename"))
imag = pygame.transform.scale(imag, (50, 50))

def graphics():
    window.fill((0, 0, 0))
    render_astroid()
    player_render()
    render_shot()
    render_collectables()
    pygame.display.update()

#

#astrodise

astroid_hitbox = 50

astroids = []

def render_astroid():
    k=0
    for i in astroids:
        x= i[0]+i[2][0]/10*speed
        y= i[1]+i[2][1]/10*speed

        pos=warp(x, y)

        astroids[k][0]=pos[0]
        astroids[k][1]=pos[1]
         
        pygame.draw.rect(window, (0, 255, 0), (pos[0], pos[1], astroid_hitbox, astroid_hitbox))
        k += 1
        window.blit(imag, (x, y))

def spawn_astroid():
    cous=random.randint(0,3)
    if cous==0:
      x=0
      y = random.randint(20,tile * screen_size[1]-20)
      vol = (random.randint(3, 10), random.randint(3, 10))
    if cous==1:
      x = screen_size[0]*tile
      y = random.randint(20,tile * screen_size[1]-20)
      vol = (random.randint(0, 7)-10, random.randint(0, 20)-10)
    if cous==2:
      x= random.randint(20,tile * screen_size[0]-20) 
      y = 0
      vol = (random.randint(0, 20)-10, random.randint(3, 10))
    if cous==3:
      y = screen_size[1] * tile
      x = random.randint(20,tile * screen_size[1]-20)
      vol = (random.randint(0, 20)-10, random.randint(0, 10)-10)
    
    astroids.append([x, y, vol])

#key presses

class Player:
    def __init__(self, x, y, vol, angle, health):
        self.x = x
        self.y = y
        self.vol = vol
        self.angle = angle
        self.health = health


jack = Player(screen_size[0] * tile / 2, screen_size[1] * tile / 2 , (0, 0), 0, int(conf_search("amount_of_life")))
print(jack.x, jack.y)

def check_keys(framecount, j, spam):
  #if framecount/2==round(framecount/2):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
    keys = pygame.key.get_pressed()
    pygame.key.set_repeat(1, 100000000)
        

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
      jack.angle+=0.08/speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
      jack.angle-=0.08/speed
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        calculate_vol(0.05,framecount)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
      jack.vol=(jack.vol[0]/1.02, jack.vol[1]/1.02)
    if keys[pygame.K_SPACE] and j == True:
        spawn_shot()
        j=False
    if framecount/spam == round(framecount/spam):
        j=True
    
    return j


def calculate_vol(x,framecount):
    anglevector = (math.sin(jack.angle-math.pi)/2, math.cos(jack.angle-math.pi)/2)
    jack.vol = (jack.vol[0]+anglevector[0]/4, jack.vol[1]+anglevector[1]/4)



#move


speed = 1


def warp(x,y):
  if x<0:
    x=screen_size[0] * tile - 2
  if x>screen_size[0] * tile:
    x=2
  if y<0:
    y=screen_size[1] * tile-2
  if y>screen_size[1] * tile:
    y=2
  return x, y

def move_player():
    jack.x += jack.vol[0]/speed
    jack.y += jack.vol[1]/speed
    pos=warp(jack.x, jack.y) 
    jack.x = pos[0]
    jack.y = pos[1]

    
# colliction
invisibility_duration = 60 # duration after taking damage in frames
# and idk how to spell invisibility but i think im at least consistent


def check_if_collide(hitbox1, hitbox2):
     for i in hitbox2:
       if i[0] > hitbox1[0][0] and i[0]<hitbox1[1][0]:
         if i[1] > hitbox1[0][1] and i[1] < hitbox1[1][1]:
           return "dead" #for some reason it returns "dead" I guess you could check an if and the "dead" would reaturn true but idk orkar change it so I write this comment insted

def player_collition(player_hitbox, invis, frame_count): # invis is the frame you last got invisibility
    if invis < frame_count - invisibility_duration:
        for i in astroids:
             if check_if_collide(player_hitbox,((i[0], i[1]), (i[0] + astroid_hitbox, i[1] + astroid_hitbox))) == "dead":
                  return False
    return True

def shot_collition():
    n = 0
    n1 = 0
    for a in astroids:
        for i in shots:
            if check_if_collide(((a[0], a[1]), (a[0] + astroid_hitbox, a[1] + astroid_hitbox)), ((round(i[0]), round(i[1])), (1, 1))):
                del astroids[n]
                del shots[n1]
            n1 += 1
        n1 = 0
        n += 1

def collectable_collition(player_hitbox, framecount):
    n=0
    for i in collectables:
        if check_if_collide(player_hitbox, ((i.pos), (i.pos[0] + col_size, i.pos[1] + col_size))) == "dead":
            i.if_collected(framecount)
            collectables.pop(n)
            if i.__class__ == Collectable:
                spawn_collectable()
        n+=1


# Extra
spam = 20


shots = []

speed_of_bullet = 5

bullet_size = 6


def spawn_shot():
    shots.append([jack.x, jack.y, jack.angle-math.pi])


def render_shot():
    i=0
    for n in shots:
      
      vec = math.sin(shots[i][2]), math.cos(shots[i][2])
      
      x = shots[i][0]
      y = shots[i][1]
      x += vec[0] * speed_of_bullet
      y += vec[1] * speed_of_bullet
      shots[i][0] = x
      shots[i][1] = y
      if x < 0 or y < 0 or x > tile*screen_size[0] or y > tile*screen_size[1]:
          shots.pop(i)
        
      i +=1

      pygame.draw.rect(window, (255, 0, 0), (x, y, bullet_size, bullet_size))

#collecatble

col_size = 10

collectables = [] # is not only for Collectable its also for Powerup

def render_collectables():
    for i in collectables:
        i.render()

def random_pos(width, hight):
    return (random.randint(10, width), random.randint(10, hight))

class Collectable:
    col_num = 0
    def __init__(self, pos):
        self.pos = pos
    def render(self):
        pygame.draw.rect(window, (255, 0, 255), (self.pos[0], self.pos[1], col_size, col_size))
    def if_collected(self, framecount):
        self.__class__.col_num += 1 #is deleted outside the function


def spawn_collectable():
    x = Collectable(random_pos(screen_size[0] * tile - 10, screen_size[1] * tile - 10 ))
    collectables.append(x)

#powerup

spawn_freq = 1200 #in frames

pow_size = col_size # Powerup size equals size in pixels of collectable 

powerup_length = 300 #in frames (60 fps)

powerup_shooting = 5 #changes spam (rate of fire) when in powerup state

class Powerup:
    last_collected = powerup_length * -1
    def __init__(self, pos):
        self.pos = pos
    def render(self):
        pygame.draw.rect(window, (0, 0, 255), (self.pos[0], self.pos[1], pow_size, pow_size))
    def if_collected(self, framecount):
        self.__class__.last_collected = framecount

def spawn_powerup():
    x = Powerup(random_pos(screen_size[0] * tile - 10, screen_size[1] * tile - 10 ))
    collectables.append(x)

#health bar
HEALTH_BAR_Y_OFSET = 20 # how many pixels the origin of the health bar from the top
HEALTH_BAR_X_OFSET = 10 # same as y ofset but for x
HEALTH_BAR_WIDTH = 10 # y width of health bar pixels
HEALTH_BAR_LENGTH = tile * screen_size[1] - 20  #x leangth of the health bar
  
class Health_bar:
    def __init__(self, x, y, length, width, health ): # check konstants
        self.__edge_pos__ = ((x, y) , (x + length, y+ width))  #bounds of the healthbar
    def render(self):
        return 0


#screens

def game_over():
        print("Your score was:", Collectable.col_num)
        pygame.quit()

#main loop
diff = 500

def main_loop():
    spamu = spam
    j = False
    clock = pygame.time.Clock()
    framecount = 0
    for i in range(1):
        spawn_astroid()
        spawn_collectable()
        spawn_powerup()
    game = True
    astro=3
    chance=1000
    invisibility_frame = 0 # the frame when you last got invicibility from taking damage
    while game:
        clock.tick(60)
        framecount+=1
        j=check_keys(framecount, j, spamu)
        move_player()
        graphics()
        player_hitbox = ((jack.x - 30, jack.y - 30), (jack.x + 30, jack.y + 30))
        # need to split this in to multipule functions
        if not player_collition(player_hitbox, invisibility_frame, framecount):#fuck for some reason i spelld frame count with framecount when i should have done frame_count wich i do inside the function it would be an esy fix but idk.
            jack.health -= 1
            invisibility_frame = framecount
        if jack.health <= 0:
            game = False
        shot_collition()
        collectable_collition(player_hitbox, framecount)
        if Powerup.last_collected + powerup_length  > framecount:
            spamu = powerup_shooting
        else:
            spamu = spam
        if Powerup.last_collected + spawn_freq < framecount:
            if len(collectables) == 1:
                spawn_powerup()
        if framecount/chance == round(framecount/chance):
            spawn_astroid()
        if framecount/diff == round(framecount/diff):
          chance = round(chance/ 1.25)
        if framecount/600 == round(framecount/600):
            print(clock.get_fps())

main_loop()
game_over()


#i mean im pretty good at comenting but i just work with an old and shit project that i didnt know what to do with 
