################################################################################################################
def staffID():

    """
    This function gives the user the ablilty to view explicitly ONE staff Member
        by providing the staffID

    1) The file is read and its contents are stored in a list form
    2) User enters ID and then we check if the ID exists or not
    3) If the ID is not found we proceed to raise a ValueError, otherwise we move
        on to print the information of ONLY the desired staff member which ID we previously
        entered
    4) We then close the file

    """
    inputFile = open("inputCopy.txt", 'r')
    linesList = inputFile.readlines() # List of the files' lines are stored in linesList
    contentCopy = []
    IDList = [] # List to store IDs for future reference
    linesList.pop(0) # Contents of the header are removed from linesList
    inputID = str(input("Enter accountID: "))
    print() #Prints empty line to keep space from the prompt and the header
    sentinel = True  # To keep track if the inputID is in the IDList or not

    while sentinel == True:
        try:
            for i in linesList:
                contentCopy.append(i.split()) # A list of lists which each element's format is [ID, NAME, HOURS, DAY] is created

            for i in contentCopy:
                IDList.append(i[0]) # The first element of contentCopy which is the ID is appended to IDList

            if inputID in IDList: # If ID is found, print header and staff info and break out of while loop by appointing sentinel as false
                index = IDList.index(inputID)
                print("%10s %15s %10s %10s" % ("Staff ID", "Staff Name", "Hour", "Days"))
                print("%10s %13s %10s %10s" % (contentCopy[index][0], (contentCopy[index][1] + ' '+ contentCopy[index][2]), contentCopy[index][3] , contentCopy[index][4]))
                sentinel = False

            if sentinel == True:
                raise ValueError
                break

            inputFile.close()
            enterToContinue()

        except ValueError:
            print("Error: Invalid account number\n")
            enterToContinue()

        except IOError:
            print("Error: file not found\n")
            enterToContinue() # Automatically returns to main menu

################################################################################################################
