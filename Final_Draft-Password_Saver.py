# CMIT-135-45C_Gann_Week_7_Programming_Assignment-Final_Draft-Password_Saver
# This is a simple password manager program.

import csv
import sys

# The password list - We start with it populated for testing purposes
passwords = [["yahoo","XqffoZeo"],["google","CoIushujSetu"]]

# The password file name to store the passwords to
passwordFileName = "samplePasswordFile"

# The encryption key for the caesar cypher
Encryptionkey=16

# Caesar Cypher Encryption
def passwordEncrypt (unencryptedPassword, Encryptionkey):

    # We will start with an empty string as our encryptedMessage
    encryptedPassword = ''

    # For each symbol in the unencryptedMessage we will add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedPassword:
        if symbol.isalpha():
            num = ord(symbol)
            num += Encryptionkey

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            encryptedPassword += chr(num)
        else:
            encryptedPassword += symbol

    return encryptedPassword


def loadPasswordFile(fileName):

    with open(fileName, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList


def savePasswordFile(passwordList, fileName):

    with open(fileName, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)


# Create a greeting to print only at the start of the program, so outside of the While True main menu loop.
print()
print("Welcome to Password Saver!")
print()

while True:  # Main menu of options.
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Print the encrypted password list (for testing)")
    print(" 6. Delete an entry")  # Added an option to delete a saved website/password entry.
    print(" 7. Change a password")  # Added an option to change the saved password for a website entry.
    print(" 8. Quit program")
    print("Please enter a number (1-8)")
    choice = input()


    if(choice == '1'): # Load the password list from a file.
        passwords = loadPasswordFile(passwordFileName)
        print("Password file opened.")


    if(choice == '2'): # Lookup a password.
        print("Which website do you want to lookup the password for?")
        for keyvalue in passwords:  # Prints a list of the first item in each sublist.
            print(keyvalue[0])
        passwordToLookup = input()  # Gathers user input to use in the loop below.

        # This loop iterates through a range the length of the passwords list comparing user input to the first
        # items in the sublists.  If the user input is found, the de-encrypting function is run on the password
        # and the result printed.
        for i in range(len(passwords)):
            if passwordToLookup == passwords[i][0]:
                encryptedPassword = passwords[i][1]
                unencryptedPassword = passwordEncrypt(encryptedPassword, (Encryptionkey*-1))  # By multiplying the
                # Encryptionkey by -1, the passwordEncrypt function has the opposite effect on the encrypted password.
                print("The passsword for " + str(passwords[i][0]) + " is: " + (unencryptedPassword))


    if(choice == '3'):  #  Add a password.
        print("What website is this password for?")
        website = input()  # Gather user input, then the loop below iterates through the list of the first item in
                            # each sublist to check if an entry already exists for that website.  This prevents
                            # having more than one entry per website.
        for i in range(len(passwords)):
            if website == passwords[i][0]:
                print("A password entry for that site already exists.")
                print("Please enter '2' to see a list of websites saved before returning to the main menu.")
                print("Or, press <Enter> to return directly to the main menu.")
                choice = input()
                if(choice == ''):  # Breaks out of the loop and returns to main menu if user presses the Enter key.
                    break
                elif(choice == '2'):  # Iterates through the list to print the first item in each sublist.
                    print("List of saved website passwords:")
                    for keyvalue in passwords:
                        print(keyvalue[0])
                break  # Breaks out of this loop and returns to main menu.
        else:  # If no duplicate is found, this portion of the loop runs.
            print("What is the password?")
            unencryptedPassword = input()  # Gathers user input and stores it as a variable.
            encryptedPassword = passwordEncrypt(unencryptedPassword, Encryptionkey)  # Uses the encryptPassword function
                                                                                     # to encrypt the user's input.
            Add_A_Password = []  # Creates a new list to store the new website/encrypted password combination.
            Add_A_Password.append(website)  # Adds website to the new list.
            Add_A_Password.append(encryptedPassword)  # Adds now encrypted password to the new list as the second item.
            passwords.extend([Add_A_Password])  #  Places the new list as a sublist at end of the master password list.
            print("Password added.")


    if(choice == '4'):  # Save the passwords to a file.
        savePasswordFile(passwords,passwordFileName)
        print("Password file saved.")


    if(choice == '5'):  # Print out the password list.
        print("Website, Encrypted password")
        for keyvalue in passwords:
            print(', '.join(keyvalue))


    if(choice == '6'):  # Delete a website and password.
        print("Which website and password do you want to delete?")
        for keyvalue in passwords:  # Iterates through the password list and prints the first item in each sublist.
            print(keyvalue[0])
        passwordToLookup = input()

        for i in range(len(passwords)):  # Iterates through the length of the password list to match user input.
            if passwordToLookup == passwords[i][0]:  # If a match is found, the entry is deleted.
                del passwords[i]
                print("Deleted entry for " + str(passwordToLookup))
                break  # Breaks out of loop and returns to the main menu.


    if(choice == '7'): # Change a password.
        print("Which website do you want to change the password for?")
        for keyvalue in passwords:  # Iterates through the password list and prints the first item in each sublist.
            print(keyvalue[0])
        passwordToLookup = input()

        for i in range(len(passwords)):  # Iterates through the length of the password list to match user input.
            if passwordToLookup == passwords[i][0]:  # If a match is found, the entry is deleted.
                del passwords[i]                    # The new website/password combination will be added below.
                print("Please enter new password for " + str(passwordToLookup))
                NewPassword = input()  # Gathers new password and then breaks out of this nested loop.
                break

        NewPassword = passwordEncrypt(NewPassword, Encryptionkey)  # Encrypts the new password.
        ModifiedPassword = []  # Creates a new list to store the new website/encrypted password combination.
        ModifiedPassword.append(passwordToLookup)  # Adds website entered at beginning of this loop to the new list.
        ModifiedPassword.append(NewPassword)  # Adds the new encrypted password to the new list as second item.
        passwords.extend([ModifiedPassword])  #  Places the new list as a sublist at end of the master password list.
        print("Password changed.")


    if(choice == '8'):  # Quit program
        print("Goodbye.")
        print("And thank you for using Password Saver!")
        sys.exit()

    print()
    print()
