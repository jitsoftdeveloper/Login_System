import re

option = input('Do you want to Login or SignUp?\n[1] Login\n[2] SignUp\n\n> Select an option: ').lower()

# SignUp Fucntion
def sign_up():

  with open('login.txt', 'a') as savefile:

    signup_user = input('\nEnter Your Username: ')

    signup_emailID = input('Enter Your Email ID: ')

    # Using regular expression to search whether user entered @ in email id or not
    if re.search('@', signup_emailID, re.IGNORECASE) == None:
      print('Please Enter valid Email ID!')
        
    else:
      signup_pass = input('Enter Your Password: ')
      signup_confirm_pass = input('Confirm Your Password: ')

      if signup_pass != signup_confirm_pass:
        print('Password Does not Match!')
      else:
        savedata = ['\n',signup_user, ',' , signup_pass, ',' , signup_emailID]
        # Writing the data to login text file
        savefile.writelines(savedata)
        print('Successfully Signed up!')

# Log In Function
def log_in():

  correct_login = False
  user = input('> Enter Username: ')
  passwrd = input('> Enter Password: ')
  studentlist = []
  with open ("login.txt", 'r+') as textfile:
        
      for row in textfile:
          row = row.strip ("\n") #removing the newlines
          studentlist.append(row.split(',')) #splitting the username & password from ','

  for everything in studentlist:       
    username = everything[0]

    if user == username:
      user_found = [everything[0], everything[1]]
      correct_login = True
      if user_found[1] == passwrd:
        print("logged in")
          
      else:
        print('wrong password')
      
  if correct_login == False:
    response = input('\n This user does not exist. Would You like to sign up? (yes or no)').lower()

    if response == 'yes':
      sign_up()
        
    else:
      print('Exiting Program!')

if option in ['1', 'login']:
  log_in()
  
else:
  sign_up()