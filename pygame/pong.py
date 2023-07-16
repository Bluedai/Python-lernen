#!/usr/bin/env python3

import sys
# import time
import random
import math
import pygame
# import pygame_gui

# Spiel Engine initialisieren
pygame.init()

# Konfiguration
Vollbild=False

# Farben definieren
schwarz = 0, 0, 0 # Farbe schwarz
blau = 0, 0, 255 # Farbe blau
gelb = 255, 255, 0 # Farbe gelb
weiß = 255, 255, 255 # Farbe weiß
rot = 255, 0, 0 # Farbe rot
regenbogen = [(255, 0, 0),    # Rot
          (0, 255, 0),    # Grün
          (0, 0, 255),    # Blau
          (255, 255, 0),  # Gelb
          (255, 0, 255),  # Magenta
          (0, 255, 255),  # Cyan
          (128, 0, 0),    # Dunkelrot
          (0, 128, 0),    # Dunkelgrün
          (0, 0, 128),    # Dunkelblau
          (128, 128, 128) # Grau
         ]


# Farben für das Spiel
farbe_background = schwarz
farbe_spieler = weiß
farbe_ball = blau
farbe_line = gelb
farbe_fps = gelb
farbe_fps_background = farbe_background

# Variablen für die FPS
view_fps = False
clock = pygame.time.Clock()

# Variablen für die Bewegung
dt = 0 


# Funktionen
# gestrichelte Linie zeichnen
def gestrichelte_linie_zeichnen(farbe, start, ende, breite, länge, abstand):
    # Berechne die Länge der gesamten Linie
    dx = ende[0] - start[0]
    dy = ende[1] - start[1]
    linienlänge = int( (dx**2 + dy**2)**0.5 )
    angle = math.atan2(dy, dx)
    hilfslänge = linienlänge + abstand
    hilfsende_x = start[0] + hilfslänge * math.cos(angle)
    hilfsende_y = start[1] + hilfslänge * math.sin(angle)
    dx = hilfsende_x - start[0]
    dy = hilfsende_y - start[1]
    linienlänge = int( (dx**2 + dy**2)**0.5 )

    # Berechne die Anzahl der Striche
    anzahl_striche = linienlänge // (länge + abstand)

    # Berechne den Abstand zwischen den Strichen
    dx = dx / anzahl_striche
    dy = dy / anzahl_striche
    dxa = dx / (länge + abstand) * abstand
    dya = dy / (länge + abstand) * abstand

    # Zeichne die Striche
    for i in range(anzahl_striche):
        startx = start[0] + dx * i
        starty = start[1] + dy * i
        endex = start[0] + dx * (i+1) - dxa
        endey = start[1] + dy * (i+1) - dya  
        pygame.draw.line(screen, farbe, (startx, starty), (endex, endey), breite)


# Spielfeld zeichnen
def Spielfeld_zeichnen():
    # Rahmen
    pygame.draw.rect(screen, farbe_line, ( 0,0,screen.get_width(),screen.get_height()), int(randabstand/1.5) )
    # Netz
    netzstart = (screen.get_width() / 2 , 0)
    netzende = (screen.get_width() / 2, screen.get_height())
    if screen.get_height() < 500:
        la = (10,5)
    elif screen.get_height() < 1000:
        la = (20,10)
    else:
        la = (40,20)
    gestrichelte_linie_zeichnen(farbe_line, netzstart, netzende, 3, la[0], la[1])

class Spieler:
    def __init__(self, höhe, breite, farbe, position, tasten):
        self.player_höhe = höhe
        self.player_breite = breite
        self.farbe = farbe
        self.position = position.copy()
        self.tasten = tasten
    def zeichnen(self):
        pygame.draw.rect(screen, self.farbe, (self.position[0], self.position[1], self.player_breite, self.player_höhe))
        # pygame.draw.circle(screen, self.farbe, (int(self.position[0]), int(self.position[1])), 5)
    def bewegen(self,keys):
        if keys[self.tasten[0]]:
            self.position.y -= int(300 * dt)
        if keys[self.tasten[1]]:
            self.position.y += int(300 * dt)
        if keys[self.tasten[2]]:
            self.position.x -= int(300 * dt)
        if keys[self.tasten[3]]:
            self.position.x += int(300 * dt)

