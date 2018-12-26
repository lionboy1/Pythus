import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


daily_gas = [15,13,13.5,14.7,11.4]
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']

plt.plot(weekdays,daily_gas)
plt.title('My Average Daily cost of fuel')
plt.xlabel('Daily drive')
plt.ylabel('Average Daily Gas Consumption in Dollars')
plt.show()
