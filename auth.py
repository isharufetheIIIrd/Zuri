#registaration system
import random
import datetime


Database = {}                                   #user details are stored            

#system initialization function
def init():
    isSelectedOptionValid = False
    print("welcome to Bank iii")
    while isSelectedOptionValid == False:
        haveaccount = (input('do you have an account with us: 1(yes), 2(no) \n'))
        if (haveaccount == "1"):
            isSelectedOptionValid = True
            login()
        elif(haveaccount == "2"):
            isSelectedOptionValid = True
            register()
                                                        
#system login function
def login():
    print("Input Login Details")
    isloginsuccessful = False                                               #loop initialization incase wrong details are entered.

    while isloginsuccessful == False:                                              #while loop to initiats
        UserAccountNumber = int(input("Enter your Account number:\n"))
        password = input("Password:\n")

        for AccountNumber,userDetails in Database.items():
            if(AccountNumber == UserAccountNumber):                                 #verify account number entered with account number saved in database
                isloginsuccessful = True                                             #break condition
                if(userDetails[3] == password):
                    isloginsuccessful = True
                else:
                    forgotPassword = int(input('Forgot Password: 1(yes), 2(no)\n'))
                    if(forgotPassword == 1):
                        mail= input('input email\n')                                                      #help user retrieve password incase forgoten
                        if(userDetails[2] == mail):
                            print("your password is '%s' " %userDetails[3])
                            isloginsuccessful = False
                    elif(forgotPassword == 2):
                        pass

            else:
                 print("Invalid account number")
    BankOperations(userDetails)                                                 #pass in user details to bankoperation function

#system register function
def register():
    email = input("what's your email?\n")
    Firstname = input("what's your first name:\n")
    Lastname = input("what's your last name?\n")
    Password = input("Please create your password\n")                           #takes user input

    AccountNumber = generatingaccountno()                                          #saves/copies function into a variable

    Database[AccountNumber] = [ Firstname, Lastname, email, Password ]
    userDetails = Database                                                          #copies database dictionary to a variable
    print("Dear new customer your account has been created")
    print("your account number: %d " %AccountNumber)                                #prints randomly generated account number
    print("Please keep it safe")
    login()
    

#account number generation function
def generatingaccountno():                                  
    return random.randrange(1111111111,9999999999)                  #uses random function to generate random numbers in range 1 to 9

#bank operation function
def BankOperations(userDetails):
    print('welcome %s %s' % ( userDetails[0], userDetails[1]) )
    now = datetime.datetime.now()
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    print('what would you like to do?')
    print("1, Withdrawal")
    print("2, Cash Deposit")
    print("3, Complaint")

    selectedoption = int(input('please select an option:'))

    if( selectedoption == 1 ):
        withdrawal()
    elif( selectedoption == 2 ):
         deposit()
    elif( selectedoption == 3):
        complaint()
    else:
            print('Invalid option selected, Try again')
            BankOperations(userDetails)

#withrawal function
def withdrawal():
    debit = int(input( 'How much do you want to Withdraw? N'))      #Takes input
    if(debit > 0):                                             #checks that input is valid
                print("Take your cash")
    else:
                print("Invalid amount selected")                 #feedback if invalid amount is inputed

#deposit function
def deposit():
     Credit = int(input( 'How much do you want to Deposit? N'))         #Takes input
     if(Credit > 0):
                 print("Current Balance: %d" %Credit)           #checks that input is valid
     else:
                print("invalid deposit amount")                         #feedback if invalid amount is inputed
                
#complaint function    
def complaint():
    Complaint = input("what issue would you like to report?")              #Takes input
    print("Thank you for contacting us")
init()


