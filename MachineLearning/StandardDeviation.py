#We are calculating the standard deviation.  
#This means how far away from the average number are the other numbers in the array?

import numpy as np
import math as mt

daily_gas = [15,13,13.5,14.7,11.4]

deviation = np.std(daily_gas)
x = mt.ceil(deviation)
print(x)

#The result is rounded to approximately within 2 units(in this case integers) of the average value.
