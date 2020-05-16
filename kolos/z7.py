import csv

with open('plik.csv', 'r') as file: #plik z danymi
    i = 0
    lis1 = []
    lis2 = []
    lis3 = []
    reader = csv.reader(file)
    for row in reader:
        for x in row:
            if i%3 == 0:
                lis1.append(x)
                i = i + 1
            elif i%3 == 1:
                lis2.append(x)
                i = i + 1
            else:
                lis3.append(x)
                i = i + 1
    lis4 = []
    pkt = [0] * 4
    for x in range (0, len(lis2)):
        if not(lis2[x] in lis4):
            lis4.append(lis2[x])

    for x in range (0, len(lis3)):
        id = lis4.index(lis2[x])
        pkt[id] = pkt[id] + int(lis3[id])
    
    for x in range(0, len(pkt)):
        print(lis4[x] + " " + str(pkt[x]))

            
file.close()
