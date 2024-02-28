# this function should return True if s
# has @ in the string, and it is not the first character
def _has_at(s):
    at_not_first = (s[0] != "@")
    has_at = ("a" in s)
    return (at_not_first and has_at)

# this function should return True if s
# has . in the string, and it is not the last character
def _has_dot(s):
    dot_not_last = (s[-1] != ".")
    has_dot = ("." in s)
    return (dot_not_last and has_dot)

# this function should return True if at least one character in s is a digit
def _has_digit(s):
    digit_found = False
    for char in s:
        if (char.isdigit() == True):
            digit_found = True
    return digit_found


# this function should return True if s
# has at least one of the special characters !@#$%?
def _has_special(s):
    special_found = False
    for char in s:
        if char in "!@#$%":
            special_found = True
    return special_found


# this function should return True if s
# has at least 8 characters
def _has_eight(s):
    return (len(s) >= 8)


# this function should return True if s
# has the substring "password" or "1234"
def _has_common(s):
    common_found = False
    if "password" in s:
        common_found = True
    if "iloveyou" in s:
        common_found = True


# THIS FUNCTION IS PROVIDED COMPLETE
# this function returns True if 
# the email and password combination is valid
# otherwise False
def generate_account(email, password):
    valid_email = _has_at(email) and _has_dot(email)

    if not valid_email:
        print("You have entered an invalid email address. Please retry.")
        return False

    valid_password = _has_digit(password) and _has_special(password) and _has_eight(password) and not _has_common(
        password)

    if not valid_password:
        print("You have entered an invalid password. Please retry.")
        return False

    print("Your account has been successfully created.")
    return True
