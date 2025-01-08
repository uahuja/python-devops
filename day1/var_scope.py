a = 5   
b = 7   # Global Variables

# Defining the functions.

def add():
    print ( a + b )

def sub():
    print ( a - b )

def new_add():
    b=10    # Local Variable. Highest priority inside the function even if the same variable is present outside. 
    print( a + b )

# Calling the functions. 

add();
sub();
new_add();

