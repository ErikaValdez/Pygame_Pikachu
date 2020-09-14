import pygame, random

WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = (0, 255, 0)
RED =(255,0,0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon")
icono= pygame.image.load("assets/poke.png")
pygame.display.set_icon(icono)
clock = pygame.time.Clock()

def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, RED)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (round(x), round(y))
	surface.blit(text_surface, text_rect)

def draw_shield_bar(surface, x,y, percentage):
	BAR_LENGHT = 100
	BAR_HEIGHT = 10
	fill = (percentage / 100) * BAR_LENGHT
	border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
	fill = pygame.Rect(x,y, fill, BAR_HEIGHT)
	pygame.draw.rect(surface, GREEN, fill)
	pygame.draw.rect(surface, WHITE, border, 2)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("assets/p3.png").convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH // 2
		self.rect.bottom = HEIGHT - 10
		self.speed_x = 0
		self.shield = 100

	def update(self):
		self.speed_x = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -5
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0

	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet)
		bullets.add(bullet)
		laser_sound.play()

class Pokebol(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(pokebol_images)
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-140, -100)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > HEIGHT + 10 or self.rect.left < -40 or self.rect.right > WIDTH + 40:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-140, - 100)
			self.speedy = random.randrange(1, 10)

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("assets/rayito1.PNG")
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()

class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = explosion_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center 
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50 # VELOCIDAD DE LA EXPLOSION

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_anim):
				self.kill()
			else:
				center = self.rect.center
				self.image = explosion_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center


def show_go_screen():
	screen.blit(menu, [0,0])
	draw_text(screen, " Pikachu debe sobrevivir ",40, 400, 30)
	draw_text(screen, "Press Key", 30, 435, 450)
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		pygame.init()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYUP:
				waiting = False



def pausa():
    pausado=True
    pygame.mixer.music.pause()
    while pausado:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    pygame.mixer.music.unpause()
                    pausado=False
                    
                #if event.key==pygame.K_r:
                    #show_go_screen()
        screen.fill(BLACK)
        draw_text(screen,"PAUSED",100,400,30)
        draw_text(screen,"PRESS c TO CONTINUE",50,500,300)
        pygame.display.flip()
        clock.tick(60)

     

pokebol_images = []
pokebol_list = ["assets/great3.png", "assets/master2.png","assets/safari1.png","assets/poke1.png","assets/ultra2.png"]
for img in pokebol_list:
	pokebol_images.append(pygame.image.load(img).convert())


####----------------EXPLOSTION IMAGENES --------------
explosion_anim = []
for i in range(6):
	file = "assets/regularExplosion0{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(BLACK)
	img_scale = pygame.transform.scale(img, (70,70))
	explosion_anim.append(img_scale)

# Cargar imagen de fondo
background = pygame.image.load("assets/back.jpg").convert()
menu = pygame.image.load("assets/menu2.jpg").convert()
# Cargar sonidos
laser_sound = pygame.mixer.Sound("assets/pika.ogg")
explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
pygame.mixer.music.load("assets/music1.ogg")
pygame.mixer.music.set_volume(0.9)


#pygame.mixer.music.play(loops=-1)

#### ----------GAME OVER
game_over = True
running = True
while running:
	if game_over:

		show_go_screen()

		game_over = False
		all_sprites = pygame.sprite.Group()
		pokebol_list = pygame.sprite.Group()
		bullets = pygame.sprite.Group()

		player = Player()
		all_sprites.add(player)
		for i in range(8):
			pokebol = Pokebol()
			all_sprites.add(pokebol)
			pokebol_list.add(pokebol)

		score = 0
		pygame.mixer.music.play(loops=-1)


	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()
			if event.key == pygame.K_p:	
				pausa()
            

	all_sprites.update()

	#colisiones - pokebolas - rayos
	hits = pygame.sprite.groupcollide(pokebol_list, bullets, True, True)
	for hit in hits:
		score += 10
		#explosion_sound.play()
		explosion = Explosion(hit.rect.center)
		all_sprites.add(explosion)
		pokebol = Pokebol()
		all_sprites.add(pokebol)
		pokebol_list.add(pokebol)

	# Checar colisiones - jugador - pokebolas
	hits = pygame.sprite.spritecollide(player, pokebol_list, True)
	for hit in hits:
		player.shield -= 25
		pokebol = Pokebol()
		all_sprites.add(pokebol)
		pokebol_list.add(pokebol)
		if player.shield <= 0:
			game_over = True
			pygame.mixer.music.stop()

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	#Marcador
	draw_text(screen, str(score), 25, 770, 10)

	# Escudo.
	draw_shield_bar(screen, 5, 5, player.shield)

	pygame.display.flip()
pygame.quit()
