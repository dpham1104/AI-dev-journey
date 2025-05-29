tri1 = float(input("Enter triangle angle 1: "))
tri2 = float(input("Enter triangle angle 2: "))
tri3 = float(input("Enter triangle angle 3: "))

if (tri1 + tri2 + tri3 == 180) and (tri1 > 0 and tri2 > 0 and tri3 > 0):
    print("This is a valid triangle")
else:
    print("This is not a valid triangle")
