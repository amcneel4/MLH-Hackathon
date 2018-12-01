import time, threading
from EzParkSimulator import outputSim
import glob
from os import listdir

totalSpaces = 0
restricted_spaces = []
handicapped_spaces = []
#taken_spaces = set([])

def readInput():
    f = open("EzPark_calc_input/input.txt")
    line = f.readline().strip()

    while True:
        # done with input file
        if len(line) == 0:
            break
        # new list line; contains text for a new list
        if line.lower() == "total spaces":
            line = f.readline().strip()
            totalSpaces = int(line.strip())
            spaces = set(range(1, totalSpaces+1))
            line = f.readline()
        elif "restricted spaces" in line.lower():
            line = f.readline().strip()
            while len(line) > 0 and line[0].isdigit():
                restricted_spaces.append(int(line))
                line = f.readline().strip()
        elif "handicapped spaces" in line.lower():
            line = f.readline().strip()
            while len(line) > 0 and line[0].isdigit():
                handicapped_spaces.append(int(line))
                line = f.readline().strip()
        elif "taken spaces" in line.lower():
            line = f.readline().strip()
            while len(line) > 0 and line[0].isdigit():
                # taken_spaces.add(int(f.readline().strip()))
                spaces.discard(int(line.strip()))
                line = f.readline().strip()
        #line = f.readline()

    f.close()
    return spaces

def updateTakenSpaces(spaces):
    filesInCalcInput = sorted(listdir('EzPark_calc_input/'))
    fileName = "EzPark_calc_input/" + filesInCalcInput[len(filesInCalcInput)-1]
    print("Current Lot:", spaces, "\nReading in sim file:", fileName)
    f = open(fileName)
    while True:
        line = f.readline().strip()
        if "left" in line:
            tokens = line.split("left space")
            free_space = int(tokens[1].strip())
            spaces.add(free_space)
            #print("\tFreeing space", free_space, ":", spaces)
        elif "parked" in line:
            tokens = line.split("parked at")
            spaces.discard(int(tokens[1].strip()))
            #print("\tBlocking space", tokens[1],":", spaces)
        else: # done with input
            break
    return spaces

def getAvailableSpaces(totalSpaces, spaces):
    print('Updating taken spaces based on sim')
    spaces = updateTakenSpaces(spaces)
    print("Updated Lot:", spaces)
    outputAvailabilities(totalSpaces, spaces)
    print("Okay, new parking lot passed to sim")
    #time.sleep(3)
    outputSim()
    print("Got New Simulated Traffic!")
    return spaces

def outputAvailabilities(totalSpaces, spaces):
    fileCount = len(listdir("EzPark_sim_input/")) + 1
    filename = "EzPark_sim_input/availabilities_" + str(fileCount) + ".txt"
    print("Writing availabilities to", filename)
    f = open(filename, "w")
    line = str(totalSpaces) + "\n"
    for sp in spaces:
        line += str(sp) + " "
    f.write(line)
    f.close()

if __name__ == "__main__":
    spaces = readInput()
    print("Built the initial parking lot")
    print("read input")
    spaces = getAvailableSpaces(totalSpaces, spaces)
    threading.Timer(10, getAvailableSpaces, args=(totalSpaces, spaces, )).start()
