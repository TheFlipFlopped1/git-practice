from time import time

def somemath(thing1, thing2):
    print(f"Doing math to {thing1} and {thing2}...")
    if time() % 2 == 0:
        return(thing1 + thing2)
    else:
        return(thing1 - thing2)