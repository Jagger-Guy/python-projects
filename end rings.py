import math 

constAREA = 4.317595034*(10**11)  # area of each ring
constOriginalRadius = 370720  # radius of the first ring
x = (0, 1)
radiuses = []  ## empty array that will store the radius of each ring

print(f"The end of the first ring is at {constOriginalRadius}. \nAs you get past the first 10 million blocks or so, you will have to travel a couple chunks to reach the start/end of a ring. \n")
num = int(input("Enter number of coordinates you want to generate. "))
choice = str(input("Save to file? (Y/N) "))
print("\n")

if choice.upper() == "Y":
    f = open("End rings.txt", "w")


def getRadius(count, radiuses):
    sumOfPreviousRadiuses = sum(radiuses)  # calculate the sum of the total radiuses that were found thus far
    count += 1  ## increment counter
    newRadius = math.sqrt((count*constAREA)/math.pi) - sumOfPreviousRadiuses - constOriginalRadius  # (1)
    return newRadius, count


for i in range(num):  # number of coordinates that will be generated
    x = getRadius(x[1], radiuses)  # x[1] is the counter incrementing each time, radiuses is the array being updated with an extra radius each time
    radiuses.append(x[0])  # add found radius to the array
    sumOfPreviousRadiuses = sum(radiuses) + constOriginalRadius
    
    output = ("Radius " + str(i) + ": " + str(x[0]) + "\n" + "Coordinate: " + str(sumOfPreviousRadiuses) + "\n" )
    
    if choice.upper() == "Y":
        f.write(output + "\n")
    else:
        print(output)


if choice.upper() == "Y":
    f.close()
    print("File name with 'End rings.txt' was created with the coordinates")




# (1): to find the radius of the second gap:
#      e.g: constArea = pi * (radius of first ring + radius of first gap) - constArea
#           since they have the same area.
#           square root and division by pi comes from doing the opposite operation of finding the area of a circle,
#           since we already know that.