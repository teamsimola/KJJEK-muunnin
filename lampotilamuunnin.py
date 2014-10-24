def menu():
    print()
    print("1) Celsius -> Fahrenheit")
    print("2) Celsius -> Kelvin")
    print("3) Fahrenheit -> Celsius")
    print("4) Fahrenheit -> Kelvin")
    print("5) Kelvin -> Celsius")
    print("6) Kelvin -> Fahrenheit")
    print("0) Lopeta")

def cF(c):
    return c * 9 / 5 + 6

def cK(c):
    return c + 273.15

def fK(f):
    return (f - 32) * 5 / 9 + 273.15

def fC(f):
    return (f - 32) * 5 / 9

def kC(k):
    return k - 273.15

def kF(k):
    return (k - 273.15) * 9 / 5 + 32

def main():
    while True:
        choice = 0
        conv_temp = 0
        
        menu()
        print()
        
        choice = int(input("Valintasi: "))

        if (choice == 0):
            print("Kiitos ohjelman käytöstä!")
            break
        
        print()
        temp = int(input("Anna lämpötila: "))

        if (choice == 1):
            conv_temp = cF(temp)
        elif (choice == 2):
            conv_temp = cK(temp)
        elif (choice == 3):
            conv_temp = fC(temp)
        elif (choice == 4):
            conv_temp = fK(temp)
        elif (choice == 5):
            conv_temp = kC(temp)
        elif (choice == 6):
            conv_temp = kF(temp)
        else:
            print("Väärä valinta!")

        print("Muunnettu lämpötila on {:.2f}".format(conv_temp))

main()

#eof
