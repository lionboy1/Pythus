# numpy currently doesn't support the mode function, so the scipy module is used here.
#Duplicate values are added to the array to see which value appears the most
#The printed array lists the value which is the mode, and how many duplicates are in the array.

from scipy import stats as st
import math as mt

daily_gas = [15,13,13.5,14.7,11.4, 15, 13, 13, 13]

mode = st.mode(daily_gas)
print(mode)
