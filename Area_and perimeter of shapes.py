# low budget calculator
print("hello")
print("i'm a low budget calcultor")
print("I can calculate area and perimeters of circles, square, rectangle")
print("so what would you like to calculate out of this ?")

answer = input()

if answer == "area of square":
    print("input your lenth and breath " + " length first")
    length = int( input())
    breadht = int( input())
    squareA = length * breadht
    print( squareA)

elif answer == "perimeter of square":
    print("input your lenght")
    lenght = int( input())
    peri = (lenght + lenght + lenght + lenght)
    print(peri)

elif answer == "area of rectangle":
    print("input your length and width " + "length first")
    lent = int(input())
    width =int(input())
    areal = lent * width
    print(areal)

elif answer == "perimeter of rectangle":
    print("input your length and width")
    lenth = int(input())
    width = int( input())
    perim = 2*(lenth + width)
    print(perim)

elif answer == "area of circle":
    print("input your radius")
    radius =int( input())
    pi = 3.142
    arean = 2 * (radius * pi)
    print(round(arean, 1))

elif answer == "perimeter of circle":
    print("input your radius only")
    radii = int(input())
    pii = 22/7
    perimi = int(pii) * radii
    print(perimi)


