import sys, pygame

# Spiel initialisieren
pygame.init()
size = width, height = 1280, 768
screen = pygame.display.set_mode(size)

# Variablen definieren

# Farben definieren
black = 0, 0, 0 # Farbe schwarz
blue = 0, 0, 255 # Farbe blau
yellow = 255, 255, 0 # Farbe gelb

# Variablen für die Bewegung
speed = 100 # Pixel pro Sekunde die sich der Ball bewegt
x, y = 1, 1 # Richtung in der sich der Ball bewegt ( initial rechts unten)
last_time = pygame.time.get_ticks()

# Variablen für die FPS
clock = pygame.time.Clock()

# Sprites
# Ball laden
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

# Spiel Schleife
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    frame_time = pygame.time.get_ticks() 

    diff_time = frame_time - last_time
    last_time = frame_time

    # print("diff_time", diff_time)


    variable = diff_time // speed # speed ist die Geschwindigkeit
    variable = speed / 1000 * diff_time 

    # Prüfen ob der Ball aus dem Bildschirm fliegt
    # diffx = 



    strecke = [ variable*x , variable*y ] # Setze die Geschwindigkeit auf die Variable

    ballrect = ballrect.move(strecke)
    # print(ballrect.left, ballrect.right, ballrect.top, ballrect.bottom )
    
    if ballrect.left < 0:
        x = 1 
    elif ballrect.right > width:
        x = -1 
    if ballrect.top < 0:
        y = 1
    elif ballrect.bottom > height:
        y = -1


    screen.fill(black)
    screen.blit(ball, ballrect)
    # FPS auf dem Bildschirm ausgeben
    # print FPS to screen
    font = pygame.font.SysFont("Arial", 18)
    text = font.render("FPS: " + str(round(clock.get_fps())), True, pygame.Color("coral"))
    # Text ausgeben in der Farbe coral
    screen.blit(text, (0, 0))
    clock.tick(144)

    pygame.display.flip()
