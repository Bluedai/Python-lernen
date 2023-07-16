import pygame
import pygame_gui

pygame.init()

# Pygame-Fenster erstellen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("UIFileDialog Beispiel")

# GUI-Manager initialisieren
manager = pygame_gui.UIManager((width, height))

# UIFileDialog erstellen
file_dialog = pygame_gui.windows.UIFileDialog(pygame.Rect(200, 200, 400, 300),
                                              manager=manager,
                                              window_title="Dateiauswahl",
                                              initial_file_path=".",
                                              allow_existing_files_only=True)

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
