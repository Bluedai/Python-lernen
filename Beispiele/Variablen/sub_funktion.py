#!/usr/bin/env python3
# Damit eine Variable in einer Sub-Funktion genutzt werden kann, muss diese als Parameter übergeben werden.
# Um eine Variable in einer Funktion zu ändern, muss diese als Rückgabewert zurückgegeben werden.

def print_my_var(my_var):
    print("Die Variable ist", my_var)

def edit_my_var(my_var):
    my_var += 1
    return my_var

def my_funktion():
    my_var = 1
    print_my_var(my_var)
    my_var = edit_my_var(my_var)
    print_my_var(my_var)

my_funktion()