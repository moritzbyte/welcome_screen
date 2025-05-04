import tkinter as tk
from tkinter import font
import time 

time.sleep(3) #Pause machen
# Erstelle ein Fenster
root = tk.Tk()
root.title("INSERT DESIRED TEXT HERE")

# Fenstergröße und Hintergrundfarbe festlegen
root.geometry("900x600")
root.configure(bg="black")

# Schriftart für ByteBounce definieren (mit vollständigem Pfad zur TTF-Datei)
bytebounce_font = font.Font(family="ByteBounce", size=50)

# Label für die Begrüßungsnachricht erstellen
label = tk.Label(root, text="", font=bytebounce_font, fg="green", bg="black")
label.pack(expand=True)

# Funktion, um den Text von links nach rechts zu schreiben (animiert)
def type_writer_effect(text, index=0):
    if index < len(text):
        label.config(text=text[:index+1])  # Nur die ersten "index+1" Zeichen anzeigen
        root.after(80, type_writer_effect, text, index + 1)  # Nächsten Schritt nach 100ms

# Text, der eingeblendet werden soll
welcome_text = "INSERT DESIRED TEXT HERE"

# Den Effekt starten
type_writer_effect(welcome_text)

# Fenster nach 5 Sekunden schließen
root.after(5000, root.quit)

# Fenster anzeigen
root.mainloop()
