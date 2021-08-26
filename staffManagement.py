def getAllStaffRecord():
    try:
        inputFile = open("inputCopy.txt", 'r') # Input file is opened in reading mode
        linesList = inputFile.readlines() # List of the files' lines are stored in linesList

        for i in range(len(linesList)): # For loop where contents will be printed to the console
            if i == 0:
                print(linesList[i]) # Header is seperately printed because it doesn't need any editing
            else:
                print(linesList[i].rstrip()) # Removing any trailing characters from element

        inputFile.close()
        enterToContinue() #Proceed back to main menu
    except IOError:
        print("Error: file not found\n")
        enterToContinue()

################################################################################################################
