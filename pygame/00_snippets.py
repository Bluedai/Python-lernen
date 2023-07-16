# https://pygame-gui.readthedocs.io/en/latest/index.html

# screen = pygame.display.set_mode((displayInfo.current_w, displayInfo.current_h), pygame.FULLSCREEN, display=0)

# Bildschirmauflösung des Desktops ermitteln
# num_displays = pygame.display.get_num_displays()
# display_infoA = pygame.display.get_display_info(0)

# print("num_displays", num_displays)
# print("display_infoA", display_infoA)

#available_modes = pygame.display.list_modes()
# print("available_modes", available_modes)

# displayInfo = pygame.display.Info()
# print("displayInfo", displayInfo)

# Variablen für die Bewegung
# speed = 100 # Pixel pro Sekunde die sich der Ball bewegt
# x, y = 1, 1 # Richtung in der sich der Ball bewegt
# last_time = pygame.time.get_ticks()

# Sprites
# Ball laden
# ball = pygame.image.load("intro_ball.gif")
# ballrect = ball.get_rect()

# def key_read():
#     global last_keypress_time
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_ESCAPE]:
#         sys.exit()
#     if keys[pygame.K_f]:
#         if pygame.time.get_ticks() - last_keypress_time > debounce_time:
#             last_keypress_time = pygame.time.get_ticks()
#             return True
#     return False



def gestrichelte_linie_zeichnen(farbe, start, ende, breite, länge, abstand):
    farben = [(255, 0, 0),    # Rot
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
    farbe=0
    # Berechne die Länge der Linie
    dx = ende[0] - start[0]
    dy = ende[1] - start[1]
    linienlaenge = int( (dx**2 + dy**2)**0.5 )
    # Berechne die Anzahl der Striche
    anzahl_striche = linienlaenge // (länge + abstand)
    # debug 
    print("Länge x: ", dx)
    print("Länge y: ", dy)
    print("Länge: ", linienlaenge)
    print("Anzahl Striche: ", anzahl_striche)

    # Berechne den Abstand zwischen den Strichen
    dx = dx / anzahl_striche
    dy = dy / anzahl_striche
    dxl = dx / (länge + abstand) * länge
    dyl = dy / (länge + abstand) * länge
    dxa = dx / (länge + abstand) * abstand
    dya = dy / (länge + abstand) * abstand


    
    print("Länge dx: ", dx)
    print("Länge dy: ", dy)
    print("Länge dxl: ", dxl)
    print("Länge dyl: ", dyl)
    print("Länge dxa: ", dxa)
    print("Länge dya: ", dya)
    print("gegeprobe dx*:", dxl + dxa)
    print("gegeprobe dy*:", dyl + dya)

    # Zeichne die Striche
    for i in range(anzahl_striche):
        startx = start[0] + dx * i
        starty = start[1] + dy * i
        endex = start[0] + dx * (i+1) - dxa
        endey = start[1] + dy * (i+1) - dya  
        pygame.draw.line(screen, farben[farbe], (startx, starty), (endex, endey), breite)
        farbe = (farbe + 1) % len(farben)

        # pygame.display.flip() # Aktualisiere den Bildschirm
        #time.sleep(1)
