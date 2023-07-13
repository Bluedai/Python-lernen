#!/usr/bin/env python3
# In diesem Beispiel wird die Variable self.value innerhalb der Klasse gesetzt. 
# Die Variable self.value ist eine Instanzvariable und kann nur von der Instanz geändert werden.
# Innerhalb der Klasse gibt es allerdings Funktionen mit denen die Variable geändert werden kann.

class MyVariable:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print("Die Variable ist", self.value)

    def edit_value(self):
        self.value += 1

def my_funktion():
    my_var = MyVariable(1)
    my_var.print_value()
    my_var.edit_value()
    my_var.print_value()

my_funktion()
