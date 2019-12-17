#Distributing the gas expense data over a histogram

%matplotlib notebook
import numpy as np
import matplotlib.pyplot as plt

daily_gas = [15,13,13.5,14.7,11.4, 17.80, 34.10, 21.67, 27.19, 31.33,16.02]

plt.xlabel("Cost($)")
plt.ylabel("# of bills")
plt.hist(daily_gas, 12) # 12 is the number of bars to distribute the data over.  The amount can be increased for visual fine tuning.
plt.show()
