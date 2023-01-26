def getRectangleArea(lenght, width):
    return lenght * width

def getTriangleArea(base, height):
    return base * height / 2

def getCircleArea(radius):
    return radius * radius * 3.14

def main():
    shape = input("Please type 'R' for rectangle, 'T' for triangle, 'C' for Circle: ")
    
    if shape == "R":
        length = float(input("Enter the lenght: "))
        width = float(input("Enter the width: "))
        area = getRectangleArea(length,width)
    elif shape == "T":
            base = float(input("Enter the base:"))
            height = float(input("Enter the height:"))
            area = getTriangleArea(base,height)
    else:
        radius = float(input("Enter the radius: "))
        area = getCircleArea(radius)
    
    print(f'Area: {area}')

if __name__ == "__main__":
        main()           

