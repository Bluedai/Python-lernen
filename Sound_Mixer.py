
import pygame
import tkinter as tk


def play_audio(sound):
    sound.play()

def set_volume(sound,volume):
    vol = int(volume) / 100
    sound.set_volume(vol)

def exit_program():
    pygame.mixer.quit()
    root.destroy()

if __name__ == "__main__":
    # Initialisiere Pygame Mixer
    pygame.mixer.init()
    # pygame.mixer.set_num_channels(16) # default 8

    # Audio Objekte erstellen und Lautstärke setzen 
    sound_1 = pygame.mixer.Sound('audio/Lautstärke.mp3')
    set_volume(sound_1, 80) # default 100 
    sound_2 = pygame.mixer.Sound('audio/Fokuswarnung - Polyglot-1.mp3')
    set_volume(sound_2, 80) # default 100 

    # Erstelle Tkinter Fenster
    root = tk.Tk()
    root.title("Mixer Test")
    root.geometry("250x200")
    root.minsize(250, 200)

    # Erstelle control Frame
    control_frame = tk.Frame(root,borderwidth=1, relief="solid")
    control_frame.pack(padx=10, pady=10)

    # Frame für jede Zeile 
    Zeile1_frame = tk.Frame(control_frame,borderwidth=1, relief="solid")
    Zeile1_frame.pack(padx=10, pady=10)
    Zeile2_frame = tk.Frame(control_frame,borderwidth=1, relief="solid")
    Zeile2_frame.pack(padx=10, pady=10)

    # Erstelle Buttons und Regler
    button1 = tk.Button(Zeile1_frame, text='Play 1', command=lambda: play_audio(sound_1))
    button1.grid(row=0,column=0, padx=10)

    volume_scale1 = tk.Scale(Zeile1_frame, from_=0, to=100, orient='horizontal', command=lambda volume: set_volume(sound_1,volume))
    volume_scale1.set(80) # default 0 
    volume_scale1.grid(row=0, column=1, padx=10)

  
    button2 = tk.Button(Zeile2_frame, text='Play 2', command=lambda: play_audio(sound_2))
    button2.grid(row=0,column=0, padx=10)

    volume_scale2 = tk.Scale(Zeile2_frame, from_=0, to=100, orient='horizontal', command=lambda volume: set_volume(sound_2, volume))
    volume_scale2.set(80) # default 0
    volume_scale2.grid(row=0, column=1, padx=10)

    exit_button = tk.Button(root, text='Exit', command=exit_program)
    exit_button.pack()

    # Starte Tkinter event loop
    root.mainloop()
