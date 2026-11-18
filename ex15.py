import re

# Function to validate email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        print("Valid Email Address")
    else:
        print("Invalid Email Address")


# Function to validate phone number
def validate_phone(phone):
    pattern = r'^[6-9][0-9]{9}$'

    if re.match(pattern, phone):
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number")


# Function to extract transaction ID
def extract_transaction(log):
    pattern = r'TXN[0-9]+'
    result = re.findall(pattern, log)

    print("Transaction IDs:", result)


# Main program
email = input("Enter Email Address: ")
phone = input("Enter Phone Number: ")

log = input("Enter Transaction Log: ")

print("\n--- Validation Results ---")

validate_email(email)
validate_phone(phone)
extract_transaction(log)