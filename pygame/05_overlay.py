import pygame
import time

# Initialisierung von Pygame
pygame.init()

# Bildschirmgröße (nur die Breite wird benötigt)
screen_width = 200
screen_height = 30  # Höhe anpassen

# Erstelle das Overlay-Fenster mit transparentem Hintergrund
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)  # Ohne Transparenz
pygame.display.set_caption("Overlay")

# Schriftart initialisieren
font = pygame.font.Font(None, 36)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Aktuelle Zeit abrufen
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min
        current_second = current_time.tm_sec

        # Berechne die verbleibende Zeit bis zur nächsten viertel Stunde (15 oder 45)
        if current_minute < 15:
            target_minute = 15
        elif current_minute < 45:
            target_minute = 45
        else:
            target_minute = 15  # Nächste Stunde, nächstes Ziel ist 15

        remaining_minutes = (target_minute - current_minute) % 60
        remaining_seconds = 60 - current_second

        # Anzeige erstellen (Surface mit Transparenz)
        overlay_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

        # Zeige die aktuelle Uhrzeit und die verbleibende Restzeit an
        time_text = f"{current_hour:02d}:{current_minute:02d}:{current_second:02d}"
        rest_time_text = f"Restzeit: {remaining_minutes:02d}:{remaining_seconds:02d}"
        combined_text = f"{time_text} {rest_time_text}"

        text_render = font.render(combined_text, True, (255, 255, 255))
        overlay_surface.blit(text_render, (10, 0))

        # Setze die Transparenz des Overlays
        overlay_surface.set_alpha(200)  # Ein Wert von 0 bis 255 (0 = transparent, 255 = voll sichtbar)

        # Overlay auf den Bildschirm blitten
        screen.blit(overlay_surface, (0, 0))

        pygame.display.update()

        # Warte einen Moment, bevor die Schleife erneut durchlaufen wird
        pygame.time.wait(1000)

    pygame.quit()

if __name__ == "__main__":
    main()
