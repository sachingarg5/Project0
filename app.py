from flask import Flask, render_template, request
from controller.registration_controller import get_registration_page, register_user
from repository.login_dao import insert_user, select_user
from models.login_dto import Login
from controller.home_controller import *
from controller.login_controller import *
from controller.create_job_controller import *

# def main():
#     print(insert_user("test_user_1","test_Pass_1"))
#     login_details=select_user("test_user_1","test_Pass_1")
#     print(f"username= {login_details.username}")

app = Flask(__name__)
app.secret_key="xyz"

@app.route('/', methods=["GET"])
def landing_page():
    return get_homepage()

@app.route('/login', methods=["GET"])
def login_page():
    return get_login_page()

@app.route('/login/input', methods=["POST"])
def user_login():
    return check_user_login(request.form)

@app.route('/registration')
def registration_page():
    return get_registration_page()

@app.route('/registration/register', methods=["POST"])
def register_new_user():
    return register_user(request.form)

@app.route('/create_job')
def create_job_page():
    return get_create_job_page()

@app.route('/create_job/job_details',methods=["POST"])
def create_new_job():
    return create_user_job(request.form)

@app.route('/view_jobs', methods=["GET"])
def view_posted_jobs():
    return get_posted_jobs()

if __name__ == "__main__":
    app.run(debug=True)