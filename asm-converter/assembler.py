data = open('main.hasm', 'r')
data = data.readlines()

binary_file = ""

line = ""

registers_name = ['AX', 'AL', 'AH', 'BH', 'CH', 'CM', 'EAX', 'DM']
registers_out = ['0011', '0010', '0001', '', '', '', '0100','']
registers_in = ['0101', '0100', '0001', '0011', '0010', '0110', '','1000']


def decToBin(x):
    b = bin(x)[2:]
    s = ""
    for i in range(8-len(b)):
        s += '0'
    s += b
    return s

for i in range(len(data)):
    # prepare data
    line = data[i]
    if line[-1:] == '\n':
        line = line[:-1]

    # instruction switch
    args = []
    s = ""
    #mov
    if line[0] == 'm' and line[1] == 'o' and line[2] == 'v' and line[3] == ' ':
        for j in range(4, len(line)):
            if line[j] != ' ' and line[j] != ',':
                    s += line[j]
            if line[j] == ',':
                args.append(s)
                s = ""

        args.append(s)

        literal = False

        #translate
        try: 
            binary_file += registers_out[registers_name.index(args[0])]
        except:
            binary_file +=  "0000"
            literal = True

        binary_file += registers_in[registers_name.index(args[1])]
        
        if literal:
            binary_file = binary_file +  " " + decToBin(int(args[0]))
        else:
            binary_file += " 00000000"

        binary_file += '\n'

    # minus mode
    elif len(line) == 5 and line[0] == 'm' and line[1] == 'i' and line[2] == 'n' and line[3] == 'u' and line[4] == 's':
        binary_file = binary_file + "10000000 00000000"
        binary_file += '\n'

    # plus mode
    elif len(line) == 3 and line[0] == 'a' and line[1] == 'd' and line[2] == 'd':
        binary_file = binary_file + "00000111 00000000"
        binary_file += '\n'


file = open('main.txt', 'w')
file.write(binary_file)
file.close()
        

        
        

