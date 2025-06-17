#Erik Rivera
#12/10/24
#last name password generator

 # Prompts user to input a domain name
domainName = input("Please enter a domain name - facebook, google, or amazon: ")

# Turns the password into a list
domainNameList = list(domainName)

# Alphabetizes the domain name list
domainSorted = ''.join(sorted(domainNameList))

# Defines vowels
vowels = "aeiou"
# Defines password as empty string
password = ""
# For loop to go through the letters in the domain name
for char in domainSorted:
    if char in vowels:
        # Capitalizes all the vowels
        password += char.upper()
    else:
        password += char

# Adds a number to the end that is the length of the string
password += str(len(domainName))

# outputs the final password            
print(domainName + " is => " + password)