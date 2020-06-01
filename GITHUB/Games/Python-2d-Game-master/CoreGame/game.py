from _ast import Set

import pygame
import random
import time



from CoreGame import Settings

WIDTH = Settings.WITDH    # Largura
HEIGHT = Settings.HEIGHT  # ALTURA
FPS = 60
PGC = 0

# define cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Inicializa o PYGAME e cria a Janela

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceShipPy")
clock = pygame.time.Clock()


#Instaciar e carregar imagens pro SPRITE


meteors = []

if Settings.currentlevel <= 3:
    meteor_list1 =['meteorBrown_big1.png','meteorBrown_med1.png',
              'meteorBrown_med1.png','meteorBrown_med3.png',
              'meteorBrown_small1.png','meteorBrown_small2.png',
              'meteorBrown_tiny1.png']

if Settings.currentlevel == 4:
    meteor_list1 =['whiskey.png','whiskey.png','whiskey.png','whiskey.png','whiskey.png','whiskey.png','whiskey.png']

if Settings.currentlevel == 5:
    meteor_list1 =['b1.png','b2.png','b3.png','b4.png','b1.png','b2.png','b3.png']

if Settings.currentlevel == 6:
    meteor_list1 =['Creditos1.png','Creditos2.png','Creditos3.png','Creditos4.png','Creditos5.png','Creditos4.png','Creditos3.png','Creditos2.png']


if Settings.currentlevel == 6:
    inimigo_img = pygame.image.load((Settings.inimigoslist[Settings.currentlevel][0])).convert()
else:
    inimigo_img = pygame.image.load((Settings.inimigoslist[Settings.currentlevel])).convert()


boss_img = pygame.image.load((Settings.bosslist[Settings.currentlevel])).convert()
boss1_img = pygame.image.load('dario1.png').convert()
boss2_img = pygame.image.load('dario2.png').convert()

img_dir = ((__file__), "Laser.png")
tiroIni_img = pygame.image.load(("Laser.png")).convert()

img_dir = ((__file__), "laser2.png")
tiro_img = pygame.image.load(("laser2.png")).convert()

if Settings.currentlevel > 6:
    mob_img = pygame.image.load((meteor_list1[random.randrange(0,5)])).convert()

if Settings.currentlevel == 6:

    mob_img = pygame.image.load((meteor_list1[random.randrange(0,6)]))






background = pygame.image.load(Settings.backimg[Settings.currentlevel])



shoot_sound = pygame.mixer.Sound('lasersound.wav')
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(snd))
pygame.mixer.music.load(Settings.ostlist[Settings.currentlevel])
pygame.mixer.music.set_volume(0.5)

background_rect = background.get_rect()


#carregar pro Player
player_img = pygame.image.load(Settings.NAVIMG).convert()



spawnini = Settings.INILOCAL

for img in meteor_list1:
    meteors.append(pygame.image.load((img)).convert())


#Explosoes

explosion_anim = {}
explosion_anim['grande'] = []
explosion_anim['pequena'] = []
explosion_anim['player'] = []

for i in range(9):
    expi = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(expi).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['grande'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['pequena'].append(img_sm)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(filename).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)

powerup_images = {}
powerup_images['shield'] = pygame.image.load('shield_gold.png').convert()
powerup_images['gun'] = pygame.image.load('bolt_gold.png').convert()


class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = tiro_img
        self.image = pygame.transform.scale(tiro_img, (15, 500))

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.centerx = player.rect.centerx
        self.rect.bottom = player.rect.top
        keystate = pygame.key.get_pressed()
        if not keystate[pygame.K_m]:
            self.kill()



class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y,d):
        pygame.sprite.Sprite.__init__(self)
        self.image = tiro_img
        self.image = pygame.transform.scale(tiro_img, (8, 10))

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -Settings.disparo
        self.direc = d

    def update(self):
        self.rect.y += self.speedy

        if self.direc == 1:
            self.rect.x += self.speedy +7
        elif self.direc == 2:
            self.rect.x -= self.speedy +7

        # kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()


