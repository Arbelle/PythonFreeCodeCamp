import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password
    

if __name__== '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)











#import re
#import secrets
#import string


#def generate_password(length, nums, special_chars, uppercase, lowercase):
    # Define the possible characters for the password
    #letters = string.ascii_letters
    #digits = string.digits
    #symbols = string.punctuation

    # Combine all characters
    #all_characters = letters + digits + symbols

    #while True:
        #password = ''
        # Generate password
        #for _ in range(length):
            #password += secrets.choice(all_characters)
        
         #constraints = [
            #(nums, r'\d'),
            #(lowercase, r'[a-z]'),
            #(uppercase, r'[A-Z]'),            
            #(special_chars, fr'[{symbols}]')            
        #]

        # Check constraints
        #count = 0
        #for constraint, pattern in constraints:
            #if constraint <= len(re.findall(pattern, password)):
                #count += 1
            
        #if count == 4:
            #break
            
        #if

    #return password
    
# new_password = generate_password(8)
# print(new_password)

#pattern = r'\W'
#quote = '_'
#print(re.findall(pattern, quote))

#Having all([expression for i in iterable]), means that a new list is created by evaluating expression for each i in iterable. After the all() function iterates over the newly created list, the list is deleted automatically, since it is no longer needed.Memory can be saved by using a generator expression. Generator expressions follow the syntax of list comprehensions but they use parentheses instead of square brackets.Change your list comprehension into a generator expression by removing the square brackets.