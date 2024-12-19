# decorater  = a function that extends behaviour of another function 
#                modifying base func , pass the base func as an argument to decorater


#formula to make a decorater 

def add_sprinkle(func):
    def cherry(*args, **kwargs):   
       print("Cherry on top 🍒")
       func(*args, **kwargs)
    return cherry

def fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge ")
        func(*args, **kwargs)
    return wrapper

@add_sprinkle
@fudge        #decorter 
#base func
def ice(flavour):
    print(f"Here is ur {flavour} ice cream ")

ice("vanila")