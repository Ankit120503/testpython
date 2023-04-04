RED = "red"

BLUE = "blue"

YELLOW = "yellow"

color_1=input("Enter First color name:")
color_2=input("Enter Second color name:")
if color_1 != RED and color_1 != BLUE and color_1 != YELLOW:
    print("Error: Invalid Color1", color_1)
elif color_2 != RED and color_2 != BLUE and color_2 != YELLOW:
    print("Error: Invalid Color2")
elif color_1==color_2:
    print("Error: The two colors you entered are same.")
else:
    if color_1==RED and color_2==BLUE:
        print("purple")
    elif color_1==RED and color_2==YELLOW:
        print("orange")
    elif color_1==BLUE and color_2==RED:
        print("purple")
    elif color_1==BLUE and color_2==YELLOW:
        print("green")
    elif color_1==YELLOW and color_2==RED:
        print("orange")
    elif color_1==YELLOW and color_2==BLUE:
        print("green")
