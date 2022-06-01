import re

def validate_login(new_login:tuple) ->bool:
    return validate_username(new_login[0]) and validate_password(new_login[1])

def validate_user_info(new_info:tuple)-> bool:
    return validate_first_name(new_info[0]) and validate_last_name(new_info[1])

def validate_new_job(job_info:tuple) -> bool:

    return validate_job_type(job_info[0]) and validate_description(job_info[1]) and validate_budget(job_info[2]) and validate_contact(job_info[3])

def validate_username(username):
    if re.findall('^(?=[a-zA-Z0-9._]{5,20}$)(?!.*[_.]{2})[^_.].*[^_.]$',username) :
        return True
    else:
        return False

def validate_password(password):
    if re.findall('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[_#?!@$%^&*-]).{5,}$',password):
        return True
    else:
        return False

def validate_first_name(firstname):
    if re.findall('[A-Za-z]{2,15}',firstname) and re.findall('[^0-9]{2,15}',firstname)  and len(firstname) <=15 and not " " in firstname:
        return True
    else:
        return False

def validate_last_name(lastname):
    if re.findall('[A-Za-z]{2,15}',lastname) and re.findall('[^0-9]{2,15}',lastname)  and len(lastname) <=15 and not " " in lastname:
        return True
    else:
        return False

def validate_job_type(job):
    if re.findall('^(?=[a-zA-Z. _]{5,50}$)(?!.*[_.]{2})[^_.].*[^_.]$',job)  and len(job) <=50:
        return True
    else:
        return False

def validate_description(desc):
    if re.findall('^(?=[a-zA-Z0-9. _@,%!#$*-/n]{5,200}$)(?!.*[_.]{2})[^_.].*[^_.]$',desc)  and len(desc) <=200:
        return True
    else:
        return False

def validate_budget(budget):
    if budget>0:
        return True
    else:
        return False

def validate_contact(contact):
    if re.findall('^[0-9]{10}$',contact)  and len(contact)==10:
        return True
    else:
        return False