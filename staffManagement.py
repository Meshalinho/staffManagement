################################################################################################################
def updateStaff():
    try:
        inputFile = open("inputCopy.txt", 'r')
        linesList = inputFile.readlines()
        IDList = [] # List of IDs for future reference
        inputID = input("Please enter staffID: ")

        contentCopy = [] # A list of lists which each element's format will be  [ID, NAME, HOURS, DAY] is created


        infoList = list(linesList)
        infoList.pop(0) # Header is removed

        for i in infoList:
            contentCopy.append(i.split())

        for i in contentCopy:
            IDList.append(i[0]) # IDs are added to IDList

        if inputID in IDList:
            signIn = int(input("Please enter Sign-in Time: "))
            signOut = int(input("Please enter Sign-out Time: "))

            if ((signIn and signOut) > 100 and (signIn and signOut) < 2400) and (signOut > signIn):
                hours = int((signOut - signIn) / 100)
                index = IDList.index(inputID) # Matching the inputID with the IDs index in IDList to determine the staff's position in the contentCopy list
                updatedInfo = contentCopy[index] # List of the staff's info [ID, NAME, HOURS, DAY] is created

                newHours = str(int(updatedInfo[3]) + hours) # Hours are added to previous hours
                newDays = str(int(updatedInfo[4]) + 1) # Days is incremented by one

                updatedInfo[3] = newHours # New hours and days are updated
                updatedInfo[4] = newDays


                contentCopy[int(index)] = updatedInfo # Original info is changed with brand new information
            else:
                raise ValueError
        else:
            raise TypeError


        inputFile.close()
        inputFile = open("inputCopy.txt", 'w')
        inputFile.write("Staff ID 	Staff Name       Hour 	    Days\n") # Header written in the file

        for i in contentCopy: # Info of the staff including the updated one are written once again in the file
            inputFile.write("%0s %19s %10s %10s\n" % (i[0], (i[1] + ' '+ i[2]), i[3] , i[4]))

        inputFile.close()
        print("Staff’s information has been updated . . .")
        enterToContinue()


    except ValueError:
        print("Error: Invalid time\n")
        enterToContinue()
    except TypeError:
        print("Error: Invalid Staff ID\n")
        enterToContinue()
    except IOError:
        print("Error: file not found\n")
        enterToContinue()





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