class BulletIni(pygame.sprite.Sprite):
    def __init__(self, x, y,d):
        pygame.sprite.Sprite.__init__(self)
        self.image = tiro_img
        self.image = pygame.transform.scale(tiroIni_img, (8, 10))

        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -5
        self.direc = d

    def update(self):
        self.rect.y -= self.speedy

        if self.direc == 1:
            self.rect.x += self.speedy +7
        elif self.direc == 2:
            self.rect.x -= self.speedy +7

        # kill if it moves off the top of the screen
        print(self.rect.y)
        if self.rect.y > HEIGHT + 20:
            print("kill")
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = player_img
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.image_orig = pygame.transform.scale(player_img, (50, 52))
        self.image = self.image_orig.copy()

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -Settings.velocidade
        if keystate[pygame.K_RIGHT]:
            self.speedx = Settings.velocidade
        self.rect.x += self.speedx

        self.speedy = 0
        if keystate[pygame.K_UP]:
            self.speedy = -Settings.velocidade
        if keystate[pygame.K_DOWN]:
            self.speedy = Settings.velocidade
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self,powerup):
        if powerup == 1:
            bullet = Bullet(self.rect.centerx, self.rect.top, 0)
            all_sprites.add(bullet)
            bullets.add(bullet)
            shoot_sound.play()

        elif powerup == 2:
            bullet = Bullet(self.rect.centerx - 10, self.rect.top, 0)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet1 = Bullet(self.rect.centerx + 10, self.rect.top, 0)
            all_sprites.add(bullet1)
            bullets.add(bullet1)
            shoot_sound.play()

        elif powerup >= 3:
            bullet = Bullet(self.rect.centerx - 20, self.rect.top, 1)
            all_sprites.add(bullet)
            bullets.add(bullet)
            bullet1 = Bullet(self.rect.centerx, self.rect.top, 0)
            all_sprites.add(bullet1)
            bullets.add(bullet1)
            bullet3 = Bullet(self.rect.centerx + 20, self.rect.top, 2)
            all_sprites.add(bullet3)
            bullets.add(bullet3)
            shoot_sound.play()



    def laser(self):
        laser = Laser(self.rect.centerx, self.rect.top)
        all_sprites.add(laser)
        lasers.add(laser)





class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image = pygame.image.load((meteor_list1[random.randrange(0,6)]))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        self.image.set_colorkey(BLACK)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center


class Inimigos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 12))
        self.image = inimigo_img

        if Settings.currentlevel == 6:
            PGC =+ 1
            if PGC > 10:
                PGC = 0
            self.image = pygame.image.load((Settings.inimigoslist[Settings.currentlevel][PGC])).convert()




        if Settings.currentlevel == 6:
            self.image = pygame.transform.scale(inimigo_img, (400, 400))
        else:
            self.image = pygame.transform.scale(inimigo_img, (50, 50))

        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .20 / 2)
        self.image.set_colorkey(BLACK)
        r = random.randrange(0,2)
        self.rect.x = spawnini[r]
        self.rect.y = random.randrange(20, 300)
        self.speedy = 1
        if r == 0:
            self.speedx = 5
        else:
            self.speedx = -5


        self.i = 0

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.speedx *= -1
        elif self.rect.left < 0:
            self.speedx *= -1

        if self.rect.bottom > HEIGHT - 300:
            self.speedy*=-1
        elif self.rect.top < 0:
            self.speedy*=-1




        self.i +=1


        if self.i % Settings.frequencia_tiros_inimigos[Settings.currentlevel] == 0:
            self.shoot()

    def shoot(self):
        bullet4 = BulletIni(self.rect.centerx, self.rect.bottom , 0)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)



