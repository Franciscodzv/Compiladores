def check(lines, terminales, noTerminales):
    lines = lines.split(" ")
    #get elements from left of ->
    for i in range(len(lines)):
        if lines[i] == "->":
            if lines[i-1] not in noTerminales:
                noTerminales.append(lines[i-1])
            break
    #get elements from right of ->
    for i in range(len(lines)):
        if lines[i] == "->":
            for j in range(i+1, len(lines)):
                if lines[j] not in terminales and lines[j] not in noTerminales and lines[j] != "'" and lines[j] != "":
                    terminales.append(lines[j])
            break

    #if element is in terminales and noTerminales, remove it from terminales
    for i in range(len(terminales)):
        if terminales[i] in noTerminales:
            terminales.pop(i)
            break
        


print("Introduzca el input: ")
inputLength = input()
terminales = []
noTerminales = []

for i in range(int(inputLength)):
    lines = input()
    check(lines, terminales, noTerminales)

#write output to file
with open('output.txt', 'w') as f:
    f.write("Terminal: ")

    for i in range(len(terminales)):
        f.write(terminales[i])
        if i != len(terminales)-1:
            f.write(", ")
    f.write("\n")
    f.write("Non terminal: ")

    for i in range(len(noTerminales)):
        f.write(noTerminales[i])
        if i != len(noTerminales)-1:
            f.write(", ")
    f.write("\n")

print("Terminal: ", terminales)
print("Non terminal: ", noTerminales)






        


    
    




    





