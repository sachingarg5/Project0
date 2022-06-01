from flask import render_template, session

from service.job_post_service import create_new_job
from repository.job_dao import select_job_by_id
from service.job_post_service import validate_job_post



def get_create_job_page():
    return render_template("create_job.html")

def create_user_job(new_job_input):
    input_dict = {
        "job_type": new_job_input["job_type"],
        "description": new_job_input["description"],
        "budget": new_job_input["budget"],
        "contact": new_job_input["contact"],}
        #validate data
    if validate_job_post(input_dict):
        # create new job
        job_id = create_new_job(new_job_input)
        if job_id is not None:
            return "Job Created Sucessfully"
    else:
        return"Invalid Data! Please Try Again"

def get_posted_jobs():
    if 'username' in session:
        username = session['username']
        job_details=select_job_by_id(session['info_id'])
    return render_template("view_jobs.html",username=username,jobs=job_details)