class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((150, 150))
        self.image = boss_img
        self.image = pygame.transform.scale(boss_img, (150, 150))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .20 / 2)
        self.image.set_colorkey(BLACK)
        r = random.randrange(0,2)
        self.rect.x = 1
        self.rect.y = 2
        self.speedy = 0.5
        if r == 1:
            self.speedx = 1
        else:
            self.speedx = -1


        self.i = 0


    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 30 or self.rect.left < -45 or self.rect.right > WIDTH + 40:
            self.speedx *= -1
        elif self.rect.left < 0:
            self.speedx *= -1




        self.i +=1

        if self.i % Settings.frequencia_tiros_inimigos[Settings.currentlevel] == 0:
            self.shoot()


    def shoot(self):
        bullet4 = BulletIni(self.rect.centerx, self.rect.bottom , 0)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
        bullet4 = BulletIni(self.rect.centerx - 20, self.rect.bottom, -1)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
        bullet4 = BulletIni(self.rect.centerx, self.rect.bottom, 0)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
        bullet4 = BulletIni(self.rect.centerx + 20, self.rect.bottom, -2)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
        bullet4 = BulletIni(self.rect.centerx + 40, self.rect.bottom, -4)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
        bullet4 = BulletIni(self.rect.centerx + 60, self.rect.bottom, -8)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
        bullet4 = BulletIni(self.rect.centerx + 80, self.rect.bottom, -10)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
        bullet4 = BulletIni(self.rect.centerx + 100, self.rect.bottom, -12)
        all_sprites.add(bullet4)
        bulletsIni.add(bullet4)
       # shootboss_sound.play()

class PoweShield(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = ('shield')
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the bottom of the screen
        if self.rect.top > HEIGHT:
            self.kill()

class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = ('gun')
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the bottom of the screen
        if self.rect.top > HEIGHT:
           self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center





font_name = pygame.font.match_font('Chandas')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / Settings.vidas) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
def newinim():
    ini = Inimigos()
    all_sprites.add(ini)
    inimigos.add(ini)

def newboss():
    bos = Boss()
    all_sprites.add(bos)
    bosses.add(bos)


def crash(frase):
    run = True
    draw_text(screen, str(frase), 120, WIDTH / 2, HEIGHT/2)
    i=0
    while run:
        i+=1
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()

        # gameDisplay.fill(white)

        if i==50:
            return False


        pygame.display.update()
        clock.tick(15)





mobs = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
bosses = pygame.sprite.Group()
if Settings.currentlevel < 6:
    player = Player()


all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bulletsIni = pygame.sprite.Group()
powerups = pygame.sprite.Group()
lasers = pygame.sprite.Group()

if Settings.currentlevel < 6:
    all_sprites.add(player)

shieldpowerups = pygame.sprite.Group()



pontos = 0
pygame.mixer.music.play(loops=-1)

# Game loop
game_over = True
tempinho=0
i=0
pup = 1
contador = Settings.vidas
bs = 0
fim=0
lifeboss = 0
cooldown = 0
vitoria = False
running = True
boleano = False
frase = "jogo"
while running:


    i+=1
    tempinho+=1
    #if game_over:
        #show_go_screen()
    # keep loop running at the right speed
    clock.tick(FPS)
    if len(bulletsIni) > 1000:
        FPS += 10
    else:
        FPS = 60
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot(pup)
            if event.key == pygame.K_m:
                player.laser()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_m:
                mobs.add(lasers)

