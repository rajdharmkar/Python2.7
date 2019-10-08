#dice rolling simulator; a die has six faces with 1 to 6 numbers written
#if a dice is rolled, any of the numbers 1 to 6 should appear randomly
#writing a program to simulate this behaviour

def die_simulator():
    import random
    print random.randint(1,6)


throw = die_simulator()
throw
