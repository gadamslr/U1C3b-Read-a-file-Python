file1 = open("transcript1.txt","r")
file2 = open("transcript2.txt","r")

transcript1 = []
transcript2 = []

for line in file1:
    transcript1.append(line.strip())

for line in file2:
    transcript2.append(line.strip())

file1.close()
file2.close()

transcript1_length = len(transcript1)

for x in range(transcript1_length):
    print(transcript1[x])
    print(transcript2[x])
