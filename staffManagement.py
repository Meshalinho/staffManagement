################################################################################################################

"""
This feature gives the user the ability to remove a desired staff member by
providing their ID:
    1) We first read the file and store its contents in a list
    2) Ask the user to provide the ID they desire to delete fromt the file
    3) Check if the entered ID truly exists in the file, if not raise a ValueError,
        otherwise remove all information that belongs to the user
    4) When the information is removed from the list, rewrite the file with the new
        updated information
    5) Close the file 
"""
def deleteStaff():
    try:
        inputFile = open("inputCopy.txt", 'r')
        IDList = []
        contentCopy = []
        staffInfo = []
        linesList = inputFile.readlines()
        listCopy = list(linesList)
        inputID = input("Enter ID to Delete: ")
        listCopy.pop(0)

        for i in listCopy:

            staffInfo = list(i.split())
            contentCopy.append(staffInfo)

        for i in contentCopy:
            IDList.append(i[0])

        if inputID not in IDList: # If the ID doesn't exist in IDList, raise an error, as non-existent IDs don't have information
            raise ValueError

        else:
            index = IDList.index(inputID) # ID is matched with the index to determine the staff member's position
            contentCopy.pop(index) # Staff member's information is deleted from the original information
            inputFile.close()

            inputFile = open("inputCopy.txt", 'w')
            inputFile.write("Staff ID 	Staff Name       Hour 	    Days\n")

            for i in contentCopy: # List containing the updated info is written into the file line by line using the for loop
                inputFile.write("%0s %19s %10s %10s\n" % (i[0], (i[1] + ' '+ i[2]), i[3] , i[4]))

            inputFile.close()
            enterToContinue()

    except ValueError:
        print("Error: ID entered does not exist\n")
        enterToContinue()
    except IOError:
        print("Error: file not found\n")
        enterToContinue()



################################################################################################################
