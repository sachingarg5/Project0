def validate_login(new_login:tuple) ->bool:
    return validate_username(new_login[0]) and validate_password(new_login[1])

def validate_info(new_info:tuple)-> bool:
    return validate_first_name(new_info[0]) and validate_last_name(new_info[1])

def validate_username(username):
    return len(username)>=5 and len(username)<=15

def validate_password(password):
    return len(password)>=5 and len(password)<=15

def validate_first_name(firstname):
    return len(firstname)>=3 and len(firstname)<=15

def validate_last_name(lastname):
    return len(lastname)>=3 and len(lastname)<=15