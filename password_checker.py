import math
def main():

    print("--------------PASSWORD ANALYSER--------------")

    common_passwords = ["123456", "password", "qwerty", "abc123", "111111"]

    password = input("Enter your password: ")

    if password.strip()=="":
        print("Invalid password")
        return
    
    checks = analyze_password(password)

    if password in common_passwords:
        print("\nVery Weak .Common password is detected")
        return
    entropy: float = calculate_entropy(password, checks)
    score = calculate_score(password, checks)
    
    

    print("\nPassword Strength (Score-Based):")
    if score<=2:
        print("Weak password")
    elif score<4:
         print("Medium password")
    else:
        print("Strong password")


    print("\nCalculation on Entropy:")
    if entropy <28:
        print("Very Weak")
    elif entropy<36:
        print("Weak")
    elif entropy<60:
        print("Moderate")
    elif entropy<128:
        print("Strong")
    else:
        print("Very Strong")

    print("\nSuggestion based on your password:")
    suggest(password, checks)


def analyze_password(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_spcl = any(not c.isalnum() for c in password)
    return has_upper, has_lower, has_digit, has_spcl

def calculate_score(password, checks):
    has_upper, has_lower, has_digit, has_spcl = checks

    score = 0
    if has_upper:
        score+=1
    if has_lower:
        score+=1
    if has_digit:
        score+=1
    if len(password)>=8:
        score+=1
    if has_spcl:
        score+=1
    return score

def calculate_entropy(password, checks):
    has_upper, has_lower, has_digit, has_spcl = checks
    charset_size=0

    if has_spcl:
        charset_size+=32
    if has_digit:
        charset_size+=10
    if has_lower:
        charset_size+=26
    if has_upper:
        charset_size+=26
    if charset_size==0:
        charset_size=1
    
    entropy = len(password) * math.log2(charset_size)
    return entropy

def suggest(password, checks):
    has_upper, has_lower, has_digit, has_spcl = checks
    if not(has_upper):
        print("Add Uppercase letter")
    if not(has_lower):
        print("Add Lowercase letter")
    if not(has_digit):
        print("Add Digit")
    if not(has_spcl):
        print("Add Special character")
    if len(password)<=8:
        print("Use 8 characters")
    elif(has_upper and has_lower and has_digit and has_spcl and len(password) >= 8):
        print("No suggestion needed")



if __name__ == "__main__":
    main()

