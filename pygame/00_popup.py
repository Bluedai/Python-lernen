import pygame
import pygame_gui

# Pygame initialisieren
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("UIConfirmationDialog Beispiel")

# GUI-Manager initialisieren
manager = pygame_gui.UIManager((width, height))

# UIConfirmationDialog erstellen
dialog = pygame_gui.windows.UIConfirmationDialog( rect=pygame.Rect(200, 200, 400, 200)
                                                 ,manager=manager
                                                 ,window_title="Bestätigung"
                                                 ,action_long_desc="Möchtest du fortfahren?"
                                                 ,object_id= "#confirmation_dialog_dialog"
                                                 ,action_short_name="Text OK Button"
                                                 ,blocking=False
                                                 )
fenster = pygame_gui.windows.UIConfirmationDialog(rect=pygame.Rect(200, 200, 400, 200)
                                                 ,manager=manager
                                                 ,window_title="Bestätigung"
                                                 ,action_long_desc="Möchtest du fortfahren?"
                                                 ,object_id="#fenster" 
                                                 ,blocking=False
                                                 )
# fenster = pygame_gui.windows.UIConfirmationDialog(rect=pygame.Rect(0, 0, 400, 200),
#                                                  manager=manager,
#                                                  window_title="Test 2",
#                                                  action_long_desc="testfenster"
#                                                  )
# hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
#                                              text='Say Hello',
#                                              manager=manager)

# Schleife zum Anzeigen des Fensters
running = True
while running:
    time_delta = pygame.time.Clock().tick(60) / 1000.0

    for event in pygame.event.get():

        # # debug
        # if event.type != pygame.MOUSEMOTION:
        #     if event: print('event:', event)
        #     if hasattr(event, 'type'): print('event.type:', event.type)
        #     if hasattr(event, 'ui_element'): print('event.ui_element', event.ui_element)
        #     print('---------------')

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            print("UI_BUTTON_PRESSED")
            #if hasattr(event, 'ui_element'): print('event.ui_element', event.ui_element)
            #if hasattr(event, 'ui_object_id'): print('event.ui_object_id', event.ui_object_id)



            # print("dialog", dialog.__dict__)
            # print("------------------") 
            # print('event.ui_element:', event.ui_element.__dict__)
            # print("------------------") 
            # print("dialog.confirm_button", dialog.confirm_button.__dict__)
            print("id:", event.ui_element.object_ids)

            if event.ui_element.object_ids == ['#dialog', '#close_button']:
                print("close_button")
            elif event.ui_element.object_ids == ['#dialog', '#confirm_button']:
                print("confirm_button")
            elif event.ui_element.object_ids == ['#dialog', '#cancel_button']:
                print("cancel_button")

            if event.ui_element == dialog.confirm_button:
                # Der Bestätigungs-Button wurde gedrückt
                print("Bestätigungs-Button von dialog wurde gedrückt!")
            elif event.ui_element == dialog.cancel_button:
                # Der Abbrechen-Button wurde gedrückt
                print("Abbrechen-Button von dialog wurde gedrückt!")

            # if event.ui_object_id == '#confirmation_dialog.#confirm_button':
            #     print('B')
            #     if event.ui_element == dialog.confirm_button:
            #         # Der Bestätigungs-Button wurde gedrückt
            #         print("Bestätigungs-Button wurde gedrückt!")
            #     elif event.ui_element == dialog.cancel_button:
            #         # Der Abbrechen-Button wurde gedrückt
            #         print("Abbrechen-Button wurde gedrückt!")

        manager.process_events(event)

    manager.update(time_delta)
    screen.fill((255, 255, 255))  # Hintergrund löschen
    manager.draw_ui(screen)

    pygame.display.update()

# Pygame beenden
pygame.quit()
