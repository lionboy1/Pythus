#Calculating percentiles
#In this tutorial we want to figure out where most of our cost is.
#We keep spending money on gas and it would be good to know what amount, for example, does 80% of the gas bill fall under.


import numpy as np
import math as mt

daily_gas = [15,13,13.5,14.7,11.4, 17.80, 34.10, 21.67, 27.19, 31.33,16.02]

percentile = np.percentile(daily_gas, 80)
x = mt.ceil(percentile)
print(x)

#The printed result means that 80% of the gas bills cost less than $28.
#This is starting to reveal some good insight on our gas expense right?
