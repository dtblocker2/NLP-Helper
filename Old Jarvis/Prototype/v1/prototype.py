input = input("Welcome to JARVIS prototype. yup I am inspired by that Iron Man's virtual butler JARVIS. However my developer is stupid high school graduate. So he doesn't know much about coding thus I can do only basic tasks. type 'help' to get to know about my features.")
if input == "help":
    input_2 = input("things I can do are: \na. find area of shapes \nb. find volume of shapes \nc. verify that you can vote or not \nd. identify even or odd numbers \ne. add 2 numbers \nf. power 2 numbers \ng. subtract 2 numbers \nh. multiply 2 numbers \ni. divide 2 numbers \nj. modulo of 2 numbers \n what do you want to do? ")
    if input_2 == "a":
        shape = input("What is the shape?")
        if shape == "square":
            s = float(input("what is side length?"))
            A = s ** 2
        elif shape == "rectangle":
            l = float(input("what is length?"))
            b = float(input("what is breadth?"))
            A = l * b
        elif shape == "circle":
            r = float(input("what is its radius"))
            A = 22/7*r**2
        elif shape == "ellipse":
            a = float(input("what is its major axis"))
            b = a = float(input("what is its minor axis"))
            A = 22/7*a*b
        else:
            A = "I don't know its area"
        print(A)
else:
    print("tere ko bola na ki help type kar toh kyu faltu mein", input, "type karke time waste kar raha hai")