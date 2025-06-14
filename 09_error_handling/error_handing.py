# Number of ways files can be declared in python

# Solution 1:
file = open('youtube.txt', 'w')

try:
    file.write("Chai aur Code")
finally:
    file.close()
    
# Solution 2:
with open('youtube.txt', 'w') as file:
    file.write("chai aur code")