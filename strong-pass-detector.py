import re
# A strong password is defined as one that is at least eight characters 
# long, contains both uppercase and lowercase characters, and has at least one digit.

def strong_pass_detector(password):
    s_count = 0
    
    p_len = len(password)

    if p_len > 7:
        print("Your password is at least 8 characters long")
        s_count += 1

    lower_case_regex = re.compile(r'[a-z]')
    if lower_case_regex.search(password):
        print("Your password has at least one lowercase letter")
        s_count += 1

    upper_case_regex = re.compile(r'[A-Z]')
    if upper_case_regex.search(password):
        print("Your password has at least one uppercase letter")
        s_count += 1
    
    number_regex = re.compile(r'[0-9]')
    if number_regex.search(password):
        print("Your password has at least one number letter")
        s_count += 1

    special_chars_regex = re.compile(r'[!\@#\$\%\^\&\*\(\)\_\-]')
    if special_chars_regex.search(password):
        print("Your password has at least one special char")
        s_count += 1

    if s_count == 0:
        return "Uber weak password"
    elif s_count == 1:
        return "Weak password"
    elif s_count == 2:
        return "Medium strenght password"
    elif s_count == 3:
        return "Stronk password"
    elif s_count == 4:
        return "Super stronks password"
    elif s_count == 5:
        return "Stupidly good password"

if __name__ == "__main__":
    print(strong_pass_detector("bitch*"))
    

