from turtle import Screen, Turtle #Import certain functions of the turtle library
#Adham Khalifa/ Jaidev Attawar/ Adil Nurmagambetov

def center():
    """Returns pen to center of the table
    
       Arguments: None
    """
    turta.up()
    turta.goto(-300,0)
    turta.down()
    turta.fd(length_table/2)
    turta.left(90)
    turta.up()
    turta.fd(width_top)
    turta.down()
    turta.right(90)


def table_top(length_table, width_top, color_table):
    """Draws the top of the table

       Arguments: 
       length_table: length of the table
       width_top: width of the top of the table
       color_table: color of the top of the table
    """
    turta.up()
    turta.goto(-300,0)
    turta.down()
    #Creates table top
    turta.begin_fill()
    turta.fd(length_table)
    turta.left(90)
    turta.fd(width_top)
    turta.left(90)
    turta.fd(length_table)
    turta.left(90)
    turta.fd(width_top)
    turta.left(90)
    turta.fillcolor(color_table)
    turta.end_fill()

def table_leg(width_leg, height_leg, color_leg):
    """Draws the leg of the table

       Arguments:
       width_leg: Width of the leg of the table
       height_leg: Height of the lef of the table
       color_leg: Color of the leg of table
    """
    #Creates first leg
    turta.begin_fill()
    turta.fd(width_leg)
    turta.right(90)
    turta.fd(height_leg)
    turta.right(90)
    turta.fd(width_leg)
    turta.right(90)
    turta.fd(height_leg)
    turta.right(90)
    turta.fillcolor(color_leg)
    turta.end_fill()
    turta.up()
    turta.down()

def plate(plate_size, plate_color):
    """Draws the plate on the table

       Arguments:
        plate_size: size of the plate
        plate_color: color of the plate
    """
    turta.begin_fill()
    turta.fd(plate_size*0.5)
    turta.left(10)
    turta.fd(plate_size*0.5)
    turta.left(170)
    turta.fd(plate_size*2)
    turta.right(180)
    turta.right(10)
    turta.fd(plate_size*0.5)
    turta.left(10)
    turta.fd(plate_size*0.5)
    turta.fillcolor(plate_color)
    turta.end_fill()
    turta.left(90)
    turta.up()
    turta.fd(plate_size*0.09)#Distance between plate and cake.
    turta.right(90)
    turta.down()


def cake(width_cake,length_cake,colorcake):#function which makes the cake
    """Draws the cakes layers
    
       Arguments:
       width_cake: width of the cake layer
       colorcake: color of cake
       length_cake: length of cake layer
    """
    turta.pencolor(colorcake)
    turta.fillcolor(colorcake)
    turta.begin_fill()
    turta.fd(length_cake/2)
    turta.left(90)
    turta.fd(width_cake)
    turta.left(90)
    turta.fd(length_cake/2)
    turta.left(90)
    turta.fd(width_cake)
    turta.right(90)
    turta.fd(length_cake/2)
    turta.right(90)
    turta.fd(width_cake)
    turta.right(90)
    turta.fd(length_cake/2)
    turta.end_fill()

def candle():                  #function to make candle
    """Draws the candle ontop of the cake
       Arguments: None
       """
    turta.pencolor("light blue")
    turta.fillcolor("light blue")
    turta.begin_fill()
    turta.fd(6)
    turta.left(90)
    turta.fd(50)
    turta.left(90)
    turta.fd(12)
    turta.left(90)
    turta.fd(50)
    turta.left(90)
    turta.fd(6)
    turta.end_fill()
    turta.up()
    turta.left(90)
    turta.fd(50)
    turta.right(90)
    turta.fd(6)
    turta.left(90)
    turta.fd(6)
    turta.down()
    #drawing the flame of the candle
    turta.pencolor("yellow")
    turta.fillcolor("yellow")
    turta.begin_fill()
    turta.circle(7, -180)
    turta.left(180)
    turta.right(30)
    turta.fd(12)
    turta.right(125)
    turta.fd(12)
    turta.right(120)
    turta.fd(12)
    turta.end_fill()


