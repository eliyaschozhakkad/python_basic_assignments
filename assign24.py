class Area:
    def circle(self):
        radius=int(input("Enter the radius\n"))
        area=3.14*radius*radius
        print(f"The area of circle is {area}")
    def square(self):
        length=int(input("Enter the length of square\n"))
        area=length*length
        print(f"The area of square is {area}")
    def rectangle(self):
        length=int(input("Enter the length\n"))
        breadth=int(input("Enter the breadth\n"))
        area=length*breadth
        print(f"The area of rectangle is {area}")
    def triangle(self):
        base=int(input("Enter the base\n"))
        height=int(input("Enter the height\n"))
        area=0.5*base*height
        print(f"The area of triangle is {area}")
class MyClass(Area):
    pass
myclass=MyClass()
choice=int(input("Enter your choice\n1.Circle\n2.Square\n3.Rectangle\n4.Triangle\n"))

match choice:
    case 1:
        myclass.circle()
    case 2:
        myclass.square()
    case 3:
        myclass.rectangle()
    case 4:
        myclass.triangle()
    case _:
        print("Invalid Entry")
