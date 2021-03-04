# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country', 'drives_right']])

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.iloc[2])

# Print out observations for Australia and Egypt
print(cars.iloc[[1,6]])

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right value of Morocco
print(cars.loc['MOR'])

# Print sub-DataFrame
print(cars.iloc[[4, 5], [1, 2]])

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars.iloc[:,2])

# Print out drives_right column as DataFrame
print(cars.iloc[:,[2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.iloc[:, [0,2]])

# Comparison of booleans
print(True == False)

# Comparison of integers
print((-5*15) != 75)

# Comparison of strings
print('pyscript' == 'PyScript')

# Compare a boolean with an integer
print(True == 1)

# Comparison of integers
x = -3 * 6
print(x>=-10)


# Comparison of strings
y = "test"
print('test'<=y)

# Comparison of booleans
print(True>False)

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house>=18)

# my_house less than your_house
print(my_house<=your_house)

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen>10 and my_kitchen<18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen>14 or my_kitchen>17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen*2 < your_kitchen*3)

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house>18.5, my_house<10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house<11, your_house<11))

# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area>15  :
    print('big place!')

# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else :
    print('pretty small.')

# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area > 10 :
    print('medium size, nice!')
else :
    print("pretty small.")

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc>500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc>100, cpc<500)
medium = cars[between]

# Print medium
print(medium)

# Initialize offset
offset = 8

# Code the while loop
while offset != 0 :
    print('correcting...')
    offset = offset-1
    print(offset)

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset>0 :
      offset = offset-1
    else :
      offset = offset+1
    print(offset)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
for height in areas :
    print(height)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas) :
    print('room' + str(index) + ':' + str(area))

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))