def icing(color_icing): #fuction to draw the icing using semi-circles
    """Draws the icing on the cake layers
       Arguments:
       color_icing: color of the icing
    """
    turta.up()
    turta.down()
    turta.right(90)
    turta.fd(length_cake/2)
    turta.left(90)
    dia_icing = length_cake/10
    rad_icing = dia_icing/2
    turta.pencolor(color_icing)
    turta.fillcolor(color_icing)
    #no_of_circles = 10
    turta.begin_fill()
    for n in range (0, 10):#Draws 10 semi circles as icing
        turta.circle(rad_icing, -180)
        turta.left(180)
    turta.end_fill()
    turta.up()
    turta.right(90)
    turta.down()

    

def draw_layers(num_layers):        #drawing layers of the cake along with the candle at the end
    """Draws the entire cake with the icing
       Arguments:
       num_layers: total number of layers of the cake"""
    global length_cake
    layer = 1
    if choice == "Yes" or choice == "yes": #asks user if they want the layers of the cake to be different.
        while layer <= num_layers:  # a while loop that will continue until current layer number is greater than the total number of layers asked for
            for color in colorlist: # a for loop that will keep drawing layers and icing of cake 
                cake(width_cake,length_cake,color)
                turta.left(90) 
                icing(color_icing)
                turta.fd(length_cake/2)   
                layer += 1 # counter that adds 1 for each layer of cake made
                length_cake = length_cake*0.8 # as we go up the cake the layers will get smaller, variable will keep getting updated and get smaller.
                
    else:
        while layer <= num_layers:
            cake(width_cake,length_cake,colorcake)
            icing(color_icing)
            layer += 1
            
    candle()   
 
def main():
    #global all variables to make accessible in all functions, rather than repeating parameters
    global length_table
    global width_top
    global width_cake
    global color_icing 
    global turta
    global choice
    global colorlist
    global colorcake
    global length_cake
    global plate_size
    width_top = int(input("Width of the table top (10 - 20): "))                        #Width of table
    length_table = int(input("Length of the table (200 - 600): "))                      #Length of table
    color_table = input("Color of table top: ")                                         #Color of table
    width_leg = int(input("Width of the leg (10 - 20): "))                              #Width of the leg
    height_leg = int(input("Height of the leg (100 - 150): "))                          #height of the leg
    color_leg = input("Color of the table leg: ")                                       #color of the leg
    plate_size = int(input("Size of the plate: (100 - 200) "))                          #size of the plate
    plate_color = input("Color of the plate: ")                                         #color ofthe plate
    width_cake = int(input("Enter the width of your cake (30 - 70): "))                 #width of the cake
    length_cake = float(input(f"Enter the size of cake between (10 - {plate_size}): ")) #length of the cake
    num_layers = int(input("How many cake layers you want to build (1 - 5): "))                 #total number of layers user wants
    color_icing = input("What color do you want the icing to be?: ")                    # color of the icing
    choice = (input("Do you want different colors for your cake? Yes/No: "))
    if choice == "Yes" or choice == "yes":
        colorlist = []   #color of different layers is stored in a list
        n = 1
        while n <= num_layers:  #while loop that will keep asking user for color of each layer, depends on how many layers user pucks
            layer_color = input("Enter the color for layer: ")
            colorlist.append(layer_color)# Attribute that add colors to colorlist
            n += 1  #counter for color
    elif choice == "No" or choice == "no":
        colorcake = input("Which color you want to your cake: ")
    sc = Screen()
    turta = Turtle()
    turta.speed(100)
    table_top(length_table, width_top, color_table) #Draws the the top of the table
    turta.fd(length_table*0.08)
    table_leg(width_leg, height_leg, color_leg) #Draws first leg
    turta.fd(length_table*0.08)
    table_leg(width_leg, height_leg*0.7, color_leg)#Draws second leg
    turta.fd(length_table*0.65)
    table_leg(width_leg, height_leg*0.7, color_leg)#Draws third leg
    turta.fd(length_table*0.08)
    table_leg(width_leg, height_leg, color_leg)#Draws last leg
    center()
    plate(plate_size, plate_color)#Draws the table
    draw_layers(num_layers)#draws the cake
    turta.up()
    turta.goto(-300,0)#Goes back to original position
    turta.down()

    sc.exitonclick()

if __name__ == "__main__":
    main()
