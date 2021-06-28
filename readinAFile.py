file = open("quick.txt", "r")

#quicktest = file.read()

#print(quicktest)

#print(file.readline())
#print(file.readline())

for line in file:
    print(line.strip())
