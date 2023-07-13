#!/usr/bin/env python3
# In diesem Beispiel wird die Variable self.value innerhalb der Klasse gesetzt. 
# Die Variable self.value ist eine Instanzvariable und kann nur von der Instanz geändert werden.
# Innerhalb der Klasse gibt es allerdings Funktionen mit denen die Variable geändert werden kann.
# Zusätzlich zu dem Beispiel class.py werden hier von der Klasse zwei Instanzen erstellt.
# Die Instanzen sind zwei verschiedene Objekte, die unabhängig voneinander sind.
# Die Instanzen haben die gleichen Funktionen, aber unterschiedliche Werte.

class MyVariable:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print("Die Variable aus ",id(self)," ist", self.value)

    def edit_value(self):
        self.value += 1

def my_funktion():
    # 2 Instanzen erstellen
    my_A_var = MyVariable(1)
    my_B_var = MyVariable(1)

    # Beide Variableinstanzen ausgeben 
    my_A_var.print_value()
    my_B_var.print_value()

    # A+1 und B+2 
    my_A_var.edit_value()
    my_B_var.edit_value()
    my_B_var.edit_value()

    # Beide Variableinstanzen ausgeben 
    my_A_var.print_value()
    my_B_var.print_value()

    
my_funktion()
