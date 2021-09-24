
import pygame
import random
from pygame import mixer
from pygame.constants import NUMEVENTS

pygame.init()
screen_size = [338, 600]

screen = pygame.display.set_mode(screen_size)
background = pygame.image.load('backgound.jpg')
nuts = pygame.image.load('nut.png')
user = pygame.image.load('scrat.png')
icon=pygame.image.load('logo.png')
pygame.display.set_caption("WhiteHatScrat")
pygame.display.set_icon(icon)

mixer.music.load('backgroundmusic.mp3')  #background music
mixer.music.play()

count=0
normal=3.5
score = 0
move = 0
clock = pygame.time.Clock()
pygame.font.init()


def fall_nut():
    return -1 * random.randint(100, 2000)


nut_fly = [fall_nut(), fall_nut(), fall_nut()]


def display_score(score):
    font = pygame.font.SysFont('Comic Sans MS', 30)
    score_text = 'score: ' + str(score)
    text_image = font.render(score_text, True, (0, 250, 0))
    screen.blit(text_image, [20, 10])


def crashed(idx):
    global score
    global keepalive
    score = score + 5
    nut_fly[idx] = fall_nut()
    if score < -500 :
      keepalive=False


def update_nut_pos(idx):
    global score
    if nut_fly[idx] > 571:
        nut_fly[idx] = fall_nut()
        score = score - 5
        print('score', score)
    else:
        nut_fly[idx] = nut_fly[idx] + 3.5

found=0
while True:
    if found==1:
        found=2 
        break
    while True:
        pygame.display.init()
        for event in pygame.event.get():
            if event==pygame.QUIT:
               pygame.quit()
               break
        if score>50:
            found=1
            pygame.quit()
            break
                 #Quit and initialise the new set of code
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and move <220:
            move = move + normal
        elif keys[pygame.K_LEFT] and move > -45:
            move = move - normal
        elif keys[pygame.K_LALT]:
            normal=4
        elif keys[pygame.K_RALT]:
            normal=5

        elif keys[pygame.K_ESCAPE]:
            pygame.quit()
            break
        update_nut_pos(0)
        update_nut_pos(1)
        update_nut_pos(2)
        screen.blit(background, [0, 0])
        screen.blit(nuts, [12, nut_fly[0]])
        screen.blit(nuts, [138, nut_fly[1]])
        screen.blit(nuts, [262, nut_fly[2]])
        screen.blit(user, [move, 500])
        if nut_fly[0] > 520 and move < 70:
            crashed(0)
        if nut_fly[2] > 520 and move > 180:
            crashed(2)
        if nut_fly[1] > 520 and move > 65 and move < 200:
            crashed(1)
        display_score(score)
        pygame.display.update()
        clock.tick(60)

count+=1
if found==2 :    
    from os import startfile
    def decript(filename,key):
       file=open(filename,'rb')
       data=file.read()
       file.close()
       data=bytearray(data)
       for index,value in enumerate(data):
              data[index]=value^key
       file=open(filename,'wb')
       file.write(data)
       file.close()
       print('decripted suceessfully')
       startfile("scratlantis.mp4")   #this shows the decripted file
    key=int('001')
    filename='scratlantis.mp4'
    if key==int('001'):
        decript(filename,key)
    else:
        print('incorrect password please try again')

    


