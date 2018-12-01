
spaces = None
restricted_spaces = []
handicapped_spaces = []
taken_spaces = []

def readInput(filename):
    f = open(filename)

    # points to the current list we are adding to; works more ike a temp pointer
    # initializing with the sirt list in file
    curList = restricted_spaces
    # check if this is the initial run or not

    if "input.txt" in filename:
        while True:
            line = f.readline().strip()

            # blank line read
            if len(line) == 0:
                break
            if line[0].isdigit():
                curList.append(int(line.strip()))
            else: # new list line; contains text for parking psaces count or a new list
                if line.lower() == "total spaces":
                    line = f.readline().strip()
                    spaces = int(line.strip())
                elif line.lower() == "handicapped spaces":
                    curList = handicapped_spaces
                elif line.lower() == "taken spaces":
                    curList = taken_spaces

        print("Spaces Available:", spaces)
        print("VIP spaces:", restricted_spaces)
        print("Handicapped/Reserved spaces:", handicapped_spaces)
        print("Taken spaces:", taken_spaces)

    # parse output from the simulator program to update available spaces in the lot
    #else: #read in EzPark_calc_input/input.txt
     #   f = open('EzPark_calc_input/input.txt')

      #  while True:
       #     line = f.readline().strip()

    f.close()



if __name__ == "__main__":
    readInput("EzPark_calc_input/input.txt")
