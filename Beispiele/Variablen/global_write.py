#!/usr/bin/env python3

# wenn man die globale Variable ändern möchte muss die Variable mit global schreibbar gemacht werden
# Es reicht aber dies in der funktion zu machen die die Variable ändern
# In diesem Beispiel ist es nicht nötig die Variable in my_funktion als global zu setzen, da sie nur über die edit Funktion verändert wird. 

my_var = 1

def print_my_var():
    print("Die Variable ist", my_var)

def edit_my_var():
    global my_var
    my_var += 1

def my_funktion():
    print_my_var()
    edit_my_var()
    print_my_var()
    edit_my_var()
    print_my_var()

my_funktion()