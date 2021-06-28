transcript1 = open("transcript1.txt", "r")
transcript2 = open("transcript2.txt", "r")

readtrns1 = []
readtrns2 = []

for line in transcript1:
    readtrns1.append(line.strip())

for line in transcript2:
    readtrns2.append(line.strip())

transcript1.close()
transcript2.close()

lengthtrans01 = len(readtrns1)
lengthtrans02 = len(readtrns2)

for i in range(len(readtrns1)):
    print(f"Trans1: {readtrns1[i]}")
    print(f"Trans2: {readtrns2[i]}")