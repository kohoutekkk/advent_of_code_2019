inputs_file = open('data/test_inputs.txt', "r")
inputs_file = open('data/inputs.txt', "r")

adapters = [int(line.strip()) for line in inputs_file.readlines()]

inputs_file.close()

adapters.append(0) # to represent the input joltage

adapters.sort()

dif_1 = 0
dif_2 = 0
dif_3 = 1 # because of the last connection to our device

for index in range((len(adapters) - 1)):
    if (adapters[index + 1] - adapters[index]) == 1:
        dif_1 += 1
    elif (adapters[index + 1] - adapters[index]) == 2:
        dif_2 += 1
    elif (adapters[index + 1] - adapters[index]) == 3:
        dif_3 += 1
    else:
        print("does not work")
        break

print(dif_1 * dif_3)


