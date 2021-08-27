<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
################################################################################################################

def enterToContinue():
    """
    Function used to shorten the process of returning to the main menu when finished working with a certain function or when entering incorrect output
    """
    input("Press Enter to continue...\n")
    main()

################################################################################################################


def main():

    """
    The main method is used as the starrting point of this program where the user is presented with the different functions and can choose between them from.

    Each choice directs the user to the desired feature, if the users fails to
    correctly select a certain function they are asked whether they want to continue or not, if not they exit, otherwise the user gets another shot at entering the
    correct input.


    """
    print("1.Display all Staff Records\n" +
          "2.Display the Record of a particular Staff Member\n" +
          "3.Display all Staff Salary\n" +
          "4.Update Staff\n" +
          "5.Add New Staff\n" +
          "6.Delete Staff\n" + '\n' +
          "7.Exit" + '\n') # Options are shown to users

    userChoice = int(input("Please select your choice: ")) # User picks their choice

    try:
        if userChoice <= 0 or userChoice >= 8: # User enters an integer number between 0 and 8, otherwise an exception is raised
            raise ValueError
        else:
            if userChoice == 1:
                getAllStaffRecord()
            elif userChoice == 2:
                staffID()
            elif userChoice == 3:
                getSalary()
            elif userChoice == 4:
                updateStaff()
            elif userChoice == 5:
                addStaff()
            elif userChoice == 6:
                deleteStaff()
            elif userChoice == 7:
                print("Thank you for using the program :)")
    except ValueError:
        print("Error: Please Enter an Integer Number Between 0 and 7\n")
        enterToContinue()






main()
||||||| 4966117
=======
################################################################################################################
def getSalary():

    """
    In this function we give the user the ability to view the salary of the staff
        members.
    """
    try:
        inputFile = open("inputCopy.txt", 'r')
        wage = float(input("Please Enter the Wage (SAR): "))
        print() #Prints empty line to keep space from the prompt and the header
        linesList = inputFile.readlines()
        linesList.pop(0)
        contentCopy = [] # A list of lists which each element's format WILL BE [ID, NAME, HOURS, DAY] is created
        finalList = [] # A list of lists which each element's format WILL BE [ID, NAME, HOURS, SALARY] is created

        if wage < 100:
            raise ValueError

        print("%15s %15s %10s %15s\n" % ("Staff ID", "Staff Name", "Hour", "Salary(SAR)")) # Print Header

        for i in linesList:
            contentCopy  = list(i.split()) # Contents of input are split and made a copy of inside contentCopy
            finalList.append(contentCopy)  # Contents of contentCopy are appended by the for loop inside finalList

        for i in finalList:
            hours = int(i[3])
            days = int(i[4])
            overtime = hours - (days * 8)
            salary = ((hours - overtime) * wage) + (overtime * wage * 0.10)
            ID = i[0]
            name = i[1] + ' ' + i[2] # First and last names are joined

            print("%15s %15s %10s %15s"  % (ID, name, hours, salary)) # Print Info of Staff's Salary

        enterToContinue()

    except ValueError:
        print("Error: Invalid withdraw amount\n")
        enterToContinue()
    except IOError:
        print("Error: file not found\n")
        enterToContinue()




################################################################################################################
>>>>>>> salary
||||||| 4966117
=======
################################################################################################################
def addStaff():

    """
    This function allows the user to add information about new staff from first and last names,
        since the staff is new to the database they get assigned a default value of zero for both hours and days

    """
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
>>>>>>> addStaff
||||||| 4966117
=======
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
>>>>>>> deleteStaff
||||||| 4966117
=======
def getAllStaffRecord():

    """
    In this function we give the user the ability to view the staff record,
    the function views the variable linesList by inserting it in a for loop and
    printing each line one by one.


    """
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
>>>>>>> staffRecord
||||||| 4966117
=======
################################################################################################################
def updateStaff():


    """


    The user can update and change a specific staff member's info by first:
    ---- Firstly, read and store the information of the file in a list----
    1) Enter the desired staffID you want changed
    2) Enter the sign-in and sign-out for the staff member
    3) Check for logic i.e: sign-out cannot be before sign-in
    4) From the entered sign-in and sign-out we can determine the hours
    5) We then access the information from the file and edit according to the index
        of the staffID
    6) View message that the information has been updated
    
    """
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
>>>>>>> updateStaff
||||||| 4966117
=======
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
>>>>>>> staffID
