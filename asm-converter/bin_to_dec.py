from ast import arg


data = open('main.txt', 'r')
data = data.readlines()

data_out = ""

for i in range(len(data)):
    line = data[i][:-1]

    s = ""
    args = []
    for j in range(len(line)):
        if line[j] != ' ':
            s += line[j]
        if line[j] == ' ':
            args.append(s)
            s = ""
    args.append(s)

    data_out = data_out + hex(int(args[0], 2))[2:]
    data_out = data_out + " " + hex(int(args[1], 2))[2:]
    data_out += '\n'

data = open('mainHex.txt', 'w')
data.write(data_out)
data.close()
