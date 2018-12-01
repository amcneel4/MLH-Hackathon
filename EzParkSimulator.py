import time, threading
import random
import glob
from os import listdir

# private helper function to read in available spaces in the parking lot
def readInput():
    filesInSimInput = sorted(listdir("EzPark_sim_input/"))
    filename = "EzPark_sim_input/" + filesInSimInput[len(filesInSimInput)-1]
    print("Reading availability file", filename)
    f = open(filename)
    totalSpaces = f.readline().strip()
    avSpaces = f.readline().split()

    for i in range(len(avSpaces)):
        avSpaces[i] = int(avSpaces[i])

    f.close()
    return totalSpaces, avSpaces

def outputSim():
    totalSpaces, avSpaces = readInput()
    fileCount = len(listdir("EzPark_calc_input/")) + 1
    filename = "EzPark_calc_input/sim_" + str(fileCount) + ".txt"
    print("Writing to simulation file", filename)

    f = open(filename, "w")
    i = 1

    # simulate cars coming into and parking
    min = 3
    if len(avSpaces) < 3:
        min = len(avSpaces)
    idxs = getNRandomSpaces(len(avSpaces), min)
    #print("\tRandom indices in av spaces:", idxs)
    for idx in idxs:
        line = "Car " + str(i) + " parked at " + str(avSpaces[idx]) + "\n"
        i += 1
        f.write(line)

    # simulate cars leaving parking lot
    parkingLot = set(range(1,int(totalSpaces)+1))
    avSpaces = set(avSpaces)
    bookedSpaces = parkingLot.difference(avSpaces)
    min = 3
    if len(bookedSpaces) < 3:
        min = len(bookedSpaces)
    idxs = getNRandomSpaces(len(bookedSpaces), min)
    #print("\tRandom indices in booked spaces:", idxs)
    for idx in idxs:
        line = "Car", i, " left space ", bookedSpaces[idx], "\n"
        i += 1
        f.write(line)

    #done with simulation
    f.close()


# private helper function to get n unique and random integers in the range (1 to number)
# used to randomly pick used and empty spaces in the parking lot for traffic simulation
def getNRandomSpaces(number, n):
    nums = set()
    if n == number:
        return set(range(0,number))
    while True:
        nums.add(random.randint(0,number-1))
        if len(nums) == n:
            return nums
