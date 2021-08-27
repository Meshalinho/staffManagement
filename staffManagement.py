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
