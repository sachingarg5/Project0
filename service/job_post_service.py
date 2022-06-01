from flask import session
from models.user_info_dto import User
from models.login_dto import Login
from repository.job_dao import insert_job_info
from repository.user_info_dao import select_by_user, select_user_info_by_id
from service.validation_service import validate_new_job


def validate_job_post(input_dict):
   return validate_new_job((input_dict["job_type"],(input_dict["description"]),(input_dict["budget"]),(input_dict["contact"])))

def create_new_job(input):
    if 'info_id' in session:
        info_id=session['info_id']
    else:
        return "Invalid Login"
    user= select_user_info_by_id(info_id)
    job_id=insert_job_info(user,input.get("job_type"),input.get("description"),input.get("budget"),input.get("contact"))
    if job_id is not None:
        return job_id