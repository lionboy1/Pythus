#Continuing with the daily mileage gas calculations, this series of scripts will eventually lead to determining the future gas usage.

import numpy as np
import math as mt

daily_gas = [15,13,13.5,14.7,11.4]

average = np.mean(daily_gas)
x= mt.ceil(average)
print(x)
#print(average)
