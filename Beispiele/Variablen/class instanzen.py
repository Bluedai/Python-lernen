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
