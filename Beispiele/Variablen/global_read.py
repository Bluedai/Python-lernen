#!/usr/bin/env python3

# wenn man die globale Variable nur lesen möchte kann man die in funktionen einfach nutzen

my_var = 1

def print_my_var():
    print("Die Variable ist", my_var)

def my_funktion():
    print_my_var()

my_funktion()