#PROGRESSAO DE INIMIGOS E NO FIM ENDBOSS



    if tempinho > 300:
        if (tempinho - 300) % (200/(Settings.currentlevel+1)) == 0:
            newinim()

    if tempinho % (500/(Settings.currentlevel+1)) == 0:
        for i in range(5):
            newmob()


    if tempinho == 8200:
        newboss()

    if tempinho == 3000 and Settings.currentlevel == 4:
        newboss()

    if tempinho == 82 and Settings.currentlevel == 6:
        newboss()

    if tempinho == 4082 and Settings.currentlevel == 6:
        running = False


    # Update
    all_sprites.update()


    if bs == 29:
        bs=0
    else:
        bs+=1

    print("Tempo::")
    print(tempinho)

    # check to see if a bullet hit a mob
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)

    for hit in hits:
        pontos += 100 - hit.radius
        random.choice(expl_sounds).play()
        mob_img = pygame.image.load((meteor_list1[random.randrange(0, 5)])).convert()
        expl = Explosion(hit.rect.center, 'grande')
        all_sprites.add(expl)
        if random.randint(1, 30)  == Settings.prob_de_dropar_shield:  # Integer from 1 to 10
            sh = PoweShield(hit.rect.center)
            all_sprites.add(sh)
            shieldpowerups.add(sh)

    if Settings.currentlevel < 6:

        hits = pygame.sprite.spritecollide(player, bulletsIni, True)

        if hits:
            if cooldown == 0:
                expl = Explosion(player.rect.center,'pequena')
                all_sprites.add(expl)
                contador -=1

            if contador == 0:
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.kill()
                boleano = True
                frase = "Game Over! Fraquinho"





            if contador == -1:
                running = False


            cooldown = 60

    if Settings.currentlevel < 6:
        hits = pygame.sprite.spritecollide(player, mobs, True)
        if hits:
            if cooldown == 0:
                expl = Explosion(player.rect.center,'pequena')
                all_sprites.add(expl)
            if contador == 0:
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.kill()
                boleano = True
                frase = "Game Over! Ceguinho!"


            contador -= 1
            cooldown = 60
            
    if Settings.currentlevel < 6:


        hits = pygame.sprite.spritecollide(player, inimigos, True)
        if hits:
            if cooldown == 0:
                expl = Explosion(player.rect.center,'pequena')
                all_sprites.add(expl)
                contador -= 1
                cooldown = 60

                if contador == 0:
                    death_explosion = Explosion(player.rect.center, 'player')
                    all_sprites.add(death_explosion)
                    player.kill()
                    boleano = True
                    frase = "Game Over! Tótó!"


    if boleano:
        fim+=1
        if fim == 70:
            running = False
            running = crash(frase)

    hits = pygame.sprite.groupcollide(inimigos, bullets, True, True)
    for hit in hits:
        pontos += 500 - hit.radius
        random.choice(expl_sounds).play()
        expl = Explosion(hit.rect.center, 'grande')
        all_sprites.add(expl)
        if random.random() > 0.9:
            pow = Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)

    hits = pygame.sprite.groupcollide(bosses, bullets, False, True)
    for hit in hits:
        pontos += 10
        lifeboss += 1

        if lifeboss >= Settings.total_vida_boss[Settings.currentlevel]*0.25 and lifeboss <= Settings.total_vida_boss[Settings.currentlevel]*0.35:
            random.choice(expl_sounds).play()
            expl = Explosion(hit.rect.center, 'pequena')
            all_sprites.add(expl)
            if Settings.currentlevel == 4:
                bosses.sprites()[0].image = pygame.transform.scale(boss1_img, (150, 150))
                bosses.sprites()[0].image.set_colorkey(BLACK)


        if lifeboss >= Settings.total_vida_boss[Settings.currentlevel]*0.75 and lifeboss <= Settings.total_vida_boss[Settings.currentlevel]*0.80 :

            random.choice(expl_sounds).play()
            expl = Explosion(hit.rect.center, 'grande')
            all_sprites.add(expl)
            if Settings.currentlevel == 4:
                bosses.sprites()[0].image = pygame.transform.scale(boss1_img, (150, 150))
                bosses.sprites()[0].image.set_colorkey(BLACK)


        if lifeboss == Settings.total_vida_boss[Settings.currentlevel]:

            death_explosion = Explosion(hit.rect.center, 'player')
            all_sprites.add(death_explosion)
            random.choice(expl_sounds).play()
            all_sprites.add(death_explosion)
            all_sprites.remove(bosses)
            vitoria = True
            boleano = True
            frase = "Ganhou!! Parabens"

            if Settings.LEVELUNLOCKED[(len(Settings.LEVELUNLOCKED) - 1)] == Settings.currentlevel:
                if Settings.currentlevel != 4:
                    Settings.LEVELUNLOCKED.append(Settings.currentlevel + 1)



    hits = pygame.sprite.groupcollide(mobs, lasers, True, False)

    if Settings.currentlevel < 6:
        hits = pygame.sprite.spritecollide(player, powerups, True)
        if hits:
            pup +=1

        hits = pygame.sprite.spritecollide(player, shieldpowerups, True)
        if hits:
            contador +=1





    # Draw / render
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    if Settings.currentlevel < 6:

        draw_shield_bar(screen, 5, 5, contador)
    # *after* drawing everything, flip the display
    pygame.display.flip()






time.sleep(1)
pygame.quit()