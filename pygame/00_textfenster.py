import pygame
import pygame_gui

pygame.init()

# Pygame-Fenster erstellen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("UIConsoleWindow Beispiel")

# GUI-Manager initialisieren
manager = pygame_gui.UIManager((width, height))

# UIConsoleWindow erstellen
console = pygame_gui.windows.UIConsoleWindow(pygame.Rect(50, 50, 700, 500),
                                             manager=manager,
                                             window_title="Konsolenfenster")

# Schleife zum Anzeigen des Fensters
running = True
while running:
    time_delta = pygame.time.Clock().tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

    manager.update(time_delta)
    screen.fill((255, 255, 255))  # Hintergrund löschen
    manager.draw_ui(screen)

    pygame.display.update()

# Pygame beenden
pygame.quit()
