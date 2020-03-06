#Example of searching for cost related values.

# Import the re module regex library
import re

#Message to decode
message = 'I spent over $90 this week on gas, ugh!'

x = re.search(r'\$[0-9]*', message)
if (x):
  print(x.group())
else:
  print("No match")
