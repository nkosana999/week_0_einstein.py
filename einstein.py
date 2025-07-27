# function that that takes in mass as input and returns energy in joules.
def energy_calculator():
    mass = int(input("m: "))
    E = mass * (300000000)**2
    print("E:",E)

energy_calculator()
