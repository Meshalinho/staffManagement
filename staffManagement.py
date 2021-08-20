################################################################################################################
def addStaff():

    
    try:
        inputFile = open("inputCopy.txt", 'r')
        IDList = []
        contentCopy = []
        staffInfo = []
        linesList = inputFile.readlines()
        listCopy = list(linesList)
        inputID = input("Enter ID to Add: ")
        listCopy.pop(0)


        for i in listCopy:
            staffInfo = list(i.split())
            contentCopy.append(staffInfo)

        for i in contentCopy:
            IDList.append(i[0])

        if inputID in IDList: # If the inputID already exists raise an error
            raise ValueError

        else:
            newStaff = [] # List with the new staff member's info is created
            firstName = input("Enter First Name: ")
            lastName = input("Enter Last Name: ")

            newStaff.append(inputID)
            newStaff.append(firstName)
            newStaff.append(lastName)
            newStaff.append('0') # Default hours
            newStaff.append('0') # Default days
            contentCopy.append(newStaff) # New staff member's info is added to the existing information


            inputFile.close()
            inputFile = open("inputCopy.txt", 'w')
            inputFile.write("Staff ID 	Staff Name       Hour 	    Days\n")

            for i in contentCopy:
                inputFile.write("%0s %19s %10s %10s\n" % (i[0], (i[1] + ' '+ i[2]), i[3] , i[4]))

            inputFile.close()
            print("Staff Member has been succesfully added")
            enterToContinue()

    except ValueError:
        print("Error: Staff ID already exists\n")
        enterToContinue()
    except IOError:
        print("Error: file not found\n")
        enterToContinue()
################################################################################################################
