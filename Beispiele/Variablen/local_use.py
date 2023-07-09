#!/usr/bin/env python3

# locale Varibalen sind nur in der Funktion verfügbar und werden auch nicht an aufgerufene funktionen weitergegeben 

def print_my_var():
    my_var = 101
    print("Die SubVariable ist", my_var)

def my_funktion():
    my_var = 1
    print("Die locale Variable ist", my_var)
    print_my_var()
    print("Die locale Variable ist immer noch ", my_var)

my_funktion()