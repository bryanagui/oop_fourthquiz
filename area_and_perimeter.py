import math
print("So you want to get the area or perimeter of a triangle, rectangle or circle?")
print("First, which do you want to calculate? \nA. Perimeter \nB.Area")
while True:
    calc_ch = input("Choice: ")
    if calc_ch.lower() == "a" or calc_ch.lower() == "b":
        break
    else:
        print("That's not in the choices!")
        continue

if calc_ch.lower() == "a":
    print("===============")
    print("You want their perimeter? Let's calculate them!")
    print("Triangles have three sides! Enter the length of those sides.")
    tri_a = float(input("Side A: "))
    tri_b = float(input("Side B: "))
    while True:
        tri_c = float(input("Side C: "))
        if (tri_a + tri_b) > tri_c:
            break
        else:
            print("Not a valid triangle! Please make sure that a + b > c")
            continue
    print("===============")

    print("Don't worry, the results will be there soon. Dimensions of the rectangle please.")
    rect_length = float(input("Length: "))
    rect_width = float(input("Width: "))
    print("===============")

    print("Circles are fun! What is the radius of yours?")
    circle_radius = float(input("Radius: "))
    print("===============")

    print("Here are your results:")
    print(f"Your Triangle's Perimeter: {tri_a + tri_b + tri_c}")
    print(f"Your Rectangle's Perimeter: {(rect_length + rect_width)*2}")
    print(f"Your Circle's Circumference: {2*math.pi*circle_radius}")

elif calc_ch.lower() == "b":
    print("===============")
    print("Their area is my job to calculate! Let's Go!")
    print("Triangles are fun! What's the base and the height of yours?")
    tri_base = float(input("Base: "))
    tri_height = float(input("Height: "))
    print("===============")

    print("Results will be there soon! Length and Width of your Rectangle please.")
    rect_length = float(input("Length: "))
    rect_width = float(input("Width: "))
    print("===============")

    print("Yay circles! Radius of your circle is?")
    circle_radius = float(input("Radius: "))
    print("===============")

    print("Here are your results:")
    print(f"Your Triangle's Area: {(tri_base * tri_height)/2}")
    print(f"Your Rectangle's Area: {rect_length * rect_width}")
    print(f"Your Circle's Area: {math.pi*(circle_radius**2)}")
