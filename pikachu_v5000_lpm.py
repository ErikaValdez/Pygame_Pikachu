import pygame,random
pygame.init()

ancho=800
alto=600
negro=(0,0,0)
blanco=(255,255,255)
rojo=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
plomo=(232,224,224)

pantalla=pygame.display.set_mode((ancho,alto))
icono= pygame.image.load("assets/poke.png")
pygame.display.set_caption("Pokemon")
pygame.display.set_icon(icono)
reloj=pygame.time.Clock() #reloj para controlar los fps

#fuentes
pequeñafuente=pygame.font.SysFont("comicsansms",15)
medianafuente=pygame.font.SysFont("comicsansms",30)
grandefuente=pygame.font.SysFont("comicsansms",50)
font = pygame.font.SysFont('Consolas', 30)

#datos de boton
boton1=(300,290)
tamboton=(200,45)
colorboton1=[plomo,rojo]
boton2=(300,340)
colorboton2=[plomo,rojo]
boton3=(300,390)
colorboton3=[plomo,rojo]
#datos de los botones en Ganador
boton4=(150,300)
colorboton4=[plomo,rojo]
boton9=(150,250)
colorboton9=[plomo,rojo]
#datos de los botones en  Fin de juego
boton5=(450,300)
colorboton5=[plomo,rojo]
boton6=(450,200)
colorboton6=[plomo,rojo]
boton7=(450,250)
colorboton7=[plomo,rojo]
#datos del boton en Controles
boton8=(300,450)
colorboton8 =[plomo,rojo]

def Texto1(superficie, texto, talla, x, y):
	fuente = pygame.font.SysFont("arialblack", talla)
	texto_superficie = fuente.render(texto, True,negro)
	texto_rect = texto_superficie.get_rect()
	texto_rect.midtop = (x,y)
	superficie.blit(texto_superficie, texto_rect)

def Barra_Vida(superficie, x, y, porcentaje):
	Largo_Barra = 100
	Alto_Barra = 10
	relleno = round((porcentaje / 100) * Largo_Barra)
	borde = pygame.Rect(x, y, Largo_Barra, Alto_Barra)
	relleno = pygame.Rect(x, y, relleno, Alto_Barra)
	pygame.draw.rect(superficie, verde, relleno)
	pygame.draw.rect(superficie, blanco, borde, 2)

class Jugador(pygame.sprite.Sprite):
	def __init__(self):     #inicializar la clase
		super().__init__()
		self.image = pygame.image.load("assets/p3.png").convert()  #cargar imagen
		self.image.set_colorkey(blanco)  #quitar fondo de la imagen
		self.rect = self.image.get_rect()
		self.rect.centerx = ancho // 2
		self.rect.bottom = alto - 5
		self.speed_x = 0  #velocidad 
#		self.shield = 100

	def update(self):
		self.speed_x = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speed_x = -5
		if keystate[pygame.K_RIGHT]:
			self.speed_x = 5
		self.rect.x += self.speed_x
		if self.rect.right > ancho:
			self.rect.right = ancho
		if self.rect.left < 0:
			self.rect.left = 0

	def Disparo(self):
		rayo = Rayo(self.rect.centerx, self.rect.top)
		all_sprites.add(rayo)
		rayos.add(rayo)
		laser_sound.play()

