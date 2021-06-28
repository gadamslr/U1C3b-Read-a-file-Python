file = open("numbers.txt", "r") # openning a file

totaliser = 0 # Setting a totaliser variable to 0

for number in file: # iterating through the file
    
    totaliser =  totaliser + int(number.strip()) # reading number line and changing it to an int

print(f"The toal of the numbers.txt file is {totaliser}")