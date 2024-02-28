import re
from sys import exit

# Get regex we will use from user
raw_user_regex = input('Enter your regex here: ')

# Check if regex we inputted is empty
if not raw_user_regex:
  print('You did not input anything')
  exit()

# This checks if the regex can work as a legitimate regex
try:
  re.compile(raw_user_regex, re.I)
except:
  print('The regex you inputted did not compile')
  exit()

# Create our regex
infoRegex = re.compile(raw_user_regex)

# Begin reading Shoreline PPP file
file  = open('shorelineppp.txt', 'r')
# We take all of the text in the document and put it in the variable lines
lines = file.readlines()
# This counts which 'line' we are on
count = 1

# Read variable lines 'line by line'
for line in lines:
  mo = infoRegex.search(line)
  # If we have found a match on this line, then run this code
  try:
    print('Line ' + str(count) + '\t- Match found: ', mo.group())
  # If we have not found a match on this line, then run this code
  except:
    print('Line ' + str(count) + '\t- No Match')
  count += 1
