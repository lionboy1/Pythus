#In this tutorial we are simulating a linear regression to predict our future bill.

%matplotlib notebook
from scipy import stats
import matplotlib.pyplot as plt

daily_gas = [15,13,13.5,14.7,11.4, 17.80, 34.10, 21.67, 27.19, 31.33,16.02] # y value
days = [1,2,3,4,5,6,7,8,9,10,11] # x value

slope, intercept, r, p, std_err = stats.linregress(days, daily_gas) # x and y values

def myfunc(days):
  return slope * days + intercept # basic school math: y = mx + b for calculating y based on slope and intercept.

mymodel = list(map(myfunc, days))

plt.xlabel("Cost($)")
plt.ylabel("# of bills")
plt.scatter( days, daily_gas) # First, create a scatter plot of the data
plt.plot( days, mymodel ) # Draw a regression line through the data.
plt.show()

#Looking a the trend, it seems that the gas bill has a decent chance of being > $25 
# although there was that last bill which showed a drop.  Overall the trend was rising.  
# Keep in mind that linear regression is not always applicable.  
# Play around with the numbers in the x and y array list and see what you get.
