tree = input("How many trees did you spot in 600ft^2 in Sacramento ") #Prompts the user for number of trees calculated over 600 square feet
tree = int(tree)
city = (100 * 100) * 5280
nol = 2788000000 / 360000 #First number is the number of feet squared in the 100 miles squared of Sacramento, the other is the number of the area calculated from
total = (nol * tree) #7744.44 are the number of 600 square foot lots in Sacramento City
actual = 418200 #Counted 54 trees in generic neighborhood within Sacramento City and multiplied by the number of lots within the city
print("The total you calculated " ,total, " compared to what we got ", actual)
