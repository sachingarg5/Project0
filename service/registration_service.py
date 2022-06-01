from repository.login_dao import insert_user, select_user_by_id
from repository.user_info_dao import insert_user_info
from service.validation_service import validate_login,validate_user_info

def validate_registration(input_dict):
   return validate_login((input_dict["username"], input_dict["password"])) and validate_user_info((input_dict["first_name"],input_dict["last_name"]))

def create_login(input):
    user_id = insert_user(input.get("username"), input.get("password"))

    if user_id is not None:
        return user_id

def create_user_info(user_id, input):
    login_dto = select_user_by_id(user_id)
    info_id = insert_user_info(login_dto, input.get("first_name"), input.get("last_name"))

    if info_id is not None:
        return info_id