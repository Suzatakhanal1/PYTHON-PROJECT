#password strength checker
# https://www.youtube.com/watch?v=pbKZ-dmUBis&list=PLdOKnrf8EcP384Ilxra4UlK9BDJGwawg9&index=30 --> link for refernce
# Objective:
# The objective of this project is to build a Password Strength  checker that evaluates the strength of user-provided passwords based on common security criteria.
# The program helps users create secure passwords by  providing feedback on password quality and suggesting improvements.

# topics covered:
# Functions, conditional statements, loops, input and output handling, string manipulation. 
# Import library (Regular Expressions(re), logic validation, etc).


import re
#re is used to search the pattern in the code especially foior special characters

# conditions:
#min 8 chars, digit, uppercase, lowercase and special characters
 
def check_password_strength(password):
    if len(password) < 8:
        return "Weak Password: It must be at least 8 characters long"
        
    elif not any (char.isdigit() for char in password):
        return "Weak Password: It must contain at least one numeric value"
    
    elif not any (char.isupper() for char in password):
        return "Weak Password: It must contain at least one capital letter"
    
    elif not any (char.islower() for char in password):
        return "Weak Password: It must contain at least one lowercase letter"
    
    elif not re.search(r'[!@#$%^&*()-+>.,<?{}]', password):
        return "Medium Password: It must contain at least one special character"

    
    return "Strong password: Your password is secured!"

# print(check_password_strength('Sujatq!3525'))

def password_checker():
    print("Welcome to the password strength checker")
    while True:
        password = input("Enter your password(or type 'exit' to quit):")

        if password.lower()== "exit":
            print("Thank you for using the Password Strength checker! Goodbye!")
            break

        result = check_password_strength(password)
        print(result) 

#run the password checker function first
if __name__ == "__main__":
    password_checker()