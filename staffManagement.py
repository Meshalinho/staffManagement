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