class Ball:
    def __init__(self, farbe, position):
        self.radius = 10
        self.farbe = farbe
        self.position = position.copy()
        self.geschwindigkeit = 400
        self.angle = random.uniform(-math.pi, math.pi)

    def zeichnen(self):
        pygame.draw.circle(screen, self.farbe, (int(self.position.x), int(self.position.y)), self.radius)

    def bewegen(self):
        # Berechne die Verschiebung in x- und y-Richtung basierend auf dem Winkel und der Geschwindigkeit
        dx = self.geschwindigkeit * math.cos(self.angle) * dt
        dy = self.geschwindigkeit * math.sin(self.angle) * dt

        # Aktualisiere die Position des Balls
        self.position.x += dx
        self.position.y += dy

        # Prüfe, ob der Ball rechts das Spielfeld verlässt
        if self.position.x > screen.get_width() - randabstand - self.radius:
            self.position.x = screen.get_width() - randabstand - self.radius 
            # Neuen Winkel setzen (Einfallswinkel umkehren)
            self.angle = math.pi - self.angle

        # Prüfe, ob der Ball links das Spielfeld verlässt
        if self.position.x < 0 + randabstand + self.radius:
            self.position.x = 0 + randabstand + self.radius 
            # Neuen Winkel setzen (Einfallswinkel umkehren)
            self.angle = math.pi - self.angle

        # Prüfe, ob der Ball oben das Spielfeld verlässt
        if self.position.y < 0 + randabstand + self.radius:
            self.position.y = 0 + randabstand + self.radius 
            # Neuen Winkel setzen (Einfallswinkel umkehren)
            self.angle = -self.angle

        # Prüfe, ob der Ball unten das Spielfeld verlässt
        if self.position.y > screen.get_height() - randabstand - self.radius:
            self.position.y = screen.get_height() - randabstand - self.radius 
            # Neuen Winkel setzen (Einfallswinkel umkehren)
            self.angle = -self.angle


        # Prüfe, ob der Ball mit einem Spieler kollidiert
        for spieler in Spieler_Liste:
            if spieler.position.x < self.position.x < spieler.position.x + spieler.player_breite:
                if spieler.position.y < self.position.y < spieler.position.y + spieler.player_höhe:
                    if (math.pi/2)*-1 <= math.atan2(math.sin(self.angle), math.cos(self.angle)) <= (math.pi/2)*1:
                        if spieler.position.x > screen.get_width()/2:
                            self.angle = math.pi - self.angle
                    else:
                        if spieler.position.x < screen.get_width()/2: 
                            self.angle = math.pi - self.angle

# FPS auf dem Bildschirm ausgeben
def FPS_zeichnen():
    if view_fps:
        x_position = 30
        y_position = 10
        font = pygame.font.SysFont("Arial", 18)
        text = font.render("FPS: " + str(round(clock.get_fps())), True, farbe_fps)
        text_rect = text.get_rect()
        text_rect = text_rect.inflate(3, 0)  # Erweitert das Rechteck um 10 Pixel in alle Richtungen
        text_rect.topleft = (x_position, y_position)  # Ändere die Position des Hintergrundrechtecks
        pygame.draw.rect(screen, farbe_fps_background, text_rect)
        screen.blit(text, (x_position +1 , y_position))  # Zeichne den Text

# Vollbild/Fenster erstellen
if Vollbild:
    # Wenn man (0,0) angibt, dann wird die Bildschirmauflösung des Desktops verwendet
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN, display=1)
else:
    screen = pygame.display.set_mode((800,600),pygame.RESIZABLE, display=1)
pygame.display.set_caption("Bluedai Pong")

# Muss leider hinter dem Fenster erstellen stehen, das muss noch aufgeräumt werden, das gehört hier nicht hin
# Ausserdem müssen sich einige Werte dynamisch an die Fenstergröße anpassen

# Variablen für Spieler
player_höhe = 100
player_breite = 20
randabstand = screen.get_width() * 0.01

# Spieler A
player_A_pos = pygame.Vector2(randabstand , screen.get_height() / 2 - player_höhe / 2)

# Spieler B
player_B_pos = pygame.Vector2(screen.get_width() - randabstand - player_breite , screen.get_height() / 2 - player_höhe / 2)



# Hauptschleife des Spiels
running = True
rungame = False
while running:
    # Clear screen
    screen.fill(farbe_background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_f]:
        view_fps = not view_fps
    if keys[pygame.K_ESCAPE]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))  # Manuell das QUIT-Event erzeugen

    # Spiel starten
    if keys[pygame.K_g]:
        rungame = True
        Spieler_Liste = []
        Ball_Liste = []
        spieler_links = Spieler(player_höhe, player_breite, farbe_spieler, player_A_pos, (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d))
        Spieler_Liste.append(spieler_links)
        spieler_rechts = Spieler(player_höhe, player_breite, farbe_spieler, player_B_pos, (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT))
        Spieler_Liste.append(spieler_rechts)
        ball = Ball(farbe_ball, pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2) )
        Ball_Liste.append(ball)

    # Spiel stoppen
    if keys[pygame.K_h]:
        rungame = False
        spieler_links = None
        spieler_rechts = None

    # Spieler + Ball bewegen
    if rungame:
        spieler_links.bewegen(keys)
        spieler_rechts.bewegen(keys)
        ball.bewegen()

    # Spielfeld zeichnen
    Spielfeld_zeichnen()

    # Spieler + Ball zeichnen
    if rungame:
        spieler_links.zeichnen()
        spieler_rechts.zeichnen()
        ball.zeichnen()

    FPS_zeichnen()

    dt = clock.tick(60) # max 144 Bilder pro Sekunde
    dt = dt / 1000 
    pygame.display.flip() # Aktualisiere den Bildschirm

pygame.quit()