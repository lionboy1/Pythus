import numpy as np
import math as mt

daily_gas = [15,13,13.5,14.7,11.4]

middle_number = np.median(daily_gas)
x= mt.ceil(middle_number)
print(x)
#print(middle_number)
