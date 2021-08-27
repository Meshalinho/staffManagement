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