class Pokebol(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(pokebol_imagenes)
		self.image.set_colorkey(blanco)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(ancho - self.rect.width)
		self.rect.y = random.randrange(-140, -100)
		self.speedy = random.randrange(1, 5)
		self.speedx = random.randrange(-2, 2)

	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > alto + 10 or self.rect.left < -40 or self.rect.right > ancho + 40:
			self.rect.x = random.randrange(ancho - self.rect.width)
			self.rect.y = random.randrange(-140, - 100)
			self.speedy = random.randrange(1, 5)

class Pokebol2(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(pokebol_imagenes)
		self.image.set_colorkey(blanco)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(ancho - self.rect.width)
		self.rect.y = random.randrange(-140, -100)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-2, 2)

	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > alto + 10 or self.rect.left < -40 or self.rect.right > ancho + 40:
			self.rect.x = random.randrange(ancho - self.rect.width)
			self.rect.y = random.randrange(-140, - 100)
			self.speedy = random.randrange(1, 10)

class Pokebol3(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = random.choice(pokebol_imagenes)
		self.image.set_colorkey(blanco)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(ancho - self.rect.width)
		self.rect.y = random.randrange(-140, -100)
		self.speedy = random.randrange(1, 15)
		self.speedx = random.randrange(-2, 2)

	def update(self):
		self.rect.y += self.speedy
		self.rect.x += self.speedx
		if self.rect.top > alto + 10 or self.rect.left < -40 or self.rect.right > ancho + 40:
			self.rect.x = random.randrange(ancho - self.rect.width)
			self.rect.y = random.randrange(-140, - 100)
			self.speedy = random.randrange(1, 15)


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

class Rayo(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.image.load("assets/rayoo.PNG")
		self.image.set_colorkey(negro)
		self.rect = self.image.get_rect()
		self.rect.y = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()

pokebol_imagenes = []
pokebol_lista = ["assets/great3.png", "assets/master2.png","assets/safari1.png","assets/poke1.png","assets/ultra2.png"]
for img in pokebol_lista:
	pokebol_imagenes.append(pygame.image.load(img).convert())

####----------------EXPLOSTION IMAGENES --------------
explosion_anim = []
for i in range(9):
	file = "assets/regularExplosion0{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(negro)
	img_scale = pygame.transform.scale(img, (70,70))
	explosion_anim.append(img_scale)

#Cargar imagenes
background = pygame.image.load("assets/back.jpg").convert()
pausa1=pygame.image.load("assets/pausar.jpg").convert()
perdio=pygame.image.load("assets/perdio.jpg").convert()
credits=pygame.image.load("assets/cred.jpg").convert()
menu=pygame.image.load("assets/fondito.png").convert()
gano=pygame.image.load("assets/gana.png").convert()
nivel2= pygame.image.load("assets/3.png").convert()
nivel3= pygame.image.load("assets/4.jpg").convert()

# Cargar sonidos
laser_sound = pygame.mixer.Sound("assets/pika.ogg")
#explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
pygame.mixer.music.load("assets/music1.ogg")
perder=pygame.mixer.Sound("assets/triste.ogg")
cmenu=pygame.mixer.Sound("assets/menu.ogg")
vict=pygame.mixer.Sound("assets/victoria.ogg")
pygame.mixer.music.set_volume(0.1)
cmenu.set_volume(0.1)
vict.set_volume(0.1)


all_sprites = pygame.sprite.Group()
pokebol_lista = pygame.sprite.Group()
rayos = pygame.sprite.Group()
jugador = Jugador()
all_sprites.add(jugador)

for i in range(8):
	pokebol = Pokebol()
	all_sprites.add(pokebol)
	pokebol_lista.add(pokebol)

#Marcador / Score
score = 0
suma = 0


#----temporizador -----
counter, text = 3, '3'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)


def puntos(marcador):
	mensaje=tamaño="mediano".render("Puntos:  "+ str(marcador),True,negro)
	pantalla.blit(perder,[0,0])


def textoboton(msg,color,botonx,botony,ancho,alto,tamaño="pequeño"):
	textosuperficie,textorect=objetotexto(msg,color,tamaño)
	textorect.center=(botonx+ round(ancho/2),botony+round(alto/2))
	pantalla.blit(textosuperficie,textorect)

def botones(texto,superficie,estado,posicionamiento,tam,identidad=None):
	cursor=pygame.mouse.get_pos()
	click =pygame.mouse.get_pressed()

	if posicionamiento[0]+tam[0] > cursor[0] > tam[0] and posicionamiento[1]+ tam[1] > cursor[1] > tam[1] and posicionamiento[1] +tam[1] < cursor[1] + tam[1]:
		if click[0] ==1:
			if identidad == "comienzo":
				gameloop()
			elif identidad == "configuracion":
				opciones()
			elif identidad == "salir":
				quit()
			elif identidad == "Volver al menu":
				introduccion()
			elif identidad == "salirPerder":
				quit()
			elif identidad == "VolveralmenuOpciones":
				introduccion()
				
		boton = pygame.draw.rect(superficie,estado[1],(posicionamiento[0],posicionamiento[1],tam[0],tam[1]))
		textoboton(texto,blanco,posicionamiento[0],posicionamiento[1],tam[0],tam[1])
	else:
		boton = pygame.draw.rect(superficie,estado[0],(posicionamiento[0],posicionamiento[1],tam[0],tam[1]))
		textoboton(texto,negro,posicionamiento[0],posicionamiento[1],tam[0],tam[1])
	return boton

def fin_juego():
	fin =True
	pygame.mixer.music.pause()
	perder.play(loops=-1)
	while fin:
		pantalla.blit(perdio,[0,0])
		Texto1(pantalla,"¡Perdiste!",40,550,100)
		Texto1(pantalla,"Tu puntuacion obtenida fue: " + str(suma), 20,550,180)
		#mensaje("¡Perdiste! ",blanco,-200,tamaño="grande")
		#mensaje("Tu puntuacion obtenida fue:  " + str(suma),blanco,-150,tamaño="mediano")
		botones("Salir",pantalla,colorboton5,boton5,tamboton,identidad="salirPerder")
		botones("Ir al menu",pantalla,colorboton7,boton7,tamboton,identidad="Volver al menu")
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					introduccion()
					fin=False
				if event.key == pygame.K_x:
					quit()
				if event.type == pygame.QUIT:
					fin=True

def objetotexto(texto,color,tamaño):
	if tamaño == "pequeño":
		textosuperficie = pequeñafuente.render(texto,True,color)
	if tamaño == "mediano":
		textosuperficie = medianafuente.render(texto,True,color)
	if tamaño == "grande":
		textosuperficie = grandefuente.render(texto,True,color)
	return textosuperficie, textosuperficie.get_rect()


def mensaje(msg,color,desplazamientoy=0,tamaño="pequeño"):
	textosuperficie, textorect= objetotexto(msg,color,tamaño)
	textorect.center = round(ancho/2), round(alto/2)+desplazamientoy
	pantalla.blit(textosuperficie,textorect)

def pausa():
	pausado=True
	pygame.mixer.music.pause()
	while pausado:
		reloj.tick(60)
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_F1:
					pausado=False
					pygame.mixer.music.unpause()
				if event.key==pygame.K_F2:
					quit()
		pantalla.blit(pausa1,[0,0])
		Texto1(pantalla,"Pausa",50,400,50)
		Texto1(pantalla,"Presione: ",30,400,210)
		Texto1(pantalla," F1 para continuar",30,400,260)
		Texto1(pantalla," F2 para salir",30,400,310)
		pygame.display.flip()


def introduccion():

	intro=True
	cmenu.play()
	pygame.mixer.Sound.stop(perder)
	pygame.mixer.Sound.stop(vict)
	pantalla.blit(menu,[0,0])
	while intro:
		pygame.mixer.music.stop()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro=False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_s:
					gameloop()
					intro=False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					opciones()
					intro=False	
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_x:
					intro=False		

			botones("Jugar",pantalla,colorboton1,boton1,tamboton,identidad="comienzo")
			botones("Controles",pantalla,colorboton2,boton2,tamboton,identidad="configuracion")
			botones("Salir",pantalla,colorboton3,boton3,tamboton,identidad="salir")
			Texto1(pantalla,"¡Pikachu debe sobrevivir!",35,300,170)
			pygame.display.update()
			reloj.tick(60)


def opciones():
	pygame.mixer.Sound.stop(cmenu)
	waiting = True
	while waiting:
		for action in pygame.event.get():
			if action.type == pygame.KEYDOWN:
				if action.key == pygame.K_x:
					introduccion()
			pantalla.blit(credits,[0,0])
			mensaje(" CONTROLES ",negro,-220,tamaño="grande")
			mensaje(" Movimiento hacia la izquierda = Flecha izquierda ",blanco,-150,tamaño="mediano")
			mensaje(" Movimiento hacia la derecha = Flecha derecha",blanco,-100,tamaño="mediano")
			mensaje(" Disparos = space",blanco,-50,tamaño="mediano")
			mensaje(" Pausa = p",blanco,0,tamaño="mediano")  
			botones("Volver al menu",pantalla,colorboton8,boton8,tamboton,identidad="VolveralmenuOpciones")
			pygame.display.flip()



def ganador():
	fin =True
	pygame.mixer.music.pause()
	vict.play()
	while fin:
		pantalla.blit(gano,[0,0])

		Texto1(pantalla,"¡Ganaste!",50,250,100)
		Texto1(pantalla,"Tu puntuacion obtenida fue: "+ str(suma),25,250,200)
		botones("Salir",pantalla,colorboton4,boton4,tamboton,identidad="salirPerder")
		botones("Ir al menu",pantalla,colorboton9,boton9,tamboton,identidad="Volver al menu")
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					introduccion()
					fin=False
				if event.key == pygame.K_x:
					quit()
				if event.type == pygame.QUIT:
					fin=True


def temporizador(): 
	
	pygame.mixer.Sound.stop(perder)
	counter =4
	global text

	var = True 
	while var:
		for event in pygame.event.get():
			if event.type == pygame.USEREVENT:
				counter-= 1
				text =str(counter).rjust(3)if counter > 0 else "A jugar!"	
				if counter ==0:
					break
		else:
			pantalla.blit(background,[0,0])
			pantalla.blit(font.render(text, True, (negro)), (350,200))
			pygame.display.flip()
			continue
		break



def gameloop():

	jugador.vida =100
	salir=True
	score = 0
	global suma
	temporizador()
	pygame.mixer.music.play(loops=-1)
	pygame.mixer.Sound.stop(cmenu)
	pygame.mixer.Sound.stop(perder)

	while salir:
		reloj.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salir=False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					jugador.Disparo()
				if event.key == pygame.K_p:	 
					pausa()

		all_sprites.update()

		# Colisiones pokebola - rayo

		hits = pygame.sprite.groupcollide(pokebol_lista,rayos, True, True)
		for hit in hits:
			score += 1
			explosion = Explosion(hit.rect.center)
			all_sprites.add(explosion)

			pokebol = Pokebol()
			all_sprites.add(pokebol)
			pokebol_lista.add(pokebol)
			suma =suma+1
			if score>=10:
				temporizador()
				gameloop2()



		# Colisiones jugador - pokebola

		hits = pygame.sprite.spritecollide(jugador, pokebol_lista, True)
		for hit in hits:
			jugador.vida -= 25
			pokebol = Pokebol()
			all_sprites.add(pokebol)
			pokebol_lista.add(pokebol)
			if jugador.vida <= 0:
				fin_juego()

		
		pantalla.blit(background, [0, 0])
		all_sprites.draw(pantalla)
		# Marcador
		Texto1(pantalla, str(score), 25, 770, 10)
		Texto1(pantalla,"nivel 1",30,400,10)

		# ESCUDO.
		Barra_Vida(pantalla, 5, 5, jugador.vida)

		pygame.display.flip()


def gameloop2():

	#player.shield =100
	salir=True
	score = 10
	global suma
	while salir:
		reloj.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salir=False

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					jugador.Disparo()
				if event.key == pygame.K_p:	
					pausa()

		all_sprites.update()

		# Colisiones pokebola - rayo

		hits = pygame.sprite.groupcollide(pokebol_lista,rayos, True, True)
		for hit in hits:
			score += 1
			explosion = Explosion(hit.rect.center)
			all_sprites.add(explosion)
			pokebol = Pokebol2()
			all_sprites.add(pokebol)
			pokebol_lista.add(pokebol)
			suma =suma+1
			if score>=30:
				temporizador()
				gameloop3()

		# Colisiones jugador - pokebola

		hits = pygame.sprite.spritecollide(jugador, pokebol_lista, True)
		for hit in hits:
			jugador.vida -= 25
			pokebol = Pokebol2()
			all_sprites.add(pokebol)
			pokebol_lista.add(pokebol)
			if jugador.vida <= 0:
				fin_juego()


		pantalla.blit(nivel2, [0, 0])
		all_sprites.draw(pantalla)
		# Marcador
		Texto1(pantalla, str(score), 25, 770, 10)
		Texto1(pantalla,"nivel 2",30,400,10)

		# ESCUDO.
		Barra_Vida(pantalla, 5, 5, jugador.vida)

		pygame.display.flip()


def gameloop3():

	salir=True
	score = 30
	global suma

	while salir:
		reloj.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salir=False

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					jugador.Disparo()
				if event.key == pygame.K_p:	
					pausa()

		all_sprites.update()

		# Colisiones pokebola - rayo

		hits = pygame.sprite.groupcollide(pokebol_lista,rayos, True, True)
		for hit in hits:
			score += 1
			explosion = Explosion(hit.rect.center)
			all_sprites.add(explosion)
			pokebol = Pokebol3()
			all_sprites.add(pokebol)
			pokebol_lista.add(pokebol)
			suma =suma+1
			if score>=50:
				ganador()

		# Colisiones jugador - pokebola

		hits = pygame.sprite.spritecollide(jugador, pokebol_lista, True)
		for hit in hits:
			jugador.vida -= 25
			pokebol = Pokebol3()
			all_sprites.add(pokebol)
			pokebol_lista.add(pokebol)
			if jugador.vida <= 0:
				fin_juego()


		pantalla.blit(nivel3, [0, 0])
		all_sprites.draw(pantalla)
		# Marcador
		Texto1(pantalla, str(score), 25, 770, 10)
		Texto1(pantalla,"nivel 3",30,400,10)

		# ESCUDO.
		Barra_Vida(pantalla, 5, 5, jugador.vida)

		pygame.display.flip()



introduccion()
quit()
gameloop()
gameloop2()
gameloop3()
temporizador()




