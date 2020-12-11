#inputs_file = open('data/test_inputs.txt', "r")
inputs_file = open('data/inputs.txt', "r")

adapters = [int(line.strip()) for line in inputs_file.readlines()]

inputs_file.close()

adapters.append(0) # to represent the input joltage

adapters.sort()

zeros = [0 for item in adapters]

for index in range(len(adapters)):
    if index == 0:
        zeros[index] = 1
    elif index == 1:
        zeros[index] = 1
    elif index == 2:
        if (adapters[index] - adapters[0]) <= 3:
            zeros[index] = zeros[0] + zeros[1]
    else:
        dif_1 = (adapters[index] - adapters[index -1]) <= 3
        dif_2 = (adapters[index] - adapters[index -2]) <= 3
        dif_3 = (adapters[index] - adapters[index -3]) <= 3

        zeros[index] = dif_1 * zeros[index - 1] + dif_2 * zeros[index -2] +  dif_3 * zeros[index - 3]

print(zeros[-1])