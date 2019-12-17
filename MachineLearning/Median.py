#Now we are calculating which number is the middle. 
#It's easy with a small array but with dozens of values it's harder to spot without doing the math.
#Thankfully numpy will handle this again.

import numpy as np
import math as mt

daily_gas = [15,13,13.5,14.7,11.4]

middle_number = np.median(daily_gas)
x= mt.ceil(middle_number)
print(x